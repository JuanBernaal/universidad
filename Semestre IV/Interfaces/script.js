document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita que el formulario se envíe normalmente

    // Obtiene los valores de usuario y contraseña ingresados por el usuario
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Comprueba si el usuario y la contraseña son válidos (esto es solo un ejemplo básico)
    if (username === "usuario" && password === "contraseña") {
        // Si son válidos, redirige a otra página o realiza alguna acción adicional
        window.location.href = "dashboard.html"; // Redirige a una página de dashboard, por ejemplo
    } else {
        // Si no son válidos, muestra un mensaje de error
        document.getElementById("message").innerHTML = "Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.";
    }
});
