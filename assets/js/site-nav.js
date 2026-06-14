(function () {
  const data = window.SANDWORM_SITE || { nav: [], sequence: [] };
  const page = document.body.dataset.page || "home";
  const base = document.body.dataset.base || "";

  function withBase(href) {
    if (/^https?:\/\//.test(href)) return href;
    return `${base}${href}`;
  }

  function renderHeader() {
    const header = document.querySelector("[data-site-header]");
    if (!header) return;

    const primaryNav = data.primaryNav || data.nav || [];
    const navGroups = data.navGroups || [];
    const navLink = (item, className = "nav-link") =>
      `<a class="${className}" href="${withBase(item.href)}" ${item.id === page ? 'aria-current="page"' : ""}>${item.label}</a>`;
    const groupMarkup = navGroups.map((group) => {
      const hasCurrent = group.items.some((item) => item.id === page);
      return `
        <details class="nav-group ${hasCurrent ? "is-current" : ""}">
          <summary>${group.label}</summary>
          <div class="nav-menu">
            ${group.items.map((item) => navLink(item)).join("")}
          </div>
        </details>
      `;
    }).join("");

    header.innerHTML = `
      <nav class="nav" aria-label="Main navigation">
        <a class="brand" href="${withBase("index.html")}" aria-label="Sandworm Subterranean Systems home">
          <span class="brand-mark" aria-hidden="true">SS</span>
          <span class="brand-text"><strong>Sandworm</strong><span>Subterranean Systems</span></span>
        </a>
        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="siteNav">Menu</button>
        <div class="nav-links" id="siteNav">
          ${primaryNav.map((item) => navLink(item)).join("")}
          ${groupMarkup}
        </div>
      </nav>
    `;

    const toggle = header.querySelector(".nav-toggle");
    if (toggle) {
      toggle.addEventListener("click", () => {
        const isOpen = document.body.classList.toggle("nav-open");
        toggle.setAttribute("aria-expanded", String(isOpen));
      });
    }

    header.querySelectorAll(".nav-group").forEach((group) => {
      group.addEventListener("toggle", () => {
        if (!group.open) return;
        header.querySelectorAll(".nav-group").forEach((other) => {
          if (other !== group) other.open = false;
        });
      });
    });
  }

  function renderSequenceNav() {
    const nav = document.querySelector("[data-sequence-nav]");
    if (!nav) return;

    const index = data.sequence.findIndex((item) => item.id === page);
    if (index < 0) return;

    const previous = data.sequence[(index - 1 + data.sequence.length) % data.sequence.length];
    const next = data.sequence[(index + 1) % data.sequence.length];

    nav.innerHTML = `
      <a href="${withBase(previous.href)}"><span>Previous</span><strong>${previous.label}</strong></a>
      <a href="${withBase(next.href)}"><span>Next</span><strong>${next.label}</strong></a>
    `;
  }

  function renderFooter() {
    const footer = document.querySelector("[data-site-footer]");
    if (!footer) return;

    footer.innerHTML = `
      <div class="site-footer-inner">
        <div>
          <strong>Sandworm Subterranean Systems</strong>
          <p>Questions, trails, maker notes and source-aware builders for people exploring local capability without giving up sovereignty.</p>
        </div>
        <div class="footer-links">
          <a href="${withBase("builders/index.html")}">Markdown builders</a>
          <a href="${withBase("boundaries.html")}">Boundaries</a>
          <a href="${withBase("sources.html")}">Source trail</a>
          <a href="${withBase("site-map.html")}">Site map</a>
          <a href="https://auraofintelligence.github.io/civilisation-of-sand/" target="_blank" rel="noopener noreferrer">Civilisation of Sand</a>
        </div>
      </div>
    `;
  }

  function setupBackToTop() {
    const button = document.querySelector("[data-back-to-top]");
    if (!button) return;

    button.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
    const update = () => button.classList.toggle("is-visible", window.scrollY > 520);
    update();
    window.addEventListener("scroll", update, { passive: true });
  }

  function setupExternalLinks() {
    document.querySelectorAll('a[href^="http://"], a[href^="https://"]').forEach((link) => {
      link.target = "_blank";
      const rel = new Set((link.getAttribute("rel") || "").split(/\s+/).filter(Boolean));
      rel.add("noopener");
      rel.add("noreferrer");
      link.setAttribute("rel", Array.from(rel).join(" "));
    });
  }

  renderHeader();
  renderSequenceNav();
  renderFooter();
  setupBackToTop();
  setupExternalLinks();
})();
