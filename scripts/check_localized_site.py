#!/usr/bin/env python3
"""Validate generated multilingual URLs, metadata, and hreflang relationships."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"
ORIGIN = "https://docs.examina.io"
LANGUAGES = {"en": "", "fr": "fr", "ar": "ar"}


class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.html_lang = ""
        self.body_dir = ""
        self.canonical = ""
        self.alternates: dict[str, str] = {}
        self.description = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.html_lang = values.get("lang") or ""
        elif tag == "body":
            self.body_dir = values.get("dir") or ""
        elif tag == "meta" and values.get("name") == "description":
            self.description = values.get("content") or ""
        elif tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href") or ""
        elif tag == "link" and values.get("rel") == "alternate":
            hreflang = values.get("hreflang")
            if hreflang:
                self.alternates[hreflang] = values.get("href") or ""


def output_path(relative: Path, prefix: str) -> Path:
    page = relative.with_suffix("")
    base = SITE / prefix if prefix else SITE
    if page.name == "index":
        return base / page.parent / "index.html"
    return base / page / "index.html"


def public_url(relative: Path, prefix: str) -> str:
    page_path = relative.with_suffix("")
    page = page_path.parent.as_posix() if page_path.name == "index" else page_path.as_posix()
    page = "" if page == "." else page
    language = f"/{prefix}" if prefix else ""
    suffix = f"{page}/" if page else ""
    return f"{ORIGIN}{language}/{suffix}"


def main() -> int:
    errors: list[str] = []
    pages = sorted(page.relative_to(DOCS) for page in DOCS.rglob("*.md"))

    for relative in pages:
        expected_alternates = {
            language: public_url(relative, prefix)
            for language, prefix in LANGUAGES.items()
        }
        expected_alternates["x-default"] = expected_alternates["en"]

        for language, prefix in LANGUAGES.items():
            page = output_path(relative, prefix)
            label = f"{language}/{relative}"
            if not page.exists():
                errors.append(f"{label}: generated page is missing")
                continue
            parsed = MetadataParser()
            parsed.feed(page.read_text(encoding="utf-8", errors="replace"))

            if parsed.html_lang != language:
                errors.append(f"{label}: html lang is {parsed.html_lang!r}")
            expected_direction = "rtl" if language == "ar" else "ltr"
            if parsed.body_dir != expected_direction:
                errors.append(f"{label}: body direction is {parsed.body_dir!r}")
            expected_canonical = public_url(relative, prefix)
            if parsed.canonical != expected_canonical:
                errors.append(f"{label}: canonical is {parsed.canonical!r}")
            if parsed.alternates != expected_alternates:
                errors.append(f"{label}: hreflang set does not match page variants")
            if not parsed.description.strip():
                errors.append(f"{label}: generated meta description is missing")

    routing = SITE / "javascripts/language-routing.js"
    if not routing.exists():
        errors.append("language query compatibility script is missing")

    robots = (SITE / "robots.txt").read_text(encoding="utf-8")
    for sitemap in ("/sitemap.xml", "/fr/sitemap.xml", "/ar/sitemap.xml"):
        if f"Sitemap: {ORIGIN}{sitemap}" not in robots:
            errors.append(f"robots.txt does not advertise {sitemap}")

    if errors:
        print("\n".join(errors))
        print(f"Localized site check failed with {len(errors)} error(s).")
        return 1

    print(f"Localized SEO metadata passed for {len(pages)} pages in 3 languages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
