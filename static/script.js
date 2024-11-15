function toggleHistory() {
    const historyModal = document.getElementById('historyModal');
    const modalOverlay = document.getElementById('modalOverlay');
    const isVisible = historyModal.style.display === 'block';
    
    historyModal.style.display = isVisible ? 'none' : 'block';
    modalOverlay.style.display = isVisible ? 'none' : 'block';
}

// Close modal if clicking outside of it
window.onclick = function(event) {
    const historyModal = document.getElementById('historyModal');
    const modalOverlay = document.getElementById('modalOverlay');
    if (event.target === modalOverlay) {
        historyModal.style.display = 'none';
        modalOverlay.style.display = 'none';
    }
}
