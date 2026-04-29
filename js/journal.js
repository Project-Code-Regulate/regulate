document.addEventListener("DOMContentLoaded", function () {
    renderJournal();
});

function deleteFromJournal(id) {
    let journal = JSON.parse(localStorage.getItem("journal")) || [];

    journal = journal.filter(function (entry) {
        return Number(entry.id) !== Number(id);
    });

    localStorage.setItem("journal", JSON.stringify(journal));

    renderJournal();
}

function renderJournal() {
    const container = document.getElementById("journal-list");
    const journal = JSON.parse(localStorage.getItem("journal")) || [];

    container.innerHTML = "";

    if (journal.length === 0) {
        container.innerHTML = "<p>No journal entries yet.</p>";
        return;
    }

    journal.forEach(function (entry) {
        const div = document.createElement("div");
        div.className = "journal-entry";

        const date = document.createElement("span");
        date.className = "entry-date";
        date.textContent = entry.date || "";

        const text = document.createElement("p");
        text.className = "entry-preview";
        text.textContent = entry.text || "";

        const meta = document.createElement("small");
        meta.textContent =
            "Pleasant: " + (entry.mood ?? "") +
            " | Stress: " + (entry.stress ?? "");

        const tagContainer = document.createElement("div");

        (entry.tags || []).forEach(function (t) {
            const tag = document.createElement("span");
            tag.className = "tag";
            tag.textContent = t;
            tagContainer.appendChild(tag);
        });

        const btn = document.createElement("button");
        btn.textContent = "Delete";
        btn.classList.add("delete");

        btn.addEventListener("click", function () {
            deleteFromJournal(entry.id);
        });

        div.appendChild(date);
        div.appendChild(text);
        div.appendChild(meta);
        div.appendChild(tagContainer);
        div.appendChild(btn);

        container.appendChild(div);
    });
}