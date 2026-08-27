#!/usr/bin/env python3
"""Reject missing, stale, or structurally damaged documentation translations."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs"
LOCALES = {"fr": ROOT / "locales/fr", "ar": ROOT / "locales/ar"}


def parse(page: Path) -> tuple[dict, str]:
    content = page.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not match:
        raise ValueError("missing YAML metadata")
    return yaml.safe_load(match.group(1)) or {}, match.group(2)


def structures(text: str) -> dict[str, list[str]]:
    return {
        "fences": re.findall(r"^\s*```", text, re.MULTILINE),
        "backticks": re.findall(r"`", text),
        "links": re.findall(r"\]\(([^)]+)\)", text),
        "images": re.findall(r"!\[[^]]*\]\(([^)]+)\)", text),
        "headings": re.findall(r"^#{1,6} ", text, re.MULTILINE),
        "admonitions": re.findall(r"^\s*!!!", text, re.MULTILINE),
    }


def main() -> int:
    source_pages = {
        page.relative_to(SOURCE) for page in SOURCE.rglob("*.md")
    }
    errors: list[str] = []

    for locale, root in LOCALES.items():
        locale_pages = {page.relative_to(root) for page in root.rglob("*.md")}
        for missing in sorted(source_pages - locale_pages):
            errors.append(f"{locale}: missing page: {missing}")
        for extra in sorted(locale_pages - source_pages):
            errors.append(f"{locale}: unexpected page: {extra}")

        for relative in sorted(source_pages & locale_pages):
            source_page = SOURCE / relative
            translated_page = root / relative
            source_content = source_page.read_text(encoding="utf-8")
            try:
                metadata, translated_body = parse(translated_page)
                _, source_body = parse(source_page)
            except (ValueError, yaml.YAMLError) as exc:
                errors.append(f"{locale}/{relative}: {exc}")
                continue

            expected_hash = hashlib.sha256(source_content.encode()).hexdigest()
            if metadata.get("translation_source") != relative.as_posix():
                errors.append(f"{locale}/{relative}: incorrect translation_source")
            if metadata.get("translation_source_sha256") != expected_hash:
                errors.append(f"{locale}/{relative}: translation is stale")

            title = str(metadata.get("title", "")).strip()
            description = str(metadata.get("description", "")).strip()
            if not title:
                errors.append(f"{locale}/{relative}: missing localized title")
            if not description:
                errors.append(f"{locale}/{relative}: missing localized description")
            elif len(description) > 170:
                errors.append(
                    f"{locale}/{relative}: localized description exceeds 170 characters"
                )

            source_structure = structures(source_body)
            translated_structure = structures(translated_body)
            for name in source_structure:
                if source_structure[name] != translated_structure[name]:
                    errors.append(f"{locale}/{relative}: changed Markdown {name}")

            if "ZXQ" in translated_page.read_text(encoding="utf-8"):
                errors.append(f"{locale}/{relative}: unresolved translation placeholder")
            if re.search(r"\b(?:Examina|Exina)\.io\b", translated_body):
                errors.append(f"{locale}/{relative}: incorrect examina.io capitalization")
            if locale == "ar" and not re.search(r"[\u0600-\u06ff]", translated_body):
                errors.append(f"ar/{relative}: Arabic content is missing")

    if errors:
        print("\n".join(errors))
        print(f"Localization check failed with {len(errors)} error(s).")
        return 1

    print(
        f"Localization parity passed for {len(source_pages)} pages in "
        f"{', '.join(LOCALES)}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
