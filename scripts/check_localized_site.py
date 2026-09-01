#!/usr/bin/env python3
"""Validate generated multilingual URLs, metadata, and hreflang relationships."""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"
ORIGIN = "https://docs.examina.io"
LANGUAGES = {"en": "", "fr": "fr", "ar": "ar", "es-419": "es-419", "pt-BR": "pt-br"}


class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.html_lang = ""
        self.body_dir = ""
        self.canonical = ""
        self.alternates: dict[str, str] = {}
        self.language_links: dict[str, str] = {}
        self.description = ""
        self.social: dict[str, str] = {}
        self.json_ld: list[str] = []
        self._json_ld_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.html_lang = values.get("lang") or ""
        elif tag == "body":
            self.body_dir = values.get("dir") or ""
        elif tag == "meta" and values.get("name") == "description":
            self.description = values.get("content") or ""
        elif tag == "meta" and values.get("property", "").startswith("og:"):
            self.social[values.get("property") or ""] = values.get("content") or ""
        elif tag == "meta" and values.get("name", "").startswith("twitter:"):
            self.social[values.get("name") or ""] = values.get("content") or ""
        elif tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href") or ""
        elif tag == "link" and values.get("rel") == "alternate":
            hreflang = values.get("hreflang")
            if hreflang:
                self.alternates[hreflang] = values.get("href") or ""
        elif tag == "a" and "md-select__link" in (values.get("class") or "").split():
            hreflang = values.get("hreflang")
            if hreflang:
                self.language_links[hreflang] = values.get("href") or ""
        elif tag == "script" and values.get("type") == "application/ld+json":
            self._json_ld_depth += 1
            self.json_ld.append("")

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._json_ld_depth:
            self._json_ld_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._json_ld_depth:
            self.json_ld[-1] += data


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
            expected_language_links = {
                lang: urlsplit(expected_alternates[lang]).path for lang in LANGUAGES
            }
            is_standalone_api_reference = language == "en" and relative == Path("api/index.md")
            if not is_standalone_api_reference and parsed.language_links != expected_language_links:
                errors.append(f"{label}: language selector links do not use canonical page paths")
            if not parsed.description.strip():
                errors.append(f"{label}: generated meta description is missing")
            required_social = {
                "og:type", "og:site_name", "og:title", "og:description", "og:url",
                "og:image", "og:image:width", "og:image:height", "og:image:alt",
                "twitter:card", "twitter:title", "twitter:description", "twitter:image",
            }
            if set(parsed.social) != required_social or any(
                not value.strip() for value in parsed.social.values()
            ):
                errors.append(f"{label}: social metadata is incomplete")
            if parsed.social.get("og:url") != expected_canonical:
                errors.append(f"{label}: Open Graph URL does not match the canonical URL")
            if parsed.social.get("og:description") != parsed.description:
                errors.append(f"{label}: Open Graph description differs from the meta description")
            if len(parsed.json_ld) != 1:
                errors.append(f"{label}: expected exactly one JSON-LD block")
            else:
                try:
                    structured = json.loads(parsed.json_ld[0])
                    graph = structured.get("@graph", [])
                    types = {item.get("@type") for item in graph if isinstance(item, dict)}
                    expected_types = {"Organization", "WebSite", "WebPage"}
                    if relative != Path("index.md"):
                        expected_types.add("BreadcrumbList")
                    if structured.get("@context") != "https://schema.org" or types != expected_types:
                        errors.append(f"{label}: structured-data graph is incomplete")
                except (json.JSONDecodeError, AttributeError):
                    errors.append(f"{label}: JSON-LD is not valid JSON")

    routing = SITE / "javascripts/language-routing.js"
    if not routing.exists():
        errors.append("language query compatibility script is missing")

    sitemap_paths = ("/sitemap.xml", "/fr/sitemap.xml", "/ar/sitemap.xml",
                     "/es-419/sitemap.xml", "/pt-br/sitemap.xml")
    index_path = SITE / "sitemap-index.xml"
    if not index_path.exists():
        errors.append("sitemap index is missing")
    else:
        try:
            tree = ElementTree.parse(index_path)
            namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            indexed = [item.text for item in tree.findall("sm:sitemap/sm:loc", namespace)]
            expected = [f"{ORIGIN}{path}" for path in sitemap_paths]
            if indexed != expected:
                errors.append("sitemap index does not contain the five locale sitemaps")
        except ElementTree.ParseError:
            errors.append("sitemap index is not valid XML")

    robots = (SITE / "robots.txt").read_text(encoding="utf-8")
    if f"Sitemap: {ORIGIN}/sitemap-index.xml" not in robots:
        errors.append("robots.txt does not advertise the sitemap index")

    if errors:
        print("\n".join(errors))
        print(f"Localized site check failed with {len(errors)} error(s).")
        return 1

    print(f"Localized SEO metadata passed for {len(pages)} pages in {len(LANGUAGES)} locales.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
