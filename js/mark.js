// MARK.JS - Premium design & interaction logic for the AI SDR page

export function initMarkAnimations() {
    // Standard reveals are handled by the inline script in mark.html
    // This file can be used for more complex mark-specific logic later
}

// Form logic
window.submitForm = function(e) {
    e.preventDefault();
    const form = document.getElementById('betaForm');
    const success = document.getElementById('formSuccess');
    if (form && success) {
        form.style.display = 'none';
        success.style.display = 'block';
    }
};
