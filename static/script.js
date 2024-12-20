document.getElementById("uploadBtn").addEventListener("click", () => {
    document.getElementById("fileInput").click();
});

document.getElementById("fileInput").addEventListener("change", async (event) => {
    const file = event.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append("file", file);

        const response = await fetch("/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        displayResults(data);
    }
});

function displayResults(results) {
    const uploadSection = document.getElementById("upload-section");
    const resultSection = document.getElementById("result-section");
    const resultsDiv = document.getElementById("results");

    uploadSection.classList.add("hidden");
    resultSection.classList.remove("hidden");
    resultsDiv.innerHTML = "";

    Object.keys(results).forEach((key) => {
        const resultItem = document.createElement("div");
        resultItem.classList.add("result-item");

        const label = document.createElement("span");
        label.textContent = `${key}: ${results[key]}`;

        const barContainer = document.createElement("div");
        barContainer.classList.add("bar");

        const barFill = document.createElement("div");
        barFill.classList.add("fill");
        barFill.style.width = results[key];

        barContainer.appendChild(barFill);
        resultItem.appendChild(label);
        resultItem.appendChild(barContainer);
        resultsDiv.appendChild(resultItem);
    });
}
