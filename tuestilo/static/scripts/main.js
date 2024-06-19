/* Comportamiento del navbar al reducir el tamaño de la pantalla */

function openNav(){
    document.getElementById("mobile-menu").style.transform = "translateX(0)";
}

function closeNav(){
    document.getElementById("mobile-menu").style.transform = "translateX(-100%)";
}
