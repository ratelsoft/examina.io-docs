#!/usr/bin/env python3
"""Validate generated documentation links, anchors, and code rendering."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []
        self.ids: set[str] = set()
        self.article_depth = 0
        self.code_depth = 0
        self.literal_backticks = 0

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = dict(attrs)
        if tag == "article":
            self.article_depth += 1
        elif tag == "code":
            self.code_depth += 1

        element_id = attributes.get("id")
        if element_id:
            self.ids.add(element_id)

        attribute = "href" if tag in {"a", "link"} else "src"
        if tag in {"a", "link", "img", "script"} and attributes.get(attribute):
            self.references.append(attributes[attribute] or "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "article":
            self.article_depth = max(0, self.article_depth - 1)
        elif tag == "code":
            self.code_depth = max(0, self.code_depth - 1)

    def handle_data(self, data: str) -> None:
        if self.article_depth and not self.code_depth:
            self.literal_backticks += data.count("`")


def destination(root: Path, source: Path, reference: str) -> Path:
    parsed = urlsplit(reference)
    path = unquote(parsed.path)
    target = root / path.lstrip("/") if path.startswith("/") else source.parent / path
    if path.endswith("/") or not Path(path).suffix:
        target /= "index.html"
    return target.resolve()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("site", nargs="?", default="site")
    args = parser.parse_args()

    root = Path(args.site).resolve()
    pages: dict[Path, PageParser] = {}
    for page in root.rglob("*.html"):
        parsed_page = PageParser()
        parsed_page.feed(page.read_text(encoding="utf-8", errors="replace"))
        pages[page.resolve()] = parsed_page

    errors: list[str] = []
    for source, parsed_page in pages.items():
        if parsed_page.literal_backticks:
            errors.append(
                f"{source.relative_to(root)}: {parsed_page.literal_backticks} "
                "unrendered backtick(s) in article content"
            )

        for reference in parsed_page.references:
            parsed = urlsplit(reference)
            if (
                parsed.scheme
                or parsed.netloc
                or reference.startswith(("#", "mailto:", "tel:", "javascript:", "data:"))
            ):
                continue

            target = destination(root, source, reference)
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f"{source.relative_to(root)}: outside site: {reference}")
                continue

            if not target.exists():
                errors.append(f"{source.relative_to(root)}: missing: {reference}")
                continue

            if parsed.fragment and target.suffix == ".html":
                target_page = pages.get(target)
                if target_page and parsed.fragment not in target_page.ids:
                    errors.append(
                        f"{source.relative_to(root)}: missing anchor: {reference}"
                    )

    if errors:
        print("\n".join(errors))
        print(f"Internal link check failed with {len(errors)} error(s).")
        return 1

    print(f"Checked {len(pages)} HTML pages; no broken internal links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
