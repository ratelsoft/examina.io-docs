#!/usr/bin/env python3
"""Check that published API and UI claims match the application contract."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "reference" / "examina.io.v1.yaml"
HTTP_METHODS = {"get", "post", "put", "patch", "delete"}

# Normalized from the public Spring controller mappings on the application main
# branch. Placeholder names and Spring regexes do not change URL compatibility.
EXPECTED_ROUTES = {
    ("POST", "/exam"),
    ("GET", "/exams"),
    ("GET", "/exams/{}"),
    ("GET", "/exams/tag/{}"),
    ("GET", "/exams/tag/{}/{}"),
    ("GET", "/exam/{}/tags"),
    ("GET", "/exam/{}/examinees"),
    ("GET", "/exam/{}/examinees/{}"),
    ("GET", "/exam/{}"),
    ("DELETE", "/exam/{}"),
    ("POST", "/exam/{}/tags"),
    ("DELETE", "/exam/{}/tags"),
    ("DELETE", "/exam/{}/tags/all"),
    ("GET", "/exam/{}/settings"),
    ("PUT", "/exam/{}/settings"),
    ("PATCH", "/exam/{}/settings"),
    ("GET", "/exam/{}/examinee/{}"),
    ("DELETE", "/exam/{}/examinee/{}"),
    ("POST", "/exam/{}/examinees"),
    ("DELETE", "/exam/{}/examinees"),
    ("POST", "/exam/{}/groups"),
    ("GET", "/login/exam/{}/id/{}/token"),
    ("GET", "/login/exam/{}/code/{}/token"),
    ("GET", "/examinees"),
    ("POST", "/examinees"),
    ("POST", "/examinees/bulk-upsert"),
    ("GET", "/examinees/{}"),
    ("GET", "/examinee/{}"),
    ("PATCH", "/examinee/{}"),
    ("DELETE", "/examinee/{}"),
    ("GET", "/examinee/{}/exams"),
    ("GET", "/examinee/{}/exams/{}"),
    ("GET", "/groups"),
    ("GET", "/groups/{}"),
    ("POST", "/groups"),
    ("POST", "/groups/{}"),
    ("POST", "/group"),
    ("GET", "/group/{}"),
    ("DELETE", "/group/{}"),
    ("POST", "/group/{}/examinees"),
    ("GET", "/group/{}/examinees"),
    ("DELETE", "/group/{}/examinees"),
    ("POST", "/group/{}/groups"),
    ("POST", "/assignments"),
    ("GET", "/assignments/{}"),
    ("PATCH", "/assignments/{}"),
    ("DELETE", "/assignments/{}"),
    ("POST", "/exam-sessions"),
    ("GET", "/results"),
    ("GET", "/results/{}"),
    ("GET", "/webhook-endpoints"),
    ("POST", "/webhook-endpoints"),
    ("DELETE", "/webhook-endpoints/{}"),
    ("GET", "/webhook-endpoints/deliveries"),
    ("POST", "/webhook-endpoints/deliveries/{}/retry"),
}

ENUM_CONTRACTS = (
    ("reference/raw/Base Exam Schema.json", ("properties", "examPaperFlow", "enum"),
     ["Force Continuous", "Client Controlled", "Server Controlled"]),
    ("reference/raw/Base Exam Settings Schema.json",
     ("properties", "handheldSettings", "properties", "phoneExamPage", "enum"),
     ["REGULAR", "MOBILE"]),
    ("reference/raw/Base Exam Settings Schema.json",
     ("properties", "handheldSettings", "properties", "tabletExamPage", "enum"),
     ["REGULAR", "MOBILE"]),
    ("reference/raw/Base Exam Settings Schema.json",
     ("properties", "internetDisconnectionPolicy", "properties", "onDisconnect", "enum"),
     ["DO_NOTHING", "PAUSE_EXAM", "LOGOUT_EXAMINEE"]),
    ("reference/raw/Base Exam Settings Schema.json",
     ("properties", "proctorPolicy", "properties", "onDisconnect", "enum"),
     ["DO_NOTHING", "PAUSE_EXAM", "LOGOUT_EXAMINEE"]),
    ("reference/raw/Change Exam Settings Schema.json", ("properties", "phoneExamPage", "enum"),
     ["REGULAR", "MOBILE"]),
    ("reference/raw/Change Exam Settings Schema.json", ("properties", "tabletExamPage", "enum"),
     ["REGULAR", "MOBILE"]),
    ("reference/raw/Change Exam Settings Schema.json",
     ("properties", "internetPolicyDisconnect", "enum"),
     ["DO_NOTHING", "PAUSE_EXAM", "LOGOUT_EXAMINEE"]),
    ("reference/raw/Change Exam Settings Schema.json",
     ("properties", "proctorPolicyDisconnect", "enum"),
     ["DO_NOTHING", "PAUSE_EXAM", "LOGOUT_EXAMINEE"]),
)


def normalize(path: str) -> str:
    return re.sub(r"\{[^}]+}", "{}", path)


def nested(document: dict, keys: tuple[str, ...]):
    value = document
    for key in keys:
        value = value[key]
    return value


def main() -> int:
    spec = yaml.safe_load(SPEC.read_text(encoding="utf-8"))
    documented = {
        (method.upper(), normalize(path))
        for path, item in spec["paths"].items()
        for method in item
        if method in HTTP_METHODS
    }

    errors: list[str] = []
    missing = EXPECTED_ROUTES - documented
    extra = documented - EXPECTED_ROUTES
    if missing:
        errors.append("Undocumented application routes: " + repr(sorted(missing)))
    if extra:
        errors.append("Documented routes absent from the application: " + repr(sorted(extra)))

    for relative_path, keys, expected in ENUM_CONTRACTS:
        document = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
        try:
            actual = nested(document, keys)
        except KeyError:
            actual = None
        if actual != expected:
            errors.append(f"{relative_path}:{'.'.join(keys)} must declare enum {expected!r}")

    component_enums = {
        "ConnectionStatus": ["CONNECTED", "READY", "RUNNING", "DISCONNECTED", "FINISHED"],
        "WebhookEventType": ["result.completed"],
        "WebhookDeliveryStatus": ["PENDING", "DELIVERED", "FAILED"],
    }
    for name, expected in component_enums.items():
        actual = spec.get("components", {}).get("schemas", {}).get(name, {}).get("enum")
        if actual != expected:
            errors.append(f"components.schemas.{name} must declare enum {expected!r}")

    for path in (
        "/login/exam/{examId}/code/{examineeCode}/token",
        "/login/exam/{examId}/id/{examineeId}/token",
    ):
        operation = spec["paths"][path]["get"]
        duration = [p for p in operation.get("parameters", []) if p.get("name") == "duration"]
        if len(duration) != 1 or duration[0].get("in") != "query":
            errors.append(f"{path}: duration must be one optional query parameter")
        if "requestBody" in operation:
            errors.append(f"{path}: GET must not advertise a request body")

    markdown_pages = list((ROOT / "docs").rglob("*.md"))
    page_text = {page: page.read_text(encoding="utf-8") for page in markdown_pages}
    claims = "\n".join(page_text.values())
    forbidden = (
        "Import Questions from File",
        "Import Paper from File",
        "Edit → Configure Defaults",
    )
    for claim in forbidden:
        if claim in claims:
            errors.append(f"Documentation still advertises unavailable behavior: {claim}")

    for page, content in page_text.items():
        match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
        if not match:
            errors.append(f"{page.relative_to(ROOT)}: missing YAML metadata")
            continue
        metadata = yaml.safe_load(match.group(1)) or {}
        if not str(metadata.get("title", "")).strip():
            errors.append(f"{page.relative_to(ROOT)}: missing SEO title")
        description = str(metadata.get("description", "")).strip()
        if not description:
            errors.append(f"{page.relative_to(ROOT)}: missing SEO description")
        elif len(description) > 170:
            errors.append(f"{page.relative_to(ROOT)}: SEO description exceeds 170 characters")

    if errors:
        print("\n".join(errors))
        return 1

    print(f"Application contract check passed for {len(documented)} public API operations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
