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
mkdocs serve
```

Build the complete production artifact:

```bash
mkdocs build --strict
npx --yes @redocly/cli@2.47.0 build-docs reference/examina.io.v1.yaml \
  --output site/api/index.html \
  --template redoc-template.hbs \
  --templateOptions.metaDescription "REST API reference for integrating with examina.io." \
  --title "API Reference | examina.io Docs"
python scripts/check_internal_links.py site
```

Changes pushed to `main` are validated and deployed to GitHub Pages by
`.github/workflows/deploy-pages.yml`.
