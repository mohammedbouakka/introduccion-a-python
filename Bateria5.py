<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor de Temperatura</title>
</head>
<body>

    <h2>Conversor de Temperatura</h2>

    <form id="temperaturaForm">
        <label for="temperaturaCelsius">Ingrese la temperatura en grados Celsius:</label>
        <input type="number" id="temperaturaCelsius" name="temperaturaCelsius" step="0.01" required>

        <br>

        <button type="button" onclick="convertirTemperatura()">Convertir a Fahrenheit</button>
    </form>

    <br>

    <p id="temperaturaResultado"></p>

    <script>
        function convertirTemperatura() {
            var temperaturaCelsius = parseFloat(document.getElementById("temperaturaCelsius").value);

            if (!isNaN(temperaturaCelsius)) {
                var temperaturaFahrenheit = (temperaturaCelsius * 9/5) + 32;

                document.getElementById("temperaturaResultado").innerHTML = "La temperatura en Fahrenheit es: " + temperaturaFahrenheit.toFixed(2) + " °F";
            } else {
                document.getElementById("temperaturaResultado").innerHTML = "Por favor, ingrese una temperatura válida en grados Celsius.";
            }
        }
    </script>

</body>
</html>
