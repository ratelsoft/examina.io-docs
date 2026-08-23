#!/usr/bin/env python3
"""Check that published API and UI claims match the application contract."""

from __future__ import annotations

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
    ("GET", "/examinees/{}"),
    ("GET", "/examinee/{}"),
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
}


def normalize(path: str) -> str:
    return re.sub(r"\{[^}]+}", "{}", path)


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
        "one-time login URL",
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
