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
  
    // Validación del formulario
    
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault();
    
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;
    
        document.getElementById('usernameError').innerText = '';
        document.getElementById('passwordError').innerText = '';
        document.getElementById('loginError').style.display = 'none';
    
        // Enviar los datos al servidor para la autenticación

        fetch('/accounts/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ username: username, password: password })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                // Si la autenticación es exitosa, redirigir o hacer alguna acción deseada
                window.location.href = '/base/';
            } else {
                // Mostrar mensaje de error en caso de autenticación fallida
                document.getElementById('loginError').style.display = 'block';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
    
    // Función para obtener el valor de la cookie CSRF
    
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    
    