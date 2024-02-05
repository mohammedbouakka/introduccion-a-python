<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Suma</title>
</head>
<body>

    <h2>Calculadora de Suma</h2>

    <form id="sumaForm">
        <label for="num1">Número 1:</label>
        <input type="number" id="num1" name="num1" required>

        <br>

        <label for="num2">Número 2:</label>
        <input type="number" id="num2" name="num2" required>

        <br>

        <button type="button" onclick="calcularSuma()">Calcular Suma</button>
    </form>

    <br>

    <p id="resultado"></p>

    <script>
        function calcularSuma() {
      
            var num1 = parseFloat(document.getElementById("num1").value);
            var num2 = parseFloat(document.getElementById("num2").value);

          
            if (!isNaN(num1) && !isNaN(num2)) {
                // Calcular la suma
                var suma = num1 + num2;

               
                document.getElementById("resultado").innerHTML = "La suma es: " + suma;
            } else {
                document.getElementById("resultado").innerHTML = "Por favor, ingrese números válidos.";
            }
        }
    </script>

</body>
</html>

