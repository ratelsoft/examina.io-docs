# examina.io documentation

The source for the public product and API documentation at
[docs.examina.io](https://docs.examina.io).

The site is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
The OpenAPI reference is rendered as a self-contained page with
[Redocly CLI](https://redocly.com/docs/cli/).

## Local development

Requirements:

- Python 3.11 or newer
- Node.js 20 or newer

Install and build the guide site:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/build_multilingual.py
python -m http.server 8000 --directory site
```

Build the complete production artifact:

```bash
python scripts/build_multilingual.py
python scripts/check_localizations.py
npx --yes @redocly/cli@2.47.0 build-docs reference/examina.io.v1.yaml \
  --output site/api/index.html \
  --template redoc-template.hbs \
  --templateOptions.metaDescription "REST API reference for integrating with examina.io." \
  --title "API Reference | examina.io Docs"
python scripts/check_localized_site.py
python scripts/check_internal_links.py site
```

English source remains in `docs/` and keeps its existing public URLs. French
and Arabic pages mirror the same paths under `locales/fr/` and `locales/ar/`,
and are published beneath `/fr/` and `/ar/`. Localized metadata records the
English source path and SHA-256 digest. `check_localizations.py` fails when a
translation is missing, structurally damaged, or stale after its English page
changes; update and review the translated page rather than changing only the
recorded digest.

The generated-site checks validate internal files and anchors, Markdown code
rendering, localized canonical URLs, reciprocal page-level `hreflang` links,
Arabic right-to-left rendering, and all three sitemaps.

Changes pushed to `main` are validated and deployed to GitHub Pages by
`.github/workflows/deploy-pages.yml`.
