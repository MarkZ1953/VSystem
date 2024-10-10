export function showToast(toastId, message, alertType = 'success') {
    // Selecciona el toast y el área de mensaje
    const toastEl = document.getElementById(toastId);
    const toastMessageEl = toastEl.querySelector('.toast-body');
    
    // Ajusta el mensaje y el estilo según el tipo de alerta
    toastMessageEl.textContent = message;
    toastEl.classList.remove('bg-success', 'bg-danger', 'bg-warning', 'bg-info');
    toastEl.classList.add(`bg-${alertType}`, 'text-light');

    // Muestra el toast
    const toast = new bootstrap.Toast(toastEl);
    toast.show();

    // Oculta el toast automáticamente después de 4 segundos
    setTimeout(() => {
        toast.hide();
    }, 4000);
}
