<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor de Peso</title>
</head>
<body>

    <h2>Conversor de Peso</h2>

    <form id="pesoForm">
        <label for="pesoKg">Ingrese el peso en kilogramos:</label>
        <input type="number" id="pesoKg" name="pesoKg" step="0.01" required>

        <br>

        <button type="button" onclick="convertirPeso()">Convertir a Libras</button>
    </form>

    <br>

    <p id="pesoResultado"></p>

    <script>
        function convertirPeso() {
            var pesoKg = parseFloat(document.getElementById("pesoKg").value);

            if (!isNaN(pesoKg)) {
                var pesoLibras = pesoKg * 2.20462;

                document.getElementById("pesoResultado").innerHTML = "El peso en libras es: " + pesoLibras.toFixed(2) + " lbs";
            } else {
                document.getElementById("pesoResultado").innerHTML = "Por favor, ingrese un peso válido en kilogramos.";
            }
        }
    </script>

</body>
</html>
