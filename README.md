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

English source remains in `docs/` and keeps its existing public URLs. French,
Arabic, Latin American Spanish, and Brazilian Portuguese pages mirror the same
paths under `locales/fr/`, `locales/ar/`, `locales/es-419/`, and
`locales/pt-BR/`; they are published beneath `/fr/`, `/ar/`, `/es-419/`, and
`/pt-br/`. Localized metadata records the
English source path and SHA-256 digest. `check_localizations.py` fails when a
translation is missing, structurally damaged, or stale after its English page
changes; update and review the translated page rather than changing only the
recorded digest.

The generated-site checks validate internal files and anchors, Markdown code
rendering, localized canonical URLs, reciprocal page-level `hreflang` links,
social metadata, structured page and breadcrumb data, Arabic right-to-left
rendering, all five locale sitemaps, and the sitemap index submitted to search
engines.

Changes pushed to `main` are validated and deployed to GitHub Pages by
`.github/workflows/deploy-pages.yml`.
