# Sandworm Subterranean Systems

Sandworm Subterranean Systems is an exploratory, self-sovereign public website about why careful subterranean work might matter: safer road crossings for animals, transport tunnels, erosion control, future tunnel spoil as a resource, geopolymer blocks, artificial reefs, quiet wave-energy questions, sand batteries, community wealth and film/documentary trails.

The site is built as static HTML so it can run on GitHub Pages without a build service.

## How it works

The source of truth is `tools/build_site.py`.

In simple terms:

1. The Python file stores the page list, builder list, and source links.
2. Running it writes the public `.html` pages.
3. The builder pages let a visitor fill in a small form, preview Markdown, copy it, or download a `.md` file.
4. Draft WebP hero images live in `assets/img/heroes/` and can be replaced later without changing the page structure.

## Local build

```powershell
python tools\build_site.py
```

Then open `index.html` in a browser, or run a tiny local server:

```powershell
python -m http.server 8080
```

## Public posture

This is a proposal and exploration workbench. It does not claim approval from Traditional Owners, Elders, councils, governments, schools, businesses, sponsors, scientists, engineers, or community groups.

The source documents are treated as raw concept material. Public claims should stay source-aware, consent-aware, and open to correction.
