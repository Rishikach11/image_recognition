// Show loading spinner
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const loadingSpinner = document.getElementById("loading");
    const fileInput = document.getElementById("fileInput");
    const previewImage = document.getElementById("previewImage");

    // Show loading spinner on form submit
    form.addEventListener("submit", () => {
        loadingSpinner.style.display = "block";
    });

    // Image preview
    fileInput.addEventListener("change", (event) => {
        const file = event.target.files[0];
        if (file) {
            previewImage.src = URL.createObjectURL(file);
            previewImage.style.display = "block";
        }
    });
});
