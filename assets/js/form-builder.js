(function () {
  const definitionNode = document.getElementById("builder-definition");
  const form = document.querySelector("[data-builder-form]");
  const output = document.querySelector("[data-markdown-output]");
  const status = document.querySelector("[data-builder-status]");
  const copyButton = document.querySelector("[data-copy-markdown]");
  const downloadButton = document.querySelector("[data-download-markdown]");
  const clearButton = document.querySelector("[data-clear-form]");

  if (!definitionNode || !form || !output) return;

  const definition = JSON.parse(definitionNode.textContent);
  const storageKey = `sandworm-builder:${definition.id}`;

  function fields() {
    return Array.from(form.querySelectorAll("[name]"));
  }

  function collect() {
    const data = {};
    fields().forEach((field) => {
      data[field.name] = field.value.trim();
    });
    return data;
  }

  function save() {
    localStorage.setItem(storageKey, JSON.stringify(collect()));
  }

  function load() {
    try {
      const saved = JSON.parse(localStorage.getItem(storageKey) || "{}");
      fields().forEach((field) => {
        if (Object.prototype.hasOwnProperty.call(saved, field.name)) {
          field.value = saved[field.name];
        }
      });
    } catch (error) {
      localStorage.removeItem(storageKey);
    }
  }

  function line(value) {
    return value && value.length ? value : "_Not answered yet._";
  }

  function markdown() {
    const values = collect();
    const lines = [
      `# ${definition.title}`,
      "",
      `Purpose: ${definition.purpose}`,
      "",
      "Status: Draft for human review",
      "",
      "## Questions",
      ""
    ];

    definition.fields.forEach((field) => {
      lines.push(`### ${field.label}`);
      lines.push("");
      lines.push(line(values[field.name]));
      lines.push("");
    });

    lines.push("## Boundaries");
    lines.push("");
    lines.push(definition.boundary);
    lines.push("");
    lines.push("## Next small step");
    lines.push("");
    lines.push(definition.next_step);
    lines.push("");

    const starters = definition.ai_prompt_starters || [];
    if (starters.length || definition.repo_copy) {
      lines.push("## Ways to use this Markdown with AI");
      lines.push("");
      lines.push("Before sharing: inspect the file, remove private details, keep sources visible and decide whether the output is support, critique, learning or review.");
      lines.push("");
    }

    starters.forEach((starter) => {
      lines.push(`### ${starter.title}`);
      lines.push("");
      lines.push(`Prompt: ${starter.text}`);
      lines.push("");
    });

    if (definition.repo_copy) {
      lines.push("## Public repo copy or local version");
      lines.push("");
      lines.push(definition.repo_copy.text);
      lines.push("");
      lines.push(`Original repo: ${definition.repo_copy.href}`);
      lines.push("");
      lines.push("Reuse note: see LICENCE.md before presenting a fork, public copy or AI-generated version as official.");
      lines.push("");
    }

    return lines.join("\n");
  }

  function render() {
    output.value = markdown();
    save();
    if (status) status.textContent = "Draft updated in this browser.";
  }

  async function copyMarkdown() {
    output.select();
    try {
      await navigator.clipboard.writeText(output.value);
      if (status) status.textContent = "Markdown copied.";
    } catch (error) {
      document.execCommand("copy");
      if (status) status.textContent = "Markdown copied.";
    }
  }

  function downloadMarkdown() {
    const blob = new Blob([output.value], { type: "text/markdown;charset=utf-8" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = `${definition.filename}.md`;
    document.body.append(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(link.href);
    if (status) status.textContent = "Markdown downloaded.";
  }

  function clearForm() {
    fields().forEach((field) => {
      field.value = "";
    });
    localStorage.removeItem(storageKey);
    render();
    if (status) status.textContent = "Draft cleared.";
  }

  load();
  render();
  form.addEventListener("input", render);
  if (copyButton) copyButton.addEventListener("click", copyMarkdown);
  if (downloadButton) downloadButton.addEventListener("click", downloadMarkdown);
  if (clearButton) clearButton.addEventListener("click", clearForm);
})();
