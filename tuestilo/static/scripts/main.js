/* Comportamiento del navbar al reducir el tamaño de la pantalla */

function openNav(){
    document.getElementById("mobile-menu").style.transform = "translateX(0)";
}

function closeNav(){
    document.getElementById("mobile-menu").style.transform = "translateX(-100%)";
}

/* Validacion formulario */

function validateForm() {
    var username = document.getElementById('id_username').value;
    var password = document.getElementById('id_password').value;
    var usernameError = document.getElementById('usernameError');
    var passwordError = document.getElementById('passwordError');
    var isValid = true;

    // Reset error messages
    usernameError.innerHTML = '';
    passwordError.innerHTML = '';

    // Username validation (numeric characters only and minimum length)
    if (!/^\d+$/.test(username)) {
        usernameError.innerHTML = 'Username must contain only numbers.';
        isValid = false;
    } else if (username.length < 6) {
        usernameError.innerHTML = 'Username must be at least 6 characters long.';
        isValid = false;
    }

    // Password validation (minimum length)
    if (password.length < 8) {
        passwordError.innerHTML = 'Password must be at least 8 characters long.';
        isValid = false;
    }

    return isValid;
}
