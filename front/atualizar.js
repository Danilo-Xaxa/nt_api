function formDataToJSON(form) {
    let formData = new FormData(form);
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


function linkFinal() {
    const form = document.getElementsByTagName('form')[0];
    let valores = formatJSON(formDataToJSON(form));
    let urlPut = "http://127.0.0.1:8000/crm/v3/objects/contacts/" + valores.apiKey + '/' + valores.jsonBody.contact;
    let contact = valores.jsonBody.contact;
    delete valores.jsonBody.contact;
    let jsonBody = valores.jsonBody;
    for (let key in jsonBody) {
        if (jsonBody[key] === '') {
            delete jsonBody[key];
        }
    }

    (async () => {
        const rawResponse = await fetch(urlPut, {
          method: 'PUT',
          mode: 'cors',
          headers: {
            'Accept': '*',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(jsonBody)
        });
        var content = await rawResponse.json();
      })();

    setTimeout(function() {
        console.log(content);
    }, 10000);

    if (jsonBody.email) {
      return "http://127.0.0.1:8000/crm/v3/objects/contacts/" + valores.apiKey + '?contact=' + jsonBody.email;
    }
    return "http://127.0.0.1:8000/crm/v3/objects/contacts/" + valores.apiKey + '?contact=' + contact;
};
