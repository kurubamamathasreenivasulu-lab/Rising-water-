document.addEventListener("DOMContentLoaded", function () {
    console.log("Flood Prediction System Loaded Successfully!");

    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function () {
            alert("Processing your flood prediction...");
        });
    }
});
