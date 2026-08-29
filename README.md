# Sandworm Subterranean Systems

<!-- github-organisation:start -->

## Project links and history

- First substantive build: 14 June 2026.
- GitHub repository: [sandworm-subterranean-systems](https://github.com/auraofintelligence/sandworm-subterranean-systems).
- Public site: [visit the public site](https://auraofintelligence.github.io/sandworm-subterranean-systems/).

## Related public projects

Each link below reflects an evidenced family, lineage or direct connection. This project has 10 relevant public connections.

### Aura Systems Image Atlas source projects

- [aura-systems-image-atlas](https://github.com/auraofintelligence/aura-systems-image-atlas) - [public page](https://auraofintelligence.github.io/aura-systems-image-atlas/) - source project represented in this visual atlas, source project represented in visual atlas.
- [civilisation-of-sand](https://github.com/auraofintelligence/civilisation-of-sand) - [public page](https://auraofintelligence.github.io/civilisation-of-sand/) - explicit cross-reference, shared community programme.
- [shared-table-initiative](https://github.com/auraofintelligence/shared-table-initiative) - [public page](https://auraofintelligence.github.io/shared-table-initiative/) - shared community programme.
- [straddie-clean-energy-superpower](https://github.com/auraofintelligence/straddie-clean-energy-superpower) - [public page](https://auraofintelligence.github.io/straddie-clean-energy-superpower/) - explicit cross-reference, shared community programme.
- [straddie-makerspace-lab](https://github.com/auraofintelligence/straddie-makerspace-lab) - [public page](https://auraofintelligence.github.io/straddie-makerspace-lab/) - shared community programme.

### Circular making and local infrastructure

- [grain-by-grain](https://github.com/auraofintelligence/grain-by-grain) - [public page](https://auraofintelligence.github.io/grain-by-grain/) - explicit cross-reference, shared community programme.
- [straddie-tip-loop-lab](https://github.com/auraofintelligence/straddie-tip-loop-lab) - [public page](https://auraofintelligence.github.io/straddie-tip-loop-lab/) - shared community programme.

### Direct and other supported connections

- [minjerribah-living-twin](https://github.com/auraofintelligence/minjerribah-living-twin) - [public page](https://auraofintelligence.github.io/minjerribah-living-twin/) - explicit cross-reference.
- [Minjerribah-Resilience](https://github.com/auraofintelligence/Minjerribah-Resilience) - [public page](https://auraofintelligence.github.io/Minjerribah-Resilience/) - explicit cross-reference.
- [minjerribah-screen-media-network](https://github.com/auraofintelligence/minjerribah-screen-media-network) - [public page](https://auraofintelligence.github.io/minjerribah-screen-media-network/) - explicit cross-reference.

<!-- github-organisation:end -->

Sandworm Subterranean Systems is an exploratory, self-sovereign public website about why careful subterranean work might matter: autonomous transport arteries, fewer wildlife road hits, less road damage, 24/7 town connection, erosion control, future tunnel spoil as a resource, geopolymer blocks, artificial reefs, quiet wave-energy questions, sand batteries, community wealth and film/documentary trails.

The site is built as static HTML so it can run on GitHub Pages without a build service.

## Public page

- [Open Sandworm Subterranean Systems](https://auraofintelligence.github.io/sandworm-subterranean-systems/)

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

## Related pages

- [Minjerribah Screen & Media Network](https://auraofintelligence.github.io/minjerribah-screen-media-network/)
- [Minjerribah Living Twin](https://auraofintelligence.github.io/minjerribah-living-twin/)
- [Civilisation of Sand](https://auraofintelligence.github.io/civilisation-of-sand/)

## Licence and reuse

See `LICENCE.md` for the local Sandworm licence. In short: people control their own generated Markdown, the public repo can be studied or forked as a scaffold for public-interest repos with honest attribution, and Sandworm story materials, brand assets and claims cannot be repackaged or presented as endorsement.
