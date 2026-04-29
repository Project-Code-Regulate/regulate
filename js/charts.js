window.onload = () => {
    const journal = JSON.parse(localStorage.getItem("journal")) || [];

    const ordered = [...journal].reverse();

    const labels = ordered.map((_, i) => i + 1);

    const pleasant = ordered.map(e => Number(e.mood));
    const stress = ordered.map(e => Number(e.stress));

    const ctx = document.getElementById("moodChart");

    new Chart(ctx, {
        type: "line",
        data: {
            labels,
            datasets: [
                {
                    label: "Pleasant",
                    data: pleasant,
                    borderColor: "#a882ab",
                    tension: 0
                },
                {
                    label: "Stress",
                    data: stress,
                    borderColor: "#ccaa6a",
                    tension: 0
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: { display: true, text: "Entry" }
                },
                y: {
                    suggestedMin: 0,
                    suggestedMax: 100
                }
            }
        }
    });
};