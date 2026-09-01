#!/usr/bin/env python3
"""Build every localized guide site into one Pages artifact."""

from __future__ import annotations

import subprocess
from pathlib import Path


SITEMAPS = (
    "https://docs.examina.io/sitemap.xml",
    "https://docs.examina.io/fr/sitemap.xml",
    "https://docs.examina.io/ar/sitemap.xml",
    "https://docs.examina.io/es-419/sitemap.xml",
    "https://docs.examina.io/pt-br/sitemap.xml",
)


def build(config: str) -> None:
    subprocess.run(["mkdocs", "build", "--strict", "--config-file", config], check=True)


def write_sitemap_index() -> None:
    entries = "\n".join(
        f"  <sitemap><loc>{sitemap}</loc></sitemap>" for sitemap in SITEMAPS
    )
    content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n"
        "</sitemapindex>\n"
    )
    Path("site/sitemap-index.xml").write_text(content, encoding="utf-8")


def main() -> int:
    for config in ("mkdocs.yml", "mkdocs.fr.yml", "mkdocs.ar.yml",
                   "mkdocs.es-419.yml", "mkdocs.pt-BR.yml"):
        build(config)
    write_sitemap_index()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
