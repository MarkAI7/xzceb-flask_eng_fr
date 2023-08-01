function translateToFrench() {
    var textToTranslate = document.getElementById('textToTranslate').value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var responseJson = JSON.parse(xhttp.responseText);
            var translatedText = responseJson.translatedText;
            document.getElementById('translated_output').textContent = responseJson.translatedText;
        }
    };
    xhttp.open("GET", "/englishToFrench?textToTranslate=" + textToTranslate, true);
    xhttp.send();
}

function translateToEnglish() {
    var textToTranslate = document.getElementById('textToTranslate').value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var responseJson = JSON.parse(xhttp.responseText);
            var translatedText = responseJson.translatedText;
            document.getElementById('translated_output').textContent = responseJson.translatedText;

        }
    };
    xhttp.open("GET", "/frenchToEnglish?textToTranslate=" + textToTranslate, true);
    xhttp.send();
}
