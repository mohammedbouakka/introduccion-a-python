<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Saludo Personalizado</title>
</head>
<body>

    <h2>Saludo Personalizado</h2>

    <form id="saludoForm">
        <label for="nombre">Ingrese su nombre:</label>
        <input type="text" id="nombre" name="nombre" required>

        <br>

        <button type="button" onclick="generarSaludo()">Generar Saludo</button>
    </form>

    <br>

    <p id="saludoResultado"></p>

    <script>
        function generarSaludo() {
            // Obtener el valor del nombre desde el campo de entrada
            var nombre = document.getElementById("nombre").value;

            // Verificar si se proporcionó un nombre
            if (nombre.trim() !== "") {
                // Construir el saludo
                var saludo = "Hola " + nombre;

                // Mostrar el resultado
                document.getElementById("saludoResultado").innerHTML = saludo;
            } else {
                // Mostrar un mensaje de error si no se proporcionó un nombre
                document.getElementById("saludoResultado").innerHTML = "Por favor, ingrese su nombre.";
            }
        }
    </script>

</body>
</html>
