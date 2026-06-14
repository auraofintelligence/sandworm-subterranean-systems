from __future__ import annotations

import json
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_TITLE = "Sandworm Subterranean Systems"
BASE_URL = "https://auraofintelligence.github.io/sandworm-subterranean-systems/"
ASSET_VERSION = "20260614-self-sovereign-hints"
DESCRIPTION = (
    "A self-sovereign public workbench for exploring why to dig carefully: maker-space starts, "
    "modern ferry-gateway data, autonomous transport corridors, future tunnel spoil as a resource, artificial reefs, "
    "sand batteries, community wealth and film-ready story trails."
)


PAGES = [
    {
        "id": "home",
        "label": "Home",
        "href": "index.html",
        "title": "Sandworm Subterranean Systems",
        "description": DESCRIPTION,
    },
    {
        "id": "start",
        "label": "Why dig?",
        "href": "start.html",
        "title": "Why Dig?",
        "description": "What reasons might make careful digging worth exploring: fewer road strikes, less road damage, parking relief, 24/7 access, erosion care, future spoil as resource, reef habitat, power storage and community assets?",
    },
    {
        "id": "makerspace",
        "label": "Ferry lab",
        "href": "makerspace.html",
        "title": "Begin At Dunwich / Gumpi",
        "description": "Could the $41M ferry terminal upgrade consultation, running 28 May to 21 June 2026, become a practical civic lab for making, mapping, modern transport flow and first tunnel questions?",
    },
    {
        "id": "digital-twin",
        "label": "Twin layer",
        "href": "digital-twin.html",
        "title": "Map The Place Before The Claim",
        "description": "A digital twin trail for road corridors, ferry movement, erosion edges, reef sites, permissions and public-source evidence.",
    },
    {
        "id": "sandworm-lab",
        "label": "Spoil loop",
        "href": "sandworm-lab.html",
        "title": "Make Spoil Useful",
        "description": "If tunnelling begins, treat sand spoil as a material stream for blocks, reef modules, dune stabilisation, tunnel lining tests and sand batteries.",
    },
    {
        "id": "civilisation",
        "label": "Reefs + power",
        "href": "civilisation-of-sand.html",
        "title": "Reefs, Banks And Quiet Power",
        "description": "Explore reef geometry, surf-side banks, wave-pressure ideas, non-spinning anchors, sand batteries and ecological review gates.",
    },
    {
        "id": "wealth",
        "label": "Wealth fund",
        "href": "wealth-fund.html",
        "title": "Sovereign Wealth And Community Hours",
        "description": "Connect community-owned assets, energy revenue, transparent receipts, C-Hours and patient local reinvestment.",
    },
    {
        "id": "culture",
        "label": "Film trail",
        "href": "film-documentary-trail.html",
        "title": "Back The Fiction Or Documentary",
        "description": "Could fiction, documentary and festival pathways help people inspect the plan without being pushed into belief?",
    },
    {
        "id": "builders",
        "label": "Builders",
        "href": "builders/index.html",
        "title": "Markdown Builders",
        "description": "Browser-only forms that turn questions, trails and project notes into clean Markdown drafts.",
    },
    {
        "id": "boundaries",
        "label": "Boundaries",
        "href": "boundaries.html",
        "title": "Boundaries Keep The Work Human",
        "description": "Consent, cultural authority, ecological safety, public claims, engineering review and data dignity for the Sandworm trail.",
    },
    {
        "id": "sources",
        "label": "Sources",
        "href": "sources.html",
        "title": "Source Trail",
        "description": "The documents and connected repositories that informed this first Sandworm public draft.",
    },
    {
        "id": "licence",
        "label": "Licence",
        "href": "licence.html",
        "title": "Licence And Reuse",
        "description": "How people can read, question, fork, create their own repo, adapt the builders and generate Markdown while keeping provenance, safety and authority clear.",
    },
    {
        "id": "site-map",
        "label": "Site map",
        "href": "site-map.html",
        "title": "Site Map",
        "description": "All public pages, builder pages, Markdown templates and source bridges.",
    },
]


HERO_IMAGES = {
    "home": "assets/img/heroes/home-system.webp",
    "start": "assets/img/heroes/why-dig.webp",
    "makerspace": "assets/img/heroes/gumpi-terminal.webp",
    "digital-twin": "assets/img/heroes/twin-layer.webp",
    "sandworm-lab": "assets/img/heroes/spoil-loop.webp",
    "civilisation": "assets/img/heroes/reef-energy.webp",
    "wealth": "assets/img/heroes/wealth-hours.webp",
    "culture": "assets/img/heroes/film-case.webp",
    "builders": "assets/img/heroes/builders.webp",
    "boundaries": "assets/img/heroes/boundaries.webp",
    "sources": "assets/img/heroes/sources.webp",
    "licence": "assets/img/heroes/sources.webp",
    "site-map": "assets/img/heroes/sources.webp",
}


COMPANION_LINKS = [
    {
        "title": "Dunwich / Gumpi Ferry Terminal Open Data Lab",
        "site": "https://auraofintelligence.github.io/dunwich-gumpi-ferry-terminal-open-data-lab/",
        "repo": "https://github.com/auraofintelligence/dunwich-gumpi-ferry-terminal-open-data-lab",
        "summary": "The grounded start node: $41M upgrade consultation, official-source trail, 360-photo evidence, open-data workflows and simulation practice around the ferry gateway.",
    },
    {
        "title": "Straddie Maker-Space Lab",
        "site": "https://auraofintelligence.github.io/straddie-makerspace-lab/",
        "repo": "https://github.com/auraofintelligence/straddie-makerspace-lab",
        "summary": "The workshop doorway for tools, forms, sand, concrete, repair, prototyping and small public learning loops.",
    },
    {
        "title": "Straddie Digital Twin Builders",
        "site": "https://auraofintelligence.github.io/straddie-digital-twin-builders/",
        "repo": "https://github.com/auraofintelligence/straddie-digital-twin-builders",
        "summary": "The mapping and simulation doorway for private, shared and bioregional twins with consent boundaries visible.",
    },
    {
        "title": "P4A / Purple Party For Australia",
        "site": "https://auraofintelligence.github.io/p4a_xyz/",
        "repo": "https://github.com/auraofintelligence/p4a_xyz",
        "summary": "The roots-up civic system where C-Hours, public ledgers, contribution receipts and grassroots governance are being tested.",
    },
    {
        "title": "Stradbroke Grants Lab",
        "site": "https://auraofintelligence.github.io/stradbroke-grants-lab/",
        "repo": "https://github.com/auraofintelligence/stradbroke-grants-lab",
        "summary": "The funding workbench for grant watchlists, windows, applicant profiles, grant-readiness Markdown, milestones and acquittal evidence.",
    },
    {
        "title": "How To Use Markdown With AI",
        "site": "https://auraofintelligence.github.io/how-to-use-md-with-ai/",
        "repo": "https://github.com/auraofintelligence/how-to-use-md-with-ai",
        "summary": "A plain-English guide for turning form answers into portable `.md` context files for AI tools, with privacy, source and review boundaries visible.",
    },
    {
        "title": "Mineral Moonshots",
        "site": "https://auraofintelligence.github.io/mineral-moonshots/",
        "repo": "https://github.com/auraofintelligence/mineral-moonshots",
        "summary": "A broader moonshot atlas for mineral sands, sand batteries, local capability, reef ideas and first-principles imagination.",
    },
    {
        "title": "Civilisation of Sand",
        "site": "https://auraofintelligence.github.io/civilisation-of-sand/",
        "repo": "https://github.com/auraofintelligence/civilisation-of-sand",
        "summary": "The larger quest and simulation layer for capability, resource loops, game-world choices and public story scaffolding.",
    },
    {
        "title": "Quandamooka Film Festival",
        "site": "https://auraofintelligence.github.io/quandamooka-film-festival/",
        "repo": "https://github.com/auraofintelligence/quandamooka-film-festival",
        "summary": "A film planning doorway for story seeds, boundaries, storyboarding, festival pathways and consent-aware cultural memory.",
    },
    {
        "title": "Film Club Documentary Builders",
        "site": "https://auraofintelligence.github.io/film-club-documentary-builders/",
        "repo": "https://github.com/auraofintelligence/film-club-documentary-builders",
        "summary": "Markdown-first documentary builders for film profiles, source trails, research angles, scenes and handoffs.",
    },
]


SOURCE_DOCS = [
    {
        "title": "Straddie Sovereign Wealth Fund And Civilisation Of Sand Research Brief",
        "file": "Straddie_Sovereign_Wealth_Fund_&_Civilisation_of_Sand_Research_Brief.md",
        "use": "Adds clean energy options, sand batteries, artificial reefs, geopolymer blocks, erosion context and community wealth fund logic.",
    },
    {
        "title": "Dunwich / Gumpi Ferry Terminal Open Data Lab",
        "file": "dunwich-gumpi-ferry-terminal-open-data-lab repo",
        "use": "Provides the practical start: the $41M Junner Street ferry terminal upgrade consultation, official-source trail, public photos, data ladder and simulation workflow.",
    },
    {
        "title": "Wildlife Rescue Minjerribah Road-Hit Statistic",
        "file": "community-supplied 2025 statistic",
        "use": "Adds the transport-safety pressure: 250+ reported kangaroo and wallaby road hits in 2025, to be kept source-aware and open to verification.",
    },
    {
        "title": "P4A C-Hour And Civic Ledger Pattern",
        "file": "p4a_xyz LOCALISE_WITH_AN_AGENT.md and civic-ledger.html",
        "use": "Clarifies C-Hours as draft public-good receipts with consent, law, verification, anti-fraud checks and human governance.",
    },
    {
        "title": "Stradbroke Grants Lab",
        "file": "stradbroke-grants-lab repo",
        "use": "Adds the practical funding layer: grant watchlists, grant windows, applicant and project matching, readiness checklists, milestone reports and acquittal evidence.",
    },
    {
        "title": "How To Use Markdown With AI",
        "file": "how-to-use-md-with-ai repo",
        "use": "Adds the builder lesson pattern: purpose, context, boundaries, specific AI request, source links, review notes and privacy checks before sharing a `.md` file.",
    },
    {
        "title": "Strange But True Public Licence",
        "file": "strange-but-true LICENCE.md",
        "use": "Provides the local licence pattern: personal/generated outputs stay with the person, code can be studied and adapted, and story, brand, provenance and endorsement boundaries stay clear.",
    },
    {
        "title": "Mineral Moonshots",
        "file": "mineral-moonshots repo",
        "use": "Adds mineral-sands language, sand batteries, material transition anchors, reef ideas and local capability links.",
    },
    {
        "title": "Makerspace Evolution To Underground Citadel",
        "file": "Makerspace Evolution to Underground Citadel.docx",
        "use": "Gives the surface-to-subterranean pathway: workshop, tools, kiosks, sensors, silica stack and careful capability growth.",
    },
    {
        "title": "Subterranean Super Civilization Master Plan",
        "file": "Subterranean_Super_Civilization_Master_Plan.md",
        "use": "Supplies Sandworm, silica citadel, material sovereignty and high-risk speculative imagination that needs review gates.",
    },
    {
        "title": "Subterranean Eco-City Quandamooka Development",
        "file": "Subterranean_Eco-City_Quandamooka_Development.md",
        "use": "Adds eco-city framing, Indigenous data sovereignty questions, co-operative pathways and braided economy ideas.",
    },
    {
        "title": "Local Government Funding Inquiry Submission",
        "file": "Local_Government_Funding_Inquiry_Submission.md",
        "use": "Connects digital twins, civic ledgers, community wealth and regenerative local government questions.",
    },
    {
        "title": "GenesisAI, Sands, And Kardashev Civilization",
        "file": "GenesisAI,_Sands,_and_Kardashev_Civilization.md",
        "use": "Adds scientific AI, materials simulation, sand batteries and federated intelligence as concept inputs.",
    },
]


AI_PROMPT_STARTERS = [
    {
        "title": "Support letter",
        "text": "Using this Markdown as context, draft a respectful support letter in plain Australian English. Keep claims source-aware and list facts that still need checking.",
    },
    {
        "title": "Expression of interest",
        "text": "Using this Markdown as context, draft a short expression of interest from a community member, maker, funder, researcher or reviewer. Include possible next steps and boundaries.",
    },
    {
        "title": "Reasons to slow or stop",
        "text": "Using this Markdown as context, write a well-structured reasons-against note explaining which parts of the plan should not go ahead, should slow down, or need stronger evidence first.",
    },
    {
        "title": "Lesson or workshop direction",
        "text": "Using this Markdown as context, create a lesson direction, workshop outline or discussion guide that helps people explore the idea without being told what to think.",
    },
    {
        "title": "Evidence and risk check",
        "text": "Using this Markdown as context, list assumptions, missing sources, safety questions, cultural or ecological review needs, and the strongest counterarguments.",
    },
]


PUBLIC_REPO_URL = "https://github.com/auraofintelligence/sandworm-subterranean-systems"
MARKDOWN_AI_GUIDE = {
    "title": "How To Use Markdown With AI",
    "href": "https://auraofintelligence.github.io/how-to-use-md-with-ai/",
}
REPO_COPY_GUIDE = {
    "title": "Could your group build its own repo?",
    "text": "If a working site would help, copy or fork this public repo as a starting scaffold, name the new repo honestly, keep attribution and licence notes visible, then adapt the pages and builders for the visionary, engineering, community or review path you are exploring.",
    "href": PUBLIC_REPO_URL,
    "action": "Open repo",
}


BUILDERS = [
    {
        "id": "entry-trail",
        "title": "Entry Trail Builder",
        "purpose": "Choose a doorway into Sandworm without needing to accept the whole vision.",
        "filename": "sandworm-entry-trail",
        "boundary": "The trail is an invitation, not a test. People can stay, leave, disagree, or take only the part that helps.",
        "next_step": "Name one small practical action that would make the idea easier to understand.",
        "fields": [
            ("doorway", "Which doorway are you using?", "Start where attention is strongest. Existing pages can be reference points, but they are not the only doors."),
            ("question", "What question are you carrying?", "It can be a doubt, a curiosity, a concern, or a quiet 'what would need to be true?'"),
            ("useful_output", "What would be useful to leave with?", "Name the kind of thing that would help you think, share or test next. Rough is welcome."),
        ],
    },
    {
        "id": "maker-space-brief",
        "title": "Ferry Maker-Space Brief Builder",
        "purpose": "Turn the Dunwich / Gumpi start into a small buildable workshop or open-data brief.",
        "filename": "sandworm-ferry-makerspace-brief",
        "boundary": "A ferry-gateway maker-space brief should respect public safety, traffic flow, cultural authority, tool training, noise, waste handling and daily transport reality.",
        "next_step": "Choose one bench test, one public-source layer and one safety review before expanding.",
        "fields": [
            ("project", "What could be made, repaired, mapped or tested?", "What small practical thing would make this less abstract for you or your group?"),
            ("place", "Where does it touch the ferry gateway?", "Name the part of the gateway it touches, or say it is only a model for now."),
            ("tools", "What tools or spaces might be needed?", "What would make the idea easier to test, observe or explain without overbuilding it?"),
            ("review", "What needs review before anyone treats it as real?", "Who or what would you want checked before the idea leaves the draft table?"),
        ],
    },
    {
        "id": "digital-twin-brief",
        "title": "Digital Twin Brief Builder",
        "purpose": "Map a place or system while keeping people, culture and data sovereign.",
        "filename": "sandworm-digital-twin-brief",
        "boundary": "A digital twin should be a mirror and memory aid, not a control system or private-data trap.",
        "next_step": "Separate what is public-source, what needs permission, and what should stay private.",
        "fields": [
            ("place", "What place, object or system is being mapped?", "Use a public-safe name, a concept name, or keep it deliberately general."),
            ("layers", "What layers belong in the twin?", "Which layers would help people see the question more clearly, and which should stay out?"),
            ("permissions", "Who has authority over the sensitive parts?", "Who might need to be asked, credited, protected, or left out for now?"),
            ("public_benefit", "What public benefit could the twin create?", "What could become easier to understand, maintain, protect, repair or question?"),
        ],
    },
    {
        "id": "sandworm-experiment",
        "title": "Sandworm Experiment Builder",
        "purpose": "Turn a subterranean systems idea into a cautious prototype question.",
        "filename": "sandworm-experiment-card",
        "boundary": "Speculative engineering belongs behind review gates. Do not treat a concept card as permission to dig, test, mine or build.",
        "next_step": "Find the smallest harmless test that improves understanding without risking people, place or trust.",
        "fields": [
            ("idea", "What is the experiment idea?", "Describe the possibility in your own words, even if it is messy or incomplete."),
            ("small_test", "What is the smallest safe test?", "What is the least invasive way to learn something useful?"),
            ("unknowns", "What is unknown or risky?", "Which unknowns would make you pause, ask for help, or change direction?"),
            ("stop_rule", "When should the idea stop or slow down?", "What sign would tell you this idea needs to slow down, shrink or stop?"),
        ],
    },
    {
        "id": "spoil-loop-brief",
        "title": "Spoil Loop Brief Builder",
        "purpose": "Track how sand spoil could become blocks, reef modules, dune support, tunnel lining or stored heat.",
        "filename": "sandworm-spoil-loop-brief",
        "boundary": "Spoil reuse needs material testing, contamination checks, ecology review, engineering review and a clear no-dumping rule.",
        "next_step": "Pick one material stream and one reviewer before proposing a public prototype.",
        "fields": [
            ("spoil_source", "Where would the sand or spoil come from?", "If material ever appears, where might it come from? If that is unknown, say so."),
            ("use_path", "What might it become?", "What possible second life is worth testing, not assuming?"),
            ("problem", "Which existing problem does this help?", "Which existing pressure would need to improve before this path earns attention?"),
            ("review", "What has to be checked?", "What checks would you want before material is moved, used, named or celebrated?"),
        ],
    },
    {
        "id": "reef-energy-brief",
        "title": "Reef, Bank And Quiet Power Builder",
        "purpose": "Draft a reef or power idea that starts with ecology, surf, safety and reversibility.",
        "filename": "sandworm-reef-energy-brief",
        "boundary": "This trail avoids bladed and noisy machinery. Any energy idea needs marine noise, animal safety, wave, sediment and cultural review before it becomes more than a sketch.",
        "next_step": "Name the habitat question, the energy question and the stop rule.",
        "fields": [
            ("site", "Which edge are you imagining?", "Name the edge you are thinking with, or keep it conceptual while the evidence catches up."),
            ("structure", "What structure is being explored?", "What shape, habitat or quiet-power idea is only being sketched for now?"),
            ("benefit", "What benefits should be tested together?", "Which benefits might sit in tension, and which would need proof?"),
            ("avoid", "What should the design avoid?", "What harms, disturbances or irreversible moves would make the idea unacceptable?"),
        ],
    },
    {
        "id": "wealth-stewardship-brief",
        "title": "Wealth And C-Hour Stewardship Builder",
        "purpose": "Connect a Sandworm asset idea to transparent stewardship, receipts and local benefit.",
        "filename": "sandworm-wealth-stewardship-brief",
        "boundary": "A C-Hour or fund note is not a launched financial product. It needs law, consent, anti-fraud checks, local legitimacy and human governance before real use.",
        "next_step": "Separate money revenue, public-good hours, receipts, trusteeship and public dashboards.",
        "fields": [
            ("asset", "What asset or value stream is being imagined?", "What value might be created, and what would make that value public-good rather than hype?"),
            ("holders", "Who might steward it?", "Who could be trusted to steward it, or whose absence makes that unclear?"),
            ("receipt", "What should be visible?", "What would people need to see to trust the claim without being surveilled?"),
            ("limits", "What should not become a score or product?", "What should stay outside measurement, money, scoring or pressure?"),
        ],
    },
    {
        "id": "film-documentary-trail",
        "title": "Film And Documentary Trail Builder",
        "purpose": "Carry a Sandworm idea into fiction, documentary or festival planning without taking over the story.",
        "filename": "sandworm-film-documentary-trail",
        "boundary": "The story stays with the people who carry it. AI and templates can help structure notes, but they do not own meaning.",
        "next_step": "Choose whether the next output is a story seed, source trail, interview map, storyboard or permissions list.",
        "fields": [
            ("story_seed", "What story seed is present?", "What feels worth following, questioning or protecting as a story?"),
            ("holders", "Who might hold the story or need a say?", "Who might need to shape, refuse, correct or withhold the story?"),
            ("assets", "What assets or evidence might help?", "What evidence or creative material could help, and what should not be collected?"),
            ("care", "What care should shape the story?", "What care would keep the story from taking more than it gives?"),
        ],
    },
    {
        "id": "source-trail",
        "title": "Source Trail Builder",
        "purpose": "Separate concept fuel, public evidence, open questions and claims that need checking.",
        "filename": "sandworm-source-trail",
        "boundary": "A source trail is not a truth badge. It helps people see what is known, what is imagined and what needs checking.",
        "next_step": "Move one strong claim into a checkable question with a date, source type and reviewer.",
        "fields": [
            ("claim", "What claim or idea is being tracked?", "Write the claim as something that can still be corrected."),
            ("source", "Where did it come from?", "Where did the idea enter the trail, and how close is that to public evidence?"),
            ("confidence", "How confident should a public reader be?", "How should a reader hold it for now: loose, promising, contested, sourced or private?"),
            ("reviewer", "Who or what should review it?", "Whose review would make the next public sentence more honest?"),
        ],
    },
    {
        "id": "boundary-check",
        "title": "Boundary Check Builder",
        "purpose": "Name consent, privacy, cultural, ecological, legal and safety limits before a trail grows.",
        "filename": "sandworm-boundary-check",
        "boundary": "Boundaries are not obstacles to the work. They are how the work keeps trust.",
        "next_step": "Pick one boundary that needs a real conversation before publication or prototyping.",
        "fields": [
            ("context", "What trail or idea is being checked?", "Name the trail, place, source or moment where a boundary is needed."),
            ("boundaries", "Which boundaries matter here?", "Which limits would protect people, place, culture, ecology or trust?"),
            ("missing_voice", "Whose voice or authority is missing?", "Who is not in the room, and what should wait until they are?"),
            ("safe_public_version", "What is the safe public version for now?", "What can be said safely now, and what should stay draft or private?"),
        ],
    },
]


def e(value: str) -> str:
    return escape(value, quote=True)


def by_id(page_id: str) -> dict[str, str]:
    for page in PAGES:
        if page["id"] == page_id:
            return page
    raise KeyError(page_id)


def hero_image(page_id: str) -> str:
    if page_id.startswith("builder-"):
        return HERO_IMAGES["builders"]
    return HERO_IMAGES.get(page_id, HERO_IMAGES["home"])


def card_grid(cards: list[dict[str, str]], class_name: str = "card-grid") -> str:
    items = []
    for card in cards:
        href = card.get("href")
        tag = "a" if href else "article"
        href_attr = f' href="{e(href)}"' if href else ""
        items.append(
            f'<{tag} class="card"{href_attr}>'
            f'<p class="mini-label">{e(card.get("label", ""))}</p>'
            f'<h3>{e(card["title"])}</h3>'
            f'<p>{e(card["text"])}</p>'
            + (f'<span class="text-link">{e(card.get("action", "Open"))}</span>' if href else "")
            + f'</{tag}>'
        )
    return f'<div class="{class_name}">{"".join(items)}</div>'


def ai_prompt_cards() -> list[dict[str, str]]:
    cards = [
        {"label": "AI prompt", "title": starter["title"], "text": starter["text"]}
        for starter in AI_PROMPT_STARTERS
    ]
    cards.append({"label": "Public repo", **REPO_COPY_GUIDE})
    return cards


def ai_handoff_section() -> str:
    return """
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Use the draft</p>
      <h2>What could this `.md` help an explorer ask next?</h2>
      <p class="lede">A builder output can be copied, downloaded, inspected and then taken to any AI tool. It can support a letter, an expression of interest, a workshop direction, or a strong reasons-against note.</p>
    </div>
""" + card_grid(ai_prompt_cards()) + f"""
    <div class="callout">
      <div><h3>Want the plain guide?</h3><p>Open the Markdown-with-AI guide for a simple pattern: purpose, context, boundaries, request, sources and review.</p></div>
      <a class="button primary" href="{e(MARKDOWN_AI_GUIDE["href"])}">Open guide</a>
    </div>
  </div>
</section>
"""


def repo_grid() -> str:
    cards = []
    for link in COMPANION_LINKS:
        cards.append(
            '<article class="repo-card">'
            f'<p class="mini-label">Source bridge</p><h3>{e(link["title"])}</h3>'
            f'<p>{e(link["summary"])}</p>'
            f'<p><a class="text-link" href="{e(link["site"])}">Live site</a> '
            f'<a class="text-link" href="{e(link["repo"])}">Source repo</a></p>'
            '</article>'
        )
    return f'<div class="repo-grid">{"".join(cards)}</div>'


def question_list(questions: list[str]) -> str:
    return '<ul class="question-list">' + ''.join(f'<li>{e(q)}</li>' for q in questions) + '</ul>'


def pathway(items: list[tuple[str, str]]) -> str:
    return '<ol class="pathway">' + ''.join(
        f'<li><div><h3>{e(title)}</h3><p>{e(text)}</p></div></li>' for title, text in items
    ) + '</ol>'


def page_hero(page: dict[str, str]) -> str:
    return (
        '<section class="page-hero"><div class="page-hero-inner">'
        f'<h1>{e(page["title"])}</h1>'
        f'<p class="lede">{e(page["description"])}</p>'
        '</div></section>'
    )


def home_body() -> str:
    return """
<section class="hero">
  <div class="hero-body">
    <div class="hero-copy">
      <p class="section-label hero-label">Exploratory public workbench</p>
      <h1>Sandworm Subterranean Systems</h1>
      <p class="hero-lede">Could careful digging help solve existing problems above ground: wildlife road hits, road damage from heavy buses, trucks and rain, disconnected towns, after-hours transport gaps, multi-decade parking pressure, erosion, energy storage and patient community assets, while treating any tunnel spoil it creates as a resource?</p>
      <div class="hero-actions">
        <a class="button primary" href="start.html">Follow the reasons</a>
        <a class="button secondary" href="builders/index.html">Open builders</a>
      </div>
      <p class="micro-note">First draft. Questions before claims. People keep the steering wheel.</p>
    </div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">The Sandworm spine</p>
      <h2>If Sandworm creates spoil, what could that material become?</h2>
      <p class="lede">A tunnel project eventually asks where the spoil goes. Sandworm asks which local problems that material might help with if each step stays tested, reviewed and open to correction.</p>
    </div>
""" + card_grid([
        {"label": "Question", "title": "Could major transport arteries move below the fragile roads?", "text": "What if autonomous on-call vehicles ran 24/7/365 between towns, ferry gateways, park-and-ride nodes and service points, reducing pressure on surface roads and wildlife?"},
        {"label": "Question", "title": "What is erosion already asking?", "text": "If tunnelling creates spoil, could tested reef modules, dune support, oyster-crete or seagrass lattices help coastal care?"},
        {"label": "Question", "title": "What does the transport data already say?", "text": "How do ferry arrivals, tourist buses, trucks, rain damage, road repairs, parking shortages, town separation and after-hours gaps change the argument?"},
        {"label": "Question", "title": "Could local material become blocks?", "text": "Which sand, binders, shells, glass or waste streams might become blocks only after material testing and lifecycle review?"},
        {"label": "Question", "title": "Could quiet power store as heat?", "text": "Which reef-anchor or wave-pressure ideas might feed sand batteries without ignoring marine life, noise or reversibility?"},
        {"label": "Question", "title": "How could assets stay local?", "text": "Could energy, materials and learning support a patient wealth fund while C-Hours recognise verified public-good work?"},
    ]) + """
  </div>
</section>
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Where to begin</p>
      <h2>Could the live ferry upgrade become the first reality check?</h2>
      <p class="lede">The $41M Dunwich / Gumpi Ferry Terminal Upgrade concept-design consultation runs from 28 May to 21 June 2026, with a business case due in late 2026. What could a maker-space and data lab help people inspect: ferry flows, bus access, kiss-and-ride, pedestrian links, long-running parking pressure, foreshore repair, public photos, open-data files, park-and-ride questions and future autonomous corridor questions?</p>
    </div>
    <div class="quote-panel">What can we map, test, repair, make or film now that would still be useful even if the largest Sandworm never gets built?</div>
  </div>
</section>
<section class="section deep-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Story with a job</p>
      <h2>The fiction and documentary are part of the test.</h2>
      <p class="lede">If people back the plan, could the film trail show the reasons, doubts, evidence, modelling, culture questions and first maker-space experiments without herding anyone into belief?</p>
    </div>
""" + card_grid([
        {"label": "Explorer", "title": "What question is alive here?", "text": "The site can be read as a trail of questions, not a finished authority."},
        {"label": "Maker", "title": "What is the smallest useful prototype?", "text": "Could the big idea shrink into a bench test, map layer, material sample or public note?"},
        {"label": "Steward", "title": "Which limits need daylight?", "text": "What ecological, cultural, legal or safety boundaries could be visible before the work gets louder?"},
    ]) + """
  </div>
</section>
"""


def start_body() -> str:
    return page_hero(by_id("start")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Reasons before scale</p>
      <h2>What would careful digging need to help before it earned trust?</h2>
      <p class="lede">Sandworm becomes worth exploring only if each layer solves something people already care about.</p>
    </div>
""" + pathway([
        ("Could Gumpi model the first autonomous loop?", "The ferry gateway may be a useful maker-space and open-data start because the transport system is already visible there."),
        ("What are wildlife road hits telling us?", "If local rescue statistics are showing 250+ kangaroo and wallaby road hits in 2025, what transport redesign questions deserve daylight?"),
        ("What is heavy traffic doing to the roads?", "How do tourist buses, trucks, rain damage and constant repairs change the case for moving major arteries off the fragile surface?"),
        ("Where do cars wait when the island is full?", "If parking has been tight for decades, could mainland shopper days, holiday peaks and resident access be modelled with park-and-ride nodes, autonomous shuttles or a tunnel-linked parking loop?"),
        ("Who is stranded when public transport sleeps?", "What happens to disconnected towns, older residents and workers when public transport is thin before 6am and after 8pm?"),
        ("If spoil appears, where could it go?", "What source, test, destination, risk check and possible second life would make a material stream trustworthy?"),
        ("How could the story stay honest?", "Could film and documentary invite support while still showing doubts, unknowns and reviewer voices?"),
    ]) + """
    <div class="callout">
      <div><h3>Leave with a Markdown handoff.</h3><p>A clean `.md` draft is a small bridge between high-level thought and practical next work.</p></div>
      <a class="button primary" href="builders/entry-trail.html">Start an entry trail</a>
    </div>
  </div>
</section>
"""


def makerspace_body() -> str:
    return page_hero(by_id("makerspace")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Grounded start</p>
      <h2>What can a modern ferry gateway teach before anyone talks about tunnels?</h2>
      <p class="lede">Dunwich / Gumpi is already a living transport system: vehicle ferries, passenger services, buses, turnarounds, freight, visitors, parking pressure and daily local movement. With the $41M Junner Street ferry terminal upgrade in consultation from 28 May to 21 June 2026, could this become the first place to compare official concept design, local evidence, open-data asks, maker-space tools, park-and-ride options and future autonomous corridor questions?</p>
    </div>
    <div class="quote-panel">A good first lab helps people understand the place before it asks them to believe a plan.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">First bench</p><h2>What could the maker-space actually do?</h2></div>
""" + card_grid([
        {"label": "Question", "title": "What is the $41M upgrade changing?", "text": "How do the official concept design, business case, terminal building, dual-berth pontoon, bus stops, kiss-and-ride, parking and foreshore plans change the first maker-space brief?"},
        {"label": "Question", "title": "What evidence is already public?", "text": "Which TMR pages, Your Say consultation material, Gumpi Master Plan notes, public photos, 3D scans or plain observations help people see the gateway clearly?"},
        {"label": "Question", "title": "What samples are safe to test?", "text": "Which sand, shells, recycled glass, binders or block forms might be explored at bench scale before claims harden?"},
        {"label": "Question", "title": "How does movement really work?", "text": "What do vehicle ferries, passenger ferries, buses, parking overflow, freight, school runs, emergency paths, workers, visitors and possible autonomous tunnel links look like together?"},
        {"label": "Question", "title": "Could parking move to a smarter edge?", "text": "Where could holiday makers, residents doing mainland shopper days and service vehicles shift into park-and-ride or tunnel-linked shuttle loops without making daily life harder?"},
        {"label": "Question", "title": "Who wants tool confidence?", "text": "How might locals, students, makers and documentarians learn scanning, forms, safety and public-source work at their own pace while consultation is still live?"},
        {"label": "Question", "title": "What would be useful to film first?", "text": "Which official source trails, transport gaps, local observations, doubts and first bench tests would help people inspect the thinking?"},
        {"label": "Question", "title": "Whose permission matters?", "text": "Which public infrastructure, cultural authority, engineering and safety questions need review before momentum?"},
    ]) + """
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Starting node</p><h2>Could the ferry lab be the practical front door?</h2></div>
""" + card_grid([
        {"label": "Public site", "title": "Dunwich / Gumpi Ferry Terminal Open Data Lab", "text": "Open the existing $41M consultation trail, evidence map, data ladder and simulation workflow.", "href": "https://auraofintelligence.github.io/dunwich-gumpi-ferry-terminal-open-data-lab/", "action": "Visit site"},
        {"label": "Builder", "title": "Ferry Maker-Space Brief", "text": "Could one ferry-gateway idea become a small Markdown brief?", "href": "builders/maker-space-brief.html", "action": "Open builder"},
        {"label": "Boundary", "title": "Safety before momentum", "text": "Which public space, tool, road, material or claim needs a boundary check?", "href": "builders/boundary-check.html", "action": "Open check"},
    ]) + """
  </div>
</section>
"""


def digital_twin_body() -> str:
    return page_hero(by_id("digital-twin")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Mirror, not master</p>
      <h2>The twin helps people see patterns before anyone argues about construction.</h2>
      <p class="lede">A useful Sandworm twin separates public-source layers, permissioned layers and private layers. It can map modern ferry flows, road corridors, parking pressure, park-and-ride options, animal crossings, erosion edges, reef ideas, material routes and emergency movement without turning people into data.</p>
    </div>
""" + pathway([
        ("L0 private or bench", "A workshop sample, room, tool, material test or private note. The holder keeps control."),
        ("L1 shared gateway", "The ferry terminal, bus turnaround, parking edge, road corridor, maker-space or public asset. Permissions and context matter."),
        ("L2 bioregion", "The bay, surf side, dunes, roads, reefs and island systems. Public sources and cultural authority matter more."),
    ]) + """
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Questions to carry</p><h2>What is enough to learn, and what is too much to capture?</h2></div>
""" + question_list([
        "Which layers are official public sources, and which are community observations?",
        "Which map layers need permission, context or cultural review?",
        "Which details should not be collected at all?",
        "Where might an autonomous corridor, tunnel or service path reduce harm instead of adding it?",
        "What correction path lets people improve the map later?",
    ]) + """
    <div class="callout">
      <div><h3>Could a twin brief help?</h3><p>One place, one possible public benefit and one permission boundary may be enough to begin.</p></div>
      <a class="button primary" href="builders/digital-twin-brief.html">Open builder</a>
    </div>
  </div>
</section>
"""


def sandworm_lab_body() -> str:
    return page_hero(by_id("sandworm-lab")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Material loop</p>
      <h2>The spoil ledger is the discipline.</h2>
      <p class="lede">If Sandworm ever digs, what would let people ask where the sand came from, how it was tested, what it became, who reviewed it, what risk remains and who benefits?</p>
    </div>
    <div class="quote-panel">Spoil becomes useful only when it has a passport, a review path and a reason to exist.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Possible destinations</p><h2>Which destination might answer which need?</h2></div>
""" + card_grid([
        {"label": "Question", "title": "Could blocks be tested first?", "text": "Which blocks, pavers or panels from sand, shells, glass, binders or waste streams would deserve a bench test before a claim?"},
        {"label": "Question", "title": "Could reef modules help habitat?", "text": "Which oyster-crete, rough texture, hole pattern, seagrass lattice or habitat-first design needs ecology review?"},
        {"label": "Question", "title": "Could erosion control be gentler?", "text": "Which forms, lattices or reef geometry might reduce wave impact only where coastal science supports it?"},
        {"label": "Question", "title": "What would tunnel models reveal?", "text": "Which small models for lining, water, access, sensors or maintenance would be useful before physical ambition?"},
        {"label": "Question", "title": "Could sand batteries fit here?", "text": "Could excess clean power heat insulated sand mass for storage, process heat or future local industry questions?"},
        {"label": "Question", "title": "What would a material passport show?", "text": "Which source, test, reviewer, destination, reuse, risk and public benefit fields would make the material legible?"},
    ]) + """
    <div class="callout">
      <div><h3>Track one material stream.</h3><p>The builder turns a spoil idea into a reviewable Markdown note.</p></div>
      <a class="button primary" href="builders/spoil-loop-brief.html">Open spoil builder</a>
    </div>
  </div>
</section>
"""


def civilisation_body() -> str:
    return page_hero(by_id("civilisation")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Ecology first</p>
      <h2>Could power ideas make the bay and surf edge safer to live with?</h2>
      <p class="lede">What happens if the trail begins with reef geometry, quiet anchors, wave-pressure structures, oscillating-water-column style questions, dune stabilisation, habitat and sand-battery storage, while leaving bladed and noisy machinery outside the frame?</p>
    </div>
""" + card_grid([
        {"label": "Question", "title": "Could reef anchors stay alive?", "text": "How might artificial reefs act as habitat, coastal protection and quiet structural anchors rather than industrial clutter?"},
        {"label": "Question", "title": "Could surf-side banks be studied gently?", "text": "Which wave-shape, dune-stability, safety, ecology and public-joy questions belong before any claim?"},
        {"label": "Question", "title": "Could wave pressure stay quiet?", "text": "Which enclosed, low-harm pressure systems or removable pilots would deserve animal-safety review?"},
        {"label": "Question", "title": "Could power become stored heat?", "text": "What local value appears if intermittent power has a patient sand-battery sink?"},
        {"label": "Question", "title": "What does marine life require?", "text": "How do noise, whales, dolphins, turtles, dugongs, fishers, currents, sediment and navigation shape the design?"},
        {"label": "Question", "title": "What should be simulated first?", "text": "Could digital twins and tabletop models carry the first arguments instead of heavy machinery?"},
    ]) + """
    <div class="callout">
      <div><h3>Could a reef or quiet-power brief help?</h3><p>The habitat question and stop rule can stay visible from the first draft.</p></div>
      <a class="button primary" href="builders/reef-energy-brief.html">Open reef builder</a>
    </div>
  </div>
</section>
"""


def wealth_body() -> str:
    return page_hero(by_id("wealth")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Assets with receipts</p>
      <h2>Could the wealth fund and C-Hours answer different parts of the same question?</h2>
      <p class="lede">A sovereign wealth fund might steward revenue, assets and long-horizon reinvestment. C-Hours, from the P4A grassroots civic system, might recognise verified public-good contribution without pretending care work is a speculative token.</p>
    </div>
    <div class="quote-panel">Money, hours and trust all need receipts. Receipts need law, consent, anti-fraud checks and human governance.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Braided stewardship</p><h2>How could normal money and public-good hours stay legible?</h2></div>
""" + card_grid([
        {"label": "Question", "title": "What might patient capital hold?", "text": "Could energy, manufacturing, training, licences or infrastructure income be reinvested in community assets over time?"},
        {"label": "Question", "title": "What counts as public-good work?", "text": "Which care, repair, mentoring, ecological work, disaster response or civic service could be visible only with consent?"},
        {"label": "Question", "title": "What receipts would people trust?", "text": "How might money, hours, claims, conflicts, corrections and review status stay inspectable without becoming surveillance?"},
        {"label": "Question", "title": "Who reviews the reviewers?", "text": "What local legitimacy, law, privacy, anti-fraud checks and right-to-refuse rules would make stewardship credible?"},
        {"label": "Question", "title": "Where does sovereignty say no?", "text": "Which private life, culture or care details should never become rankings or public exposure?"},
        {"label": "Question", "title": "Could documentary show the trust work?", "text": "How could contribution, ownership and benefit be argued, tested and corrected on camera?"},
        {"label": "Source bridge", "title": "Where does Stradbroke Grants Lab fit?", "text": "Could grant windows, applicant profiles, readiness checks, milestone reports and acquittal notes support small public trials before asset revenue exists?", "href": "https://auraofintelligence.github.io/stradbroke-grants-lab/", "action": "Open Grants Lab"},
    ]) + """
    <div class="callout">
      <div><h3>Draft a stewardship note.</h3><p>Separate revenue, contribution, receipts, trusteeship and public limits.</p></div>
      <a class="button primary" href="builders/wealth-stewardship-brief.html">Open stewardship builder</a>
    </div>
  </div>
</section>
"""


def culture_body() -> str:
    return page_hero(by_id("culture")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Story as inspection</p>
      <h2>Could fiction carry possibility while documentary carries the receipts?</h2>
      <p class="lede">Sandworm is not only an engineering idea. It is a way to ask whether difficult infrastructure could become story, learning, review, consent, wealth and ecological repair without taking anyone's authority away.</p>
    </div>
    <div class="quote-panel">A good story trail does not take the story. It makes the next respectful conversation easier.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
""" + card_grid([
        {"label": "Question", "title": "What would a future story reveal?", "text": "Could autonomous corridors, reefs, fewer road hits, sand batteries and public ledgers appear as lived choices rather than slogans?"},
        {"label": "Question", "title": "What should the camera follow?", "text": "Which source trails, makers, sceptics, reviewers, failed tests and careful improvements would make the first attempts honest?"},
        {"label": "Question", "title": "How do people enter freely?", "text": "Could screenings, builder forms and discussion trails let people explore without being told what to think?"},
        {"label": "Builder", "title": "Film And Documentary Trail", "text": "Could one Sandworm idea become a story-planning note without taking over meaning?", "href": "builders/film-documentary-trail.html", "action": "Open builder"},
        {"label": "Bridge", "title": "Quandamooka Film Festival", "text": "A related film planning doorway for story seeds, storyboarding and readiness.", "href": "https://auraofintelligence.github.io/quandamooka-film-festival/", "action": "Visit site"},
        {"label": "Bridge", "title": "Film Club Documentary Builders", "text": "Markdown-first builders for source trails, research angles and handoffs.", "href": "https://auraofintelligence.github.io/film-club-documentary-builders/", "action": "Visit site"},
    ]) + """
  </div>
</section>
"""


def boundaries_body() -> str:
    return page_hero(by_id("boundaries")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Human guardrails</p><h2>Which boundaries would make the exploration stronger?</h2><p class="lede">Could clear boundaries help the work avoid extraction, false authority, private-data capture, unsafe engineering or ecological arrogance?</p></div>
""" + card_grid([
        {"label": "Question", "title": "Who can carry this story?", "text": "Which stories, images, place memories or cultural details are powerful without being public property?"},
        {"label": "Question", "title": "Which layers stay private?", "text": "How can a digital twin clarify public systems without exposing household, health, identity or vulnerable-person details?"},
        {"label": "Question", "title": "Who holds authority here?", "text": "Where would public pages risk implying endorsement, approval or representation that has not been granted?"},
        {"label": "Question", "title": "What does marine life need?", "text": "How do noise, animal-risk machinery, sediment, navigation, fishers, whales, dolphins, turtles and dugongs shape the boundary?"},
        {"label": "Question", "title": "What needs review first?", "text": "Which material, tunnel, energy, sensor or machine ideas need review before they become physical activity?"},
        {"label": "Question", "title": "How does participation stay voluntary?", "text": "How can people use, reject, correct or ignore the tools without losing dignity?"},
    ]) + """
    <div class="callout">
      <div><h3>Would a quick review note help?</h3><p>A boundary can be named before the project gets louder.</p></div>
      <a class="button primary" href="builders/boundary-check.html">Open boundary check</a>
    </div>
  </div>
</section>
"""


def sources_body() -> str:
    cards = []
    for source in SOURCE_DOCS:
        cards.append(
            '<article class="source-card">'
            f'<p class="mini-label">Source input</p><h3>{e(source["title"])}</h3>'
            f'<p><code>{e(source["file"])}</code></p><p>{e(source["use"])}</p>'
            '</article>'
        )
    return page_hero(by_id("sources")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Source posture</p>
      <h2>The documents and repos are fuel for inquiry, not automatic public proof.</h2>
      <p class="lede">This first draft keeps the source trail visible while separating concept fuel, public evidence, permissioned knowledge and claims that need checking.</p>
    </div>
    <div class="source-grid">
""" + "".join(cards) + """
    </div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Connected workbenches</p><h2>Bridge repos that informed the draft.</h2><p class="lede">These are connected tools and source worlds. They are not the point of Sandworm, but they help explain where a trail can continue.</p></div>
""" + repo_grid() + """
  </div>
</section>
"""


def builders_index_body() -> str:
    cards = []
    for builder in BUILDERS:
        cards.append(
            f'<a href="{e(builder["id"])}.html">'
            f'<p class="mini-label">Markdown builder</p><strong>{e(builder["title"])}</strong>'
            f'<p>{e(builder["purpose"])}</p>'
            f'<span class="text-link">Open form</span></a>'
        )
    return page_hero(by_id("builders")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Browser-only forms</p>
      <h2>Each builder makes a clean `.md` draft.</h2>
      <p class="lede">The forms save only in this browser while you type. You can copy or download the Markdown when it is useful.</p>
    </div>
    <div class="builder-index">
""" + "".join(cards) + """
    </div>
  </div>
</section>
""" + ai_handoff_section()


def builder_body(builder: dict) -> str:
    field_html = []
    for name, label, hint in builder["fields"]:
        field_html.append(
            '<div class="field">'
            f'<label for="{e(name)}">{e(label)}</label>'
            f'<span>{e(hint)}</span>'
            f'<textarea id="{e(name)}" name="{e(name)}"></textarea>'
            '</div>'
        )

    definition = {
        "id": builder["id"],
        "title": builder["title"],
        "purpose": builder["purpose"],
        "filename": builder["filename"],
        "boundary": builder["boundary"],
        "next_step": builder["next_step"],
        "ai_prompt_starters": AI_PROMPT_STARTERS,
        "markdown_ai_guide": MARKDOWN_AI_GUIDE,
        "repo_copy": REPO_COPY_GUIDE,
        "fields": [
            {"name": name, "label": label, "hint": hint}
            for name, label, hint in builder["fields"]
        ],
    }
    page = {"title": builder["title"], "description": builder["purpose"]}
    definition_json = json.dumps(definition).replace("</", "<\\/")

    return page_hero(page) + f"""
<section class="section">
  <div class="section-inner builder-layout">
    <div class="builder-panel">
      <p class="section-label">Draft form</p>
      <p class="muted">The hints are optional thought-starters, not directions or approved answers. Bring your own framing, doubt, refusal or path.</p>
      <form class="builder-form" data-builder-form>
        {''.join(field_html)}
      </form>
      <div class="button-row">
        <button class="button primary" type="button" data-copy-markdown>Copy Markdown</button>
        <button class="button ghost" type="button" data-download-markdown>Download `.md`</button>
        <button class="button ghost" type="button" data-clear-form>Clear</button>
      </div>
      <p class="status-line" data-builder-status></p>
    </div>
    <div class="builder-panel">
      <p class="section-label">Markdown preview</p>
      <textarea class="markdown-output" data-markdown-output readonly></textarea>
    </div>
  </div>
</section>
<script id="builder-definition" type="application/json">{definition_json}</script>
<script src="../assets/js/form-builder.js"></script>
""" + ai_handoff_section()


def licence_body() -> str:
    return page_hero(by_id("licence")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Public infrastructure</p>
      <h2>What reuse helps the work stay useful and honest?</h2>
      <p class="lede">Sandworm is shared as a public-interest workbench. People can read it, question it, use the builders, make their own Markdown notes, and fork or copy the repo as a scaffold for their own repo while keeping the source trail visible.</p>
    </div>
""" + card_grid([
        {"label": "Builder output", "title": "Who owns a generated `.md`?", "text": "The person who writes the answers controls their downloaded Markdown. The site does not need to host it, approve it or claim it."},
        {"label": "Code", "title": "Could the public repo be copied?", "text": "Yes, for public-interest, educational, community, artistic, regenerative or review purposes, if attribution, licence notes and honest provenance stay visible."},
        {"label": "Own repo", "title": "What makes a fork honest?", "text": "A new repo should name itself clearly, avoid implying endorsement, keep links back to the original, and show what has changed."},
        {"label": "Story material", "title": "What stays protected?", "text": "The Sandworm name, writings, images, narrative materials, brand assets and public story world are not offered as raw material to sell, mislabel or repackage."},
        {"label": "AI use", "title": "Can AI tools use the Markdown?", "text": "Yes, as context for drafts, letters, critique, lessons or expressions of interest, while keeping facts, sources, privacy, cultural authority and review status visible."},
        {"label": "Reality check", "title": "What is not granted?", "text": "No page, builder, fork or AI output is engineering approval, legal advice, cultural permission, environmental approval, financial advice or official endorsement."},
    ]) + """
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner split">
    <div>
      <p class="section-label">Plain path</p>
      <h2>Could someone build their own repo without muddying the source?</h2>
      <p class="lede">A respectful fork can be simple: copy the public repo, keep the original licence and source links, name the new repo for the visionary, engineering, group or review path, change the pages and builders, then add notes showing what is draft, sourced, reviewed or still uncertain.</p>
    </div>
    <div class="quote-panel">Good reuse leaves a trail. People can see what came from Sandworm, what changed, and who now carries the local responsibility.</div>
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="callout">
      <div><h3>Read the full local licence.</h3><p>The repo-level `LICENCE.md` sets the practical boundaries for builders, code, AI drafts, public forks, creative works and liability.</p></div>
      <a class="button primary" href="LICENCE.md">Open LICENCE.md</a>
    </div>
  </div>
</section>
"""


def site_map_body() -> str:
    page_links = ''.join(
        f'<a class="card" href="{e(page["href"])}"><p class="mini-label">Page</p><h3>{e(page["title"])}</h3><p>{e(page["description"])}</p></a>'
        for page in PAGES
    )
    builder_links = ''.join(
        f'<a class="card" href="builders/{e(builder["id"])}.html"><p class="mini-label">Builder page</p><h3>{e(builder["title"])}</h3><p>{e(builder["purpose"])}</p></a>'
        for builder in BUILDERS
    )
    template_links = ''.join(
        f'<a class="card" href="builders/{e(builder["id"])}.md"><p class="mini-label">Markdown template</p><h3>{e(builder["title"])}</h3><p>{e(builder["filename"])}.md</p></a>'
        for builder in BUILDERS
    )
    return page_hero(by_id("site-map")) + f"""
<section class="section">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Public pages</p><h2>Site pages</h2></div>
    <div class="card-grid">{page_links}</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Builder pages</p><h2>Forms</h2></div>
    <div class="card-grid">{builder_links}</div>
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Markdown templates</p><h2>Downloadable source templates</h2></div>
    <div class="card-grid">{template_links}</div>
  </div>
</section>
<section class="section deep-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Source bridges</p><h2>Connected workbenches</h2></div>
    {repo_grid()}
  </div>
</section>
"""


BODY_RENDERERS = {
    "home": home_body,
    "start": start_body,
    "makerspace": makerspace_body,
    "digital-twin": digital_twin_body,
    "sandworm-lab": sandworm_lab_body,
    "civilisation": civilisation_body,
    "wealth": wealth_body,
    "culture": culture_body,
    "builders": builders_index_body,
    "boundaries": boundaries_body,
    "sources": sources_body,
    "licence": licence_body,
    "site-map": site_map_body,
}


def render_shell(page_id: str, title: str, description: str, body: str, path: str) -> str:
    base = "../" if "/" in path else ""
    canonical = BASE_URL + path
    css = base + f"assets/css/styles.css?v={ASSET_VERSION}"
    favicon = base + "assets/img/favicon.svg"
    site_data = base + f"assets/js/site-data.js?v={ASSET_VERSION}"
    site_nav = base + f"assets/js/site-nav.js?v={ASSET_VERSION}"
    image_path = hero_image(page_id)
    preload_image = base + f"{image_path}?v={ASSET_VERSION}"
    image = BASE_URL + image_path
    css_image = "../" + image_path.removeprefix("assets/") + f"?v={ASSET_VERSION}"
    body_markup = body.strip()
    return f"""<!doctype html>
<html lang="en-AU">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{e(description)}">
  <meta name="theme-color" content="#06242d">
  <meta property="og:title" content="{e(title)} | {SITE_TITLE}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{e(canonical)}">
  <meta property="og:image" content="{e(image)}">
  <meta property="og:site_name" content="{SITE_TITLE}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(title)} | {SITE_TITLE}">
  <meta name="twitter:description" content="{e(description)}">
  <meta name="twitter:image" content="{e(image)}">
  <title>{e(title)} | {SITE_TITLE}</title>
  <link rel="canonical" href="{e(canonical)}">
  <link rel="icon" href="{favicon}" type="image/svg+xml">
  <link rel="preload" as="image" href="{e(preload_image)}" type="image/webp" fetchpriority="high">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Nunito+Sans:wght@700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css}">
</head>
<body data-page="{e(page_id)}" data-base="{base}" style="--page-hero-image: url('{e(css_image)}');">
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header" data-site-header></header>
  <main id="main">
{body_markup}
    <nav class="sequence-nav" data-sequence-nav aria-label="Previous and next pages"></nav>
  </main>
  <footer class="site-footer" data-site-footer></footer>
  <button class="back-to-top" type="button" data-back-to-top aria-label="Back to top">^</button>
  <script src="{site_data}"></script>
  <script src="{site_nav}"></script>
</body>
</html>
"""


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")


def builder_template(builder: dict) -> str:
    lines = [
        f"# {builder['title']}",
        "",
        f"Purpose: {builder['purpose']}",
        "",
        "Status: Draft for human review",
        "",
        "Note: the thought-starters below are optional. They are not directions, approved answers or a test.",
        "",
        "## Questions",
        "",
    ]
    for _name, label, hint in builder["fields"]:
        lines.extend([f"### {label}", "", f"Optional thought-starter: {hint}", "", "_Not answered yet._", ""])
    lines.extend(["## Boundaries", "", builder["boundary"], "", "## Next small step", "", builder["next_step"], ""])
    lines.extend([
        "## Ways to use this Markdown with AI",
        "",
        "Before sharing: inspect the file, remove private details, keep sources visible and decide whether the output is support, critique, learning or review.",
        "",
    ])
    for starter in AI_PROMPT_STARTERS:
        lines.extend([f"### {starter['title']}", "", f"Prompt: {starter['text']}", ""])
    lines.extend([
        "## Public repo copy or own repo",
        "",
        REPO_COPY_GUIDE["text"],
        "",
        f"Original repo: {PUBLIC_REPO_URL}",
        "",
        "Reuse note: see LICENCE.md before presenting a fork, public copy or AI-generated version as official.",
        "",
    ])
    return "\n".join(lines)


def write_site_data() -> None:
    sequence = [{"id": page["id"], "label": page["label"], "href": page["href"]} for page in PAGES]
    builder_sequence = [
        {"id": f"builder-{builder['id']}", "label": builder["title"], "href": f"builders/{builder['id']}.html"}
        for builder in BUILDERS
    ]
    final_sequence = []
    for item in sequence:
        final_sequence.append(item)
        if item["id"] == "builders":
            final_sequence.extend(builder_sequence)
    nav = [{"id": page["id"], "label": page["label"], "href": page["href"]} for page in PAGES]
    by_page_id = {item["id"]: item for item in nav}
    primary_nav = [by_page_id[item_id] for item_id in ["home", "start", "makerspace", "builders"]]
    nav_groups = [
        {
            "label": "Explore",
            "items": [by_page_id[item_id] for item_id in ["digital-twin", "sandworm-lab", "civilisation", "wealth", "culture"]],
        },
        {
            "label": "Sources",
            "items": [by_page_id[item_id] for item_id in ["boundaries", "sources", "licence", "site-map"]],
        },
    ]
    nav_order = [
        {"type": "link", "item": by_page_id["home"]},
        {"type": "link", "item": by_page_id["start"]},
        {"type": "link", "item": by_page_id["makerspace"]},
        {"type": "group", **nav_groups[0]},
        {"type": "link", "item": by_page_id["builders"]},
        {"type": "group", **nav_groups[1]},
    ]
    payload = {
        "nav": nav,
        "primaryNav": primary_nav,
        "navGroups": nav_groups,
        "navOrder": nav_order,
        "sequence": final_sequence,
    }
    write("assets/js/site-data.js", "window.SANDWORM_SITE = " + json.dumps(payload, indent=2) + ";\n")


def write_docs_site_map() -> None:
    lines = ["# Sandworm Subterranean Systems Site Map", ""]
    lines.append("## Pages")
    for page in PAGES:
        lines.append(f"- [{page['title']}](../{page['href']}) - {page['description']}")
    lines.extend(["", "## Builders"])
    for builder in BUILDERS:
        lines.append(f"- [{builder['title']}](../builders/{builder['id']}.html) - {builder['purpose']}")
    lines.extend(["", "## Source Bridges"])
    for link in COMPANION_LINKS:
        lines.append(f"- [{link['title']}]({link['site']}) - [{link['title']} repo]({link['repo']})")
    write("docs/site-map.md", "\n".join(lines) + "\n")


def main() -> None:
    write_site_data()
    for page in PAGES:
        body = BODY_RENDERERS[page["id"]]()
        write(page["href"], render_shell(page["id"], page["title"], page["description"], body, page["href"]))

    for builder in BUILDERS:
        page_id = f"builder-{builder['id']}"
        href = f"builders/{builder['id']}.html"
        write(href, render_shell(page_id, builder["title"], builder["purpose"], builder_body(builder), href))
        write(f"builders/{builder['id']}.md", builder_template(builder))

    write_docs_site_map()
    print(f"Built {len(PAGES)} pages and {len(BUILDERS)} builders.")


if __name__ == "__main__":
    main()
