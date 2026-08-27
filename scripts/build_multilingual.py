#!/usr/bin/env python3
"""Build every localized guide site into one Pages artifact."""

from __future__ import annotations

import subprocess


def build(config: str) -> None:
    subprocess.run(["mkdocs", "build", "--strict", "--config-file", config], check=True)


def main() -> int:
    for config in ("mkdocs.yml", "mkdocs.fr.yml", "mkdocs.ar.yml",
                   "mkdocs.es-419.yml", "mkdocs.pt-BR.yml"):
        build(config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
