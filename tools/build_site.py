from __future__ import annotations

import json
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_TITLE = "Sandworm Subterranean Systems"
BASE_URL = "https://auraofintelligence.github.io/sandworm-subterranean-systems/"
DESCRIPTION = (
    "An exploratory self-sovereign public workbench that starts with a maker space, "
    "then follows trails into Straddie digital twins, subterranean systems, Civilisation "
    "of Sand, film culture and documentary builders."
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
        "label": "Start",
        "href": "start.html",
        "title": "Choose A Trail",
        "description": "Pick a human-scale doorway into Sandworm Subterranean Systems.",
    },
    {
        "id": "makerspace",
        "label": "Maker space",
        "href": "makerspace.html",
        "title": "Start With A Maker Space",
        "description": "A practical surface workshop is the first step before any larger subterranean imagination.",
    },
    {
        "id": "digital-twin",
        "label": "Digital twin",
        "href": "digital-twin.html",
        "title": "Map The Place Without Owning The People",
        "description": "A Straddie digital twin trail for public-source mapping, point clouds, consent and local capability.",
    },
    {
        "id": "sandworm-lab",
        "label": "Sandworm lab",
        "href": "sandworm-lab.html",
        "title": "Prototype The Subterranean Questions",
        "description": "A speculative maker-to-systems lab for wet sand, silica, tunnel ideas and safety gates.",
    },
    {
        "id": "civilisation",
        "label": "Civilisation",
        "href": "civilisation-of-sand.html",
        "title": "Bridge To Civilisation Of Sand",
        "description": "A bridge from practical local work into the larger simulation, quest and capability story.",
    },
    {
        "id": "culture",
        "label": "Film trail",
        "href": "film-documentary-trail.html",
        "title": "Carry The Story Through Film",
        "description": "Quandamooka Film Festival and documentary builder bridges for story care, consent and cultural memory.",
    },
    {
        "id": "builders",
        "label": "Builders",
        "href": "builders/index.html",
        "title": "Markdown Builders",
        "description": "Browser-only forms that turn questions into clean Markdown drafts.",
    },
    {
        "id": "boundaries",
        "label": "Boundaries",
        "href": "boundaries.html",
        "title": "Boundaries Keep The Work Human",
        "description": "Consent, data dignity, cultural authority, safety and source posture for the Sandworm trail.",
    },
    {
        "id": "sources",
        "label": "Sources",
        "href": "sources.html",
        "title": "Source Trail",
        "description": "The local documents and companion repositories that informed this exploratory public site.",
    },
    {
        "id": "site-map",
        "label": "Site map",
        "href": "site-map.html",
        "title": "Site Map",
        "description": "All public pages, builder pages, Markdown templates and companion project links.",
    },
]


COMPANION_LINKS = [
    {
        "title": "Straddie Maker-Space Lab",
        "site": "https://auraofintelligence.github.io/straddie-makerspace-lab/",
        "repo": "https://github.com/auraofintelligence/straddie-makerspace-lab",
        "summary": "The practical surface doorway: tools, forms, experiments, sand, concrete and future workshop pathways.",
    },
    {
        "title": "Straddie Digital Twin Builders",
        "site": "https://auraofintelligence.github.io/straddie-digital-twin-builders/",
        "repo": "https://github.com/auraofintelligence/straddie-digital-twin-builders",
        "summary": "L0 to L2 prompt builders for private rooms, shared places, bioregions and simulation scenes.",
    },
    {
        "title": "Civilisation of Sand",
        "site": "https://auraofintelligence.github.io/civilisation-of-sand/",
        "repo": "https://github.com/auraofintelligence/civilisation-of-sand",
        "summary": "The larger quest and simulation layer for subterranean city thinking, capability paths and source-aware play.",
    },
    {
        "title": "Quandamooka Film Festival",
        "site": "https://auraofintelligence.github.io/quandamooka-film-festival/",
        "repo": "https://github.com/auraofintelligence/quandamooka-film-festival",
        "summary": "A film planning doorway for story seeds, boundaries, asset sharing, AI storyboarding and readiness.",
    },
    {
        "title": "Film Club Documentary Builders",
        "site": "https://auraofintelligence.github.io/film-club-documentary-builders/",
        "repo": "https://github.com/auraofintelligence/film-club-documentary-builders",
        "summary": "Markdown-first documentary workbench for film profiles, source trails, research angles and handoffs.",
    },
]


SOURCE_DOCS = [
    {
        "title": "10 Companies All At Once",
        "file": "10_Companies_All_At_Once.md",
        "use": "Positions Sandworm Subterranean Systems as one living organism inside a wider local ecosystem.",
    },
    {
        "title": "Makerspace Evolution to Underground Citadel",
        "file": "Makerspace Evolution to Underground Citadel.docx",
        "use": "Gives the strongest surface-to-subterranean pathway: workshop, tools, human rotation, kiosks, sensors and silica stack.",
    },
    {
        "title": "Subterranean Super Civilization Master Plan",
        "file": "Subterranean_Super_Civilization_Master_Plan.md",
        "use": "Supplies the Sandworm, silica citadel, material sovereignty and high-risk speculative imagination.",
    },
    {
        "title": "Subterranean Eco-City Quandamooka Development",
        "file": "Subterranean_Eco-City_Quandamooka_Development.md",
        "use": "Adds eco-city framing, Indigenous data sovereignty questions, co-operative pathways and braided economy ideas.",
    },
    {
        "title": "Subterranean City Multigenerational Resilience Framework",
        "file": "Subterranean_(3)_City__Multigenerational_Resilience_Framework.md",
        "use": "Adds phased sovereignty, legal overcompliance, material loops and inter-generational resilience language.",
    },
    {
        "title": "Subterranean Crystal City Kardashev Ground Station",
        "file": "Subterranean_Crystal_City_Kardashev_Ground_Station.md",
        "use": "Adds gamified learning, adaptive scaling and layered response prompts.",
    },
    {
        "title": "Global Subterranean Hyperloop And Micro Nova",
        "file": "global_subterranean_hyperloop_and_micro_nova.md",
        "use": "Supplies large-scale tunnelling and resilience scenarios that need careful public-source checking.",
    },
    {
        "title": "Local Government Funding Inquiry Submission",
        "file": "Local_Government_Funding_Inquiry_Submission.md",
        "use": "Connects digital twins, civic ledgers, community wealth and regenerative local government questions.",
    },
    {
        "title": "Project Aura Geode",
        "file": "Project_Aura_Geode__The_Alchemical_Genesis_of_a_Regenerative_Civilization.md",
        "use": "Adds co-operative architecture, self-understanding and human-centred technology patterns.",
    },
    {
        "title": "GenesisAI, Sands, And Kardashev Civilization",
        "file": "GenesisAI,_Sands,_and_Kardashev_Civilization.md",
        "use": "Adds scientific AI, materials simulation, sand batteries and federated intelligence as concept inputs.",
    },
]


BUILDERS = [
    {
        "id": "entry-trail",
        "title": "Entry Trail Builder",
        "purpose": "Choose a doorway into Sandworm without needing to accept the whole vision.",
        "filename": "sandworm-entry-trail",
        "boundary": "The trail is an invitation, not a test. People can stay, leave, disagree, or take only the part that helps.",
        "next_step": "Name one small practical action that would make the idea easier to understand.",
        "fields": [
            ("doorway", "Which doorway are you using?", "Making, mapping, filming, documentary research, sources, material loops, or another doorway."),
            ("question", "What question are you carrying?", "Write it as a real question, not a conclusion."),
            ("useful_output", "What would be useful to leave with?", "A note, map, source list, experiment card, film prompt, workshop plan, or handoff."),
        ],
    },
    {
        "id": "maker-space-brief",
        "title": "Maker Space Brief Builder",
        "purpose": "Turn a practical workshop idea into a small buildable brief.",
        "filename": "sandworm-maker-space-brief",
        "boundary": "A maker-space brief should respect safety, training, tool access, local noise, waste handling and human pace.",
        "next_step": "Choose one tool, one material, and one safety check to research next.",
        "fields": [
            ("project", "What could be made, repaired or tested?", "Keep it concrete enough for a first bench test."),
            ("tools", "What tools or spaces might be needed?", "Hand tools, CNC, 3D printing, solar sintering, mapping gear, benches, storage, or safety gear."),
            ("people", "Who would need support to participate well?", "First-timers, students, elders, technicians, artists, documentarians, local businesses, or volunteers."),
            ("review", "What needs review before anyone treats it as real?", "Safety, council rules, cultural authority, engineering, insurance, ecology, or funding."),
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
            ("place", "What place, object or system is being mapped?", "Name the real place if it is public-safe, or describe the concept level."),
            ("layers", "What layers belong in the twin?", "Photos, point cloud, paths, public assets, maintenance notes, ecological observations, oral history, or workshop data."),
            ("permissions", "Who has authority over the sensitive parts?", "Name the people, groups or review roles without assuming consent."),
            ("public_benefit", "What public benefit could the twin create?", "Better maintenance, learning, access, safety, planning, story care, or open-data capability."),
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
            ("idea", "What is the experiment idea?", "Wet sand stabilisation, silica block, material passport, sensor loop, slurry model, or tunnel simulation."),
            ("small_test", "What is the smallest safe test?", "A tabletop model, literature review, digital simulation, interview, material sample, or workshop exercise."),
            ("unknowns", "What is unknown or risky?", "Geology, water, ecology, law, culture, energy, cost, safety, waste, or evidence quality."),
            ("stop_rule", "When should the idea stop or slow down?", "Name a clear condition that means review comes before momentum."),
        ],
    },
    {
        "id": "film-documentary-trail",
        "title": "Film And Documentary Trail Builder",
        "purpose": "Carry a Sandworm idea into film, documentary or festival planning without taking over the story.",
        "filename": "sandworm-film-documentary-trail",
        "boundary": "The story stays with the people who carry it. AI and templates can help structure notes, but they do not own meaning.",
        "next_step": "Choose whether the next output is a story seed, source trail, interview map, storyboard or permissions list.",
        "fields": [
            ("story_seed", "What story seed is present?", "A person, place, question, material, experiment, source trail, workshop, or future scene."),
            ("holders", "Who might hold the story or need a say?", "Do not assume public permission. Name review roles carefully."),
            ("assets", "What assets or evidence might help?", "Photos, audio, maps, public records, interviews, sketches, footage, documents, or workshop notes."),
            ("care", "What care should shape the story?", "Privacy, culture, grief, humour, youth safety, permissions, ecological sensitivity, or uncertainty."),
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
            ("claim", "What claim or idea is being tracked?", "Keep it narrow enough to check."),
            ("source", "Where did it come from?", "Document, repo, public website, observation, interview, official record, model output, or brainstorm."),
            ("confidence", "How confident should a public reader be?", "Concept only, needs checking, source-backed, community-reviewed, or not public yet."),
            ("reviewer", "Who or what should review it?", "A person, community authority, engineer, scientist, council source, legal source, or public dataset."),
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
            ("context", "What trail or idea is being checked?", "Name the page, project, source, experiment, place or story."),
            ("boundaries", "Which boundaries matter here?", "Consent, private data, cultural authority, safety, ecological impact, law, funding, public claims, or youth protection."),
            ("missing_voice", "Whose voice or authority is missing?", "Do not fill the gap by guessing. Name the gap."),
            ("safe_public_version", "What is the safe public version for now?", "Draft, anonymised note, question, private only, source list, or nothing public yet."),
        ],
    },
]


def e(value: str) -> str:
    return escape(value, quote=True)


def attrs_for_page(page_id: str) -> tuple[str, str]:
    in_builders = page_id.startswith("builder-") or page_id == "builders"
    return ("../" if page_id.startswith("builder-") else "", "../" if page_id.startswith("builder-") else "")


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


def repo_grid() -> str:
    cards = []
    for link in COMPANION_LINKS:
        cards.append(
            '<article class="repo-card">'
            f'<p class="mini-label">Companion repo</p><h3>{e(link["title"])}</h3>'
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
      <h1>Sandworm Subterranean Systems</h1>
      <p class="hero-lede">Start with a maker space. Map the place with care. Follow the trails into subterranean systems, story, film and source-aware experiments without asking anyone to surrender their sovereignty.</p>
      <div class="hero-actions">
        <a class="button primary" href="start.html">Choose a trail</a>
        <a class="button secondary" href="builders/index.html">Open builders</a>
      </div>
      <p class="micro-note">Exploratory, public, correction-friendly. Questions before claims.</p>
    </div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading centred">
      <p class="section-label">Explorer doorway</p>
      <h2>Five starting points, one living inquiry.</h2>
      <p class="lede">Each trail begins at human scale: a bench, a map, a safe question, a story seed, a source note.</p>
    </div>
""" + card_grid([
        {"label": "Trail 01", "title": "Make first", "text": "Use the maker-space path to turn a large idea into a small workshop question.", "href": "makerspace.html", "action": "Open trail"},
        {"label": "Trail 02", "title": "Map with consent", "text": "Use the digital twin path to separate public layers, permission layers and private layers.", "href": "digital-twin.html", "action": "Open trail"},
        {"label": "Trail 03", "title": "Prototype carefully", "text": "Use the Sandworm lab path to keep speculative engineering behind safety and source gates.", "href": "sandworm-lab.html", "action": "Open trail"},
        {"label": "Trail 04", "title": "Play the simulation", "text": "Use Civilisation of Sand as a quest world for capability, not a doctrine.", "href": "civilisation-of-sand.html", "action": "Open trail"},
        {"label": "Trail 05", "title": "Carry the story", "text": "Use film and documentary builders when the work needs culture, memory and public care.", "href": "film-documentary-trail.html", "action": "Open trail"},
        {"label": "Trail 06", "title": "Leave a clean note", "text": "Use Markdown builders to turn the next question into a draft an AI or human can continue.", "href": "builders/index.html", "action": "Open builders"},
    ]) + """
  </div>
</section>
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Core posture</p>
      <h2>Self-sovereign means people keep the steering wheel.</h2>
      <p class="lede">The site does not ask visitors to believe everything, join everything or hand over private data. It offers trails, asks better questions and helps create useful notes.</p>
    </div>
    <div class="quote-panel">What can we learn, build, map, repair or film together while keeping consent, dignity and local authority intact?</div>
  </div>
</section>
<section class="section deep-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Connected public work</p>
      <h2>Sandworm starts in the repo family.</h2>
      <p class="lede">The project begins by linking five existing public workbenches: maker space, digital twin builders, Civilisation of Sand, film festival tooling and documentary builders.</p>
    </div>
""" + repo_grid() + """
  </div>
</section>
"""


def start_body() -> str:
    page = by_id("start")
    return page_hero(page) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Pick your entry</p>
      <h2>You do not need to start with the biggest idea.</h2>
      <p class="lede">A useful trail is simply a sequence of questions that leaves you with more clarity and more agency than you had before.</p>
    </div>
""" + pathway([
        ("Touch the surface", "Start with a maker-space question: what could be repaired, prototyped, measured or taught locally?"),
        ("Map the shared place", "Move into digital twin questions: what is public, what needs permission and what should stay private?"),
        ("Ask the subterranean question", "Explore Sandworm systems as cautious prototypes, simulations and source trails before any physical ambition."),
        ("Open the simulation layer", "Use Civilisation of Sand as a story-space for capability, resource loops and choices under pressure."),
        ("Carry it through culture", "When the idea needs people, memory and public meaning, bring in film and documentary builders."),
    ]) + """
    <div class="callout">
      <div><h3>Leave with a Markdown handoff.</h3><p>A clean `.md` draft is a small bridge between high-level thought and practical next work.</p></div>
      <a class="button primary" href="builders/index.html">Open builders</a>
    </div>
  </div>
</section>
"""


def makerspace_body() -> str:
    return page_hero(by_id("makerspace")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Surface first</p>
      <h2>A maker space gives the big vision somewhere honest to begin.</h2>
      <p class="lede">Before anyone talks about tunnels, citadels or civilisational systems, there is a simpler question: what can a local workshop help people learn, make, repair and document together?</p>
    </div>
    <div class="visual-panel"><img src="assets/img/sandworm-subterranean-systems-hero.png" alt="Coastal maker lab and subterranean systems concept image"></div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Questions to carry</p><h2>Workshop questions before system claims.</h2></div>
""" + question_list([
        "What can be made from safe, local, reused or well-understood materials?",
        "Which tools build confidence rather than dependency?",
        "What training, supervision and safety checks would make first-timers feel welcome?",
        "What should be documented as a public recipe, and what should stay private?",
        "What evidence would make the next prototype easier to trust?",
    ]) + """
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Companion doorway</p><h2>Use the existing maker-space lab as the first bench.</h2></div>
""" + card_grid([
        {"label": "Public site", "title": "Straddie Maker-Space Lab", "text": "Open the existing forms, tool trails, sand, concrete and future pages.", "href": "https://auraofintelligence.github.io/straddie-makerspace-lab/", "action": "Visit site"},
        {"label": "Builder", "title": "Maker Space Brief", "text": "Turn one repair, prototype or workshop idea into a clean Markdown draft.", "href": "builders/maker-space-brief.html", "action": "Use builder"},
        {"label": "Boundary", "title": "Safety before momentum", "text": "Use the boundary check when tools, machines, materials or public claims need review.", "href": "builders/boundary-check.html", "action": "Check"},
    ]) + """
  </div>
</section>
"""


def digital_twin_body() -> str:
    return page_hero(by_id("digital-twin")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Mirror, not trap</p>
      <h2>A digital twin can help a community see patterns without turning people into data mines.</h2>
      <p class="lede">The useful question is not "how much can we capture?" It is "what should be visible, to whom, for what purpose, and under whose authority?"</p>
    </div>
""" + pathway([
        ("Level 0", "Private room, object, bench, tool or personal workspace. The person keeps control."),
        ("Level 1", "Shared place, venue, project, public asset or workshop scene. Permissions and context matter."),
        ("Level 2", "Bioregion, route, island, bay, catchment or system. Public sources and cultural authority matter more."),
    ]) + """
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Questions to carry</p><h2>Point clouds are powerful. So are boundaries.</h2></div>
""" + question_list([
        "Which layers are public-source and useful for everyone?",
        "Which layers need permission, context or cultural review?",
        "Which details should not be collected at all?",
        "How can a twin build local capability instead of outsourcing local memory?",
        "What correction path lets people improve the map later?",
    ]) + """
  </div>
</section>
<section class="section">
  <div class="section-inner">
""" + card_grid([
        {"label": "Public site", "title": "Straddie Digital Twin Builders", "text": "Use the existing L0, L1 and L2 builder set for public-safe visual and simulation prompts.", "href": "https://auraofintelligence.github.io/straddie-digital-twin-builders/", "action": "Visit site"},
        {"label": "Builder", "title": "Digital Twin Brief", "text": "Write a sovereignty-aware map or twin brief for this Sandworm trail.", "href": "builders/digital-twin-brief.html", "action": "Use builder"},
        {"label": "Source", "title": "Source Trail", "text": "Separate observations, public records, permissions and claims that need checking.", "href": "builders/source-trail.html", "action": "Track source"},
    ]) + """
  </div>
</section>
"""


def sandworm_lab_body() -> str:
    return page_hero(by_id("sandworm-lab")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Prototype posture</p>
      <h2>The Sandworm is a question engine before it is a machine.</h2>
      <p class="lede">The source notes imagine wet-sand tunnelling, silica lining, material loops and subterranean resilience. This public trail keeps those ideas exploratory: testable pieces, source checks, engineering review and clear stop rules.</p>
    </div>
    <div class="quote-panel">What is the smallest harmless test that teaches something real?</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Lab trails</p><h2>Speculative does not have to be careless.</h2></div>
""" + card_grid([
        {"label": "Material loop", "title": "Silica, sand and safe samples", "text": "Track possible materials as passports: source, safe use, unknowns, reuse path and review needed."},
        {"label": "Simulation", "title": "Wet-sand questions", "text": "Explore hydrology, slurry, stabilisation and tunnel-support ideas as models before physical claims."},
        {"label": "Systems", "title": "Sensors and kiosks", "text": "Connect the makerspace to low-power nodes, public screens, LoRa-style thinking and place-based monitoring."},
        {"label": "Human layer", "title": "Try everything carefully", "text": "Rotate learning without treating people as replaceable parts. Capability grows with care."},
        {"label": "Review gate", "title": "Stop rules", "text": "Name conditions where culture, safety, ecology, law or engineering review comes first."},
        {"label": "Story trail", "title": "Make it understandable", "text": "Use film, diagrams and Markdown notes so non-technical people can inspect the thinking."},
    ]) + """
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Builder</p><h2>Turn one big subterranean idea into a cautious experiment card.</h2></div>
    <a class="button primary" href="builders/sandworm-experiment.html">Use Sandworm experiment builder</a>
  </div>
</section>
"""


def civilisation_body() -> str:
    return page_hero(by_id("civilisation")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Simulation bridge</p>
      <h2>Civilisation of Sand is the quest layer.</h2>
      <p class="lede">Sandworm asks practical and engineering questions. Civilisation of Sand turns those questions into a playable public story about capability, resource loops, care, in-situ materials and choices under pressure.</p>
    </div>
""" + question_list([
        "What capability would help people sooner, even if the largest vision never happened?",
        "Which resource loop is safe enough to teach in public?",
        "What should be simulated before anyone argues about building it?",
        "What story helps people understand trade-offs without being pushed?",
        "Where does a quest need a source note, not a confident claim?",
    ]) + """
    <div class="callout">
      <div><h3>Open the sibling simulation.</h3><p>Use it as a question world, not a demand that anyone believe every source note.</p></div>
      <a class="button primary" href="https://auraofintelligence.github.io/civilisation-of-sand/">Visit Civilisation of Sand</a>
    </div>
  </div>
</section>
"""


def culture_body() -> str:
    return page_hero(by_id("culture")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Culture as infrastructure</p>
      <h2>Some systems only become real when people can tell the story back.</h2>
      <p class="lede">Film, documentary notes and festival pathways give the work a human memory layer. They help people ask: who is this for, what is being shown, what is being left private, and what care is needed before publication?</p>
    </div>
    <div class="quote-panel">A good story trail does not take the story. It makes the next respectful conversation easier.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
""" + card_grid([
        {"label": "Public site", "title": "Quandamooka Film Festival", "text": "A practical story planning doorway for film ideas, boundaries, storyboarding and readiness.", "href": "https://auraofintelligence.github.io/quandamooka-film-festival/", "action": "Visit site"},
        {"label": "Public site", "title": "Film Club Documentary Builders", "text": "Markdown-first builders for source trails, research angles, scene analysis and handoffs.", "href": "https://auraofintelligence.github.io/film-club-documentary-builders/", "action": "Visit site"},
        {"label": "Builder", "title": "Film And Documentary Trail", "text": "Carry a Sandworm idea into story planning without taking over meaning.", "href": "builders/film-documentary-trail.html", "action": "Use builder"},
    ]) + """
  </div>
</section>
"""


def boundaries_body() -> str:
    return page_hero(by_id("boundaries")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Human guardrails</p><h2>Boundaries make the exploration stronger.</h2><p class="lede">They keep the work from sliding into extraction, false authority, private-data capture or unsafe engineering momentum.</p></div>
""" + card_grid([
        {"label": "Consent", "title": "Ask before carrying someone else's story", "text": "A story, image, place memory or cultural detail can be powerful without being yours to publish."},
        {"label": "Data", "title": "Keep private layers private", "text": "A digital twin should clarify public systems without exposing household, health, identity or vulnerable-person details."},
        {"label": "Culture", "title": "Do not claim authority you do not hold", "text": "Public pages should not imply endorsement, approval or representation where it has not been granted."},
        {"label": "Safety", "title": "Prototype behind gates", "text": "Material, tunnel, energy, sensor and machine ideas need review before they become physical activity."},
        {"label": "Sources", "title": "Questions before claims", "text": "Speculative notes can inspire better questions without becoming public certainty."},
        {"label": "Sovereignty", "title": "Participation stays voluntary", "text": "People should be able to use, reject, correct or ignore the tools without losing dignity."},
    ]) + """
    <div class="callout">
      <div><h3>Need a quick review note?</h3><p>Use the builder to name the boundary before the project gets louder.</p></div>
      <a class="button primary" href="builders/boundary-check.html">Use boundary check</a>
    </div>
  </div>
</section>
"""


def sources_body() -> str:
    cards = []
    for source in SOURCE_DOCS:
        cards.append(
            '<article class="source-card">'
            f'<p class="mini-label">Local source</p><h3>{e(source["title"])}</h3>'
            f'<p><code>{e(source["file"])}</code></p><p>{e(source["use"])}</p>'
            '</article>'
        )
    return page_hero(by_id("sources")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Source posture</p>
      <h2>The documents are fuel for inquiry, not automatic public proof.</h2>
      <p class="lede">Some source notes are practical. Some are speculative. Some use intense civilisational language. This site keeps them visible as a trail while asking for source checks, consent checks and human review before public claims harden.</p>
    </div>
    <div class="source-grid">
""" + "".join(cards) + """
    </div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Verified companion links</p><h2>Public bridge targets checked during build.</h2></div>
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
"""


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
        "fields": [
            {"name": name, "label": label, "hint": hint}
            for name, label, hint in builder["fields"]
        ],
    }

    page = {
        "title": builder["title"],
        "description": builder["purpose"],
    }

    definition_json = json.dumps(definition).replace("</", "<\\/")

    return page_hero(page) + f"""
<section class="section">
  <div class="section-inner builder-layout">
    <div class="builder-panel">
      <p class="section-label">Draft form</p>
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
    <div class="section-heading"><p class="section-label">Companion projects</p><h2>External bridges</h2></div>
    {repo_grid()}
  </div>
</section>
"""


def by_id(page_id: str) -> dict[str, str]:
    for page in PAGES:
        if page["id"] == page_id:
            return page
    raise KeyError(page_id)


BODY_RENDERERS = {
    "home": home_body,
    "start": start_body,
    "makerspace": makerspace_body,
    "digital-twin": digital_twin_body,
    "sandworm-lab": sandworm_lab_body,
    "civilisation": civilisation_body,
    "culture": culture_body,
    "builders": builders_index_body,
    "boundaries": boundaries_body,
    "sources": sources_body,
    "site-map": site_map_body,
}


def render_shell(page_id: str, title: str, description: str, body: str, path: str) -> str:
    base = "../" if "/" in path else ""
    canonical = BASE_URL + path
    css = base + "assets/css/styles.css"
    favicon = base + "assets/img/favicon.svg"
    site_data = base + "assets/js/site-data.js"
    site_nav = base + "assets/js/site-nav.js"
    image = BASE_URL + "assets/img/sandworm-subterranean-systems-hero.png"
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
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Nunito+Sans:wght@700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css}">
</head>
<body data-page="{e(page_id)}" data-base="{base}">
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
        "## Questions",
        "",
    ]
    for _name, label, hint in builder["fields"]:
        lines.extend([f"### {label}", "", f"Prompt: {hint}", "", "_Not answered yet._", ""])
    lines.extend(["## Boundaries", "", builder["boundary"], "", "## Next small step", "", builder["next_step"], ""])
    return "\n".join(lines)


def write_site_data() -> None:
    sequence = [{"id": page["id"], "label": page["label"], "href": page["href"]} for page in PAGES]
    builder_sequence = [
        {"id": f"builder-{builder['id']}", "label": builder["title"], "href": f"builders/{builder['id']}.html"}
        for builder in BUILDERS
    ]
    final_sequence = sequence[:8] + builder_sequence + sequence[8:]
    nav = [{"id": page["id"], "label": page["label"], "href": page["href"]} for page in PAGES if page["id"] in {
        "home", "start", "makerspace", "digital-twin", "sandworm-lab", "civilisation", "culture", "builders", "boundaries", "sources"
    }]
    payload = {"nav": nav, "sequence": final_sequence}
    write("assets/js/site-data.js", "window.SANDWORM_SITE = " + json.dumps(payload, indent=2) + ";\n")


def write_docs_site_map() -> None:
    lines = ["# Sandworm Subterranean Systems Site Map", ""]
    lines.append("## Pages")
    for page in PAGES:
        lines.append(f"- [{page['title']}](../{page['href']}) - {page['description']}")
    lines.extend(["", "## Builders"])
    for builder in BUILDERS:
        lines.append(f"- [{builder['title']}](../builders/{builder['id']}.html) - {builder['purpose']}")
    lines.extend(["", "## Companion Links"])
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
