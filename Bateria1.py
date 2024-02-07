<!DOCTYPE html>
<html lang="ca">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Benvinguda</title>
  <script>
    function comprovarUsuari() {
      var nomUsuari = document.getElementById("nom").value;

      if (nomUsuari === "Amilcar" || nomUsuari === "Sila") {
        alert("Benvingut, " + nomUsuari + "!");
      } else {
        alert("Nom d'usuari no vàlid. Només es permeten 'Amilcar' o 'Sila'.");
      }
    }
  </script>
</head>
<body>
  <h1>Benvinguda</h1>
  <label for="nom">Introdueix el teu nom:</label>
  <input type="text" id="nom" name="nom">
  <button onclick="comprovarUsuari()">Verificar</button>
</body>
</html>
