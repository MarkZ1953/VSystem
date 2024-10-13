var internalErrorMessage = "Se ha producido un error interno. Por favor, inténtelo de nuevo más tarde o póngase en contacto con nuestro servicio al cliente para obtener asistencia.";

export function alertController({idAlert, message, type = "danger", timeOut = 3000}) {
    var alertElement = document.getElementById(idAlert);
    var msg = message

    if (message === "internalError") {
        msg = internalErrorMessage;
    }

    alertElement.innerHTML = `
        <div class="alert alert-${type}" role="alert"> 
            ${msg}
        </div>
    `;    
    
    setTimeout(() => {
        alertElement.innerHTML = ""
    }, timeOut)
}