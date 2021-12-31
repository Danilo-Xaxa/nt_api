function formDataToJSON() {
  let formData = new FormData(document.getElementsByTagName('form')[0]);
  let obj = {};
  formData.forEach(function(value, key){
    obj[key] = value;
  });
  // let json = JSON.stringify(obj);
  return obj;
}


function setAction(tipo, lista) {
    const primeiroForm = document.getElementsByTagName('form')[0];
    switch (tipo) {
        case 'ver':
            let queryParameters = lista[0] ? '?' + lista[0] : '';
            let finalURL = 'localhost:8000/crm/v3/objects/contacts/' + lista[1] + queryParameters
            return finalURL;
            break;

        case 'criar':
            primeiroForm.action = 'localhost:8000/crm/v3/objects/contacts/' + lista[1];
            // body = lista[0];
            break;

        case 'atualizar':
            primeiroForm.action = 'localhost:8000/crm/v3/objects/contacts/' + lista[1] + lista[2];
            // body = lista[0];
            break;

        default:
            break;
    }
}	


function formatJSON(tipo, json) {
    switch (tipo) {
        case 'ver':
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
                return [queryParameters, json.apiKey];
            }
            let queryParameters = properties;
            return [queryParameters, json.apiKey];
            break;

        case 'criar':
            return [json, json.apiKey]; // retorna um objeto para o body
            break;

        case 'atualizar':
            let jsonNovo = {}
            for (let property in json) {
                if (property in ['email', 'telefone', 'niver', 'peso']) {
                    jsonNovo[property] = json[property];
                }
            }
            return [json, json.apiKey, json.contact]
            break;

        default:
            throw new Error('ERRO');
            break;
    }
}


function linkFinal() {
    let primeiroForm = document.getElementsByTagName('form')[0];
    let tipo = primeiroForm.id.split('_')[1];
    let json = formDataToJSON();
    lista = formatJSON(tipo, json);
    return 'http://' + setAction(tipo, lista);
}
