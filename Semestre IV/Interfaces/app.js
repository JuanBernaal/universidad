const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware para analizar el cuerpo de las solicitudes JSON
app.use(bodyParser.json());

// Servir archivos estáticos desde el directorio "public"
app.use(express.static(path.join(__dirname, 'public')));

// Ruta para manejar la solicitud de inicio de sesión
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    // Aquí deberías tener tu lógica de autenticación
    // Por simplicidad, este es un ejemplo básico
    if (username === 'usuario' && password === 'contraseña') {
        res.json({ success: true });
    } else {
        res.json({ success: false });
    }
});

// Ruta para la página de inicio de sesión
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`Servidor iniciado en http://localhost:${PORT}`);
});
