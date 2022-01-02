function formDataToJSON() {
    let formulario = document.getElementsByTagName('form')[0];
    let formData = new FormData(formulario);
    let obj = {};
    formData.forEach(function(value, key){
    obj[key] = value;
    });
    return obj;
}


function formatJSON(json) {
    const apiKey = json.apiKey;
    let properties = ''
    for (let property in json) {
        if (['email', 'telefone', 'niver', 'peso'].includes(property.toString())) {
            properties = properties + `${property}-`
        }
    }
    if (properties.endsWith('-')) {
        properties = properties.slice(0, -1);
    }
    if (properties) {
        properties = 'properties=' + properties;
    }
    if (json.contact) {
        let contact = 'contact=' + json.contact;
        let queryParameters = properties ? contact + '&' + properties : contact;
        return {
            queryParameters: queryParameters,
            apiKey: apiKey
        };
    }
    let queryParameters = properties;
    return {
        queryParameters: queryParameters,
        apiKey: apiKey
    };
}


function linkFinal() {
    valores = formatJSON(formDataToJSON());
    let queryParameters = valores.queryParameters ? '?' + valores.queryParameters : '';
    return 'http://' + '127.0.0.1:8000/crm/v3/objects/contacts/' + valores.apiKey + queryParameters;
}
