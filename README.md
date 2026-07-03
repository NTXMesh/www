# ntxmesh-site

Website for **NTX Mesh** (ntxmesh.com).

A static-HTML site for the DFW / North Texas mesh community, supporting both
Meshtastic and MeshCore. This is a **beta / work-in-progress** rebuild and is
not the production NTX Mesh website.

## Structure

```
index.html            Home
info/  connect/  devices/  settings/  channels/  howtos/  blog/  reports/
assets/css/style.css  Site stylesheet
assets/images/        Images
CNAME                 Custom domain (ntxmesh.com)
archive-astro/        Previous Astro + Tailwind site (kept for reference)
```

## Local preview

It's plain static HTML — no build step. Serve the root with any static server,
e.g.:

```
python -m http.server 8000
```

then open http://localhost:8000/.

## Deploy

Pushes to `main` publish to GitHub Pages via
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml), which uploads the
static files at the repo root (excluding `archive-astro/`).

## License

You're welcome to reuse this site — just give credit.

- **Code** (HTML, CSS, JS) — [MIT License](LICENSE)
- **Content** (text, copy, original images) — [Creative Commons Attribution 4.0
  (CC BY 4.0)](LICENSE-CONTENT)

Both require attribution but otherwise let you use, modify, and redistribute
freely, including commercially. Third-party names and logos (Meshtastic,
MeshCore, Discord, etc.) belong to their respective owners and aren't covered by
these licenses.
