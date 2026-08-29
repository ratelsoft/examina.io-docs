#!/usr/bin/env python3
"""Reject localized pages whose screenshots silently resolve to English assets."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs"
LOCALES = {
    "fr": ROOT / "locales/fr",
    "ar": ROOT / "locales/ar",
    "es-419": ROOT / "locales/es-419",
    "pt-BR": ROOT / "locales/pt-BR",
}
IMAGE_PATTERN = re.compile(r"!\[[^]]*\]\(([^)]+)\)")


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def main() -> int:
    errors: list[str] = []

    for source_page in sorted(SOURCE.rglob("*.md")):
        relative_page = source_page.relative_to(SOURCE)
        source_refs = [
            ref for ref in IMAGE_PATTERN.findall(source_page.read_text(encoding="utf-8"))
            if "://" not in ref
        ]

        for locale, locale_root in LOCALES.items():
            locale_page = locale_root / relative_page
            if not locale_page.exists():
                continue
            locale_refs = [
                ref for ref in IMAGE_PATTERN.findall(locale_page.read_text(encoding="utf-8"))
                if "://" not in ref
            ]
            for ref in locale_refs:
                asset = locale_page.parent / ref
                if not asset.exists():
                    errors.append(f"{locale}/{relative_page}: missing screenshot {ref}")
                    continue
                resolved = asset.resolve()
                if not is_within(resolved, locale_root.resolve()):
                    errors.append(
                        f"{locale}/{relative_page}: screenshot falls back outside its locale: {ref}"
                    )

            if len(locale_refs) != len(source_refs):
                errors.append(
                    f"{locale}/{relative_page}: screenshot count differs from English source"
                )

    if errors:
        print("\n".join(errors))
        print(f"Localized screenshot check failed with {len(errors)} error(s).")
        return 1

    print(f"Localized screenshots are self-contained for {len(LOCALES)} locales.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
