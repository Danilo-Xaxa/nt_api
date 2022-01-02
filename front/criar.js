function formDataToJSON(formulario) {
    let formData = new FormData(formulario);
    let obj = {};
    formData.forEach(function(value, key){
      obj[key] = value;
    });
    return obj;
}


function formatJSON(json) {
    const apiKey = json.apiKey;
    delete json.apiKey;
    return {
        jsonBody: json,
        apiKey: apiKey
    };
}


function criar() {
    const formulario = document.getElementsByTagName('form')[0];
    let valores = formatJSON(formDataToJSON(formulario));
    let urlFinal = "http://127.0.0.1:8000/crm/v3/objects/contacts/" + valores.apiKey;
    let jsonBody = valores.jsonBody;

    (async () => {
        const rawResponse = await fetch(urlFinal, {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Accept': '*',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(jsonBody)
        });
        const content = await rawResponse.json();
      
        console.log(content);
      })();

    return false; // ou true? ou nada?
};
