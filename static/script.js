// Image preview function
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

// Toggle history modal display
function toggleHistory() {
    const historyModal = document.getElementById('historyModal');
    historyModal.style.display = historyModal.style.display === 'block' ? 'none' : 'block';
}

// Close modal if clicking outside of it
window.onclick = function(event) {
    const historyModal = document.getElementById('historyModal');
    if (event.target === historyModal) {
        historyModal.style.display = 'none';
    }
}
