/* Comportamiento del navbar al reducir el tamaño de la pantalla */

function openNav(){
    document.getElementById("mobile-menu").style.transform = "translateX(0)";
}

function closeNav(){
    document.getElementById("mobile-menu").style.transform = "translateX(-100%)";
}

/* Formulario */

    // Script para mostrar u ocultar la contraseña

    document.getElementById('togglePassword').addEventListener('click', function() {
        const passwordInput = document.getElementById('password');
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        this.textContent = type === 'password' ? 'Mostrar' : 'Ocultar';
      });