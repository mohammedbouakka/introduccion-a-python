<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Cuadrado</title>
</head>
<body>

    <h2>Calculadora de Cuadrado</h2>

    <form id="cuadradoForm">
        <label for="numero">Ingrese un número:</label>
        <input type="number" id="numero" name="numero" required>

        <br>

        <button type="button" onclick="calcularCuadrado()">Calcular Cuadrado</button>
    </form>

    <br>

    <p id="resultado"></p>

    <script>
        function calcularCuadrado() {
            var numero = parseFloat(document.getElementById("numero").value);

            if (!isNaN(numero)) {
                var cuadrado = numero * numero;

                document.getElementById("resultado").innerHTML = "El cuadrado es: " + cuadrado;
            } else {
                document.getElementById("resultado").innerHTML = "Por favor, ingrese un número válido.";
            }
        }
    </script>

</body>
</html>
