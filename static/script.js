// Function to preview the image before submission
function previewImage(event) {
    const preview = document.getElementById('previewImage');
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.style.display = 'block';
            preview.src = e.target.result;
        };
        reader.readAsDataURL(file);
    } else {
        preview.style.display = 'none';
    }
}

// Function to show the loading spinner
function showLoading() {
    const loading = document.getElementById('loading');
    loading.style.display = 'block';
}

// Add event listener to form submission to show the loading spinner
document.querySelector('form').addEventListener('submit', function() {
    showLoading();
});
