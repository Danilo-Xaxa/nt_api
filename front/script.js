function formDataToJSON() {
  let formData = new FormData(document.getElementsByTagName('form')[0]);
  let obj = {};
  formData.forEach(function(value, key){
    obj[key] = value;
  });
  // let json = JSON.stringify(obj);
  return obj;
}


async function postar(url, body) {
    const urlFinal = 'http://' + url;

    const axios = require('axios')
    const qs = require('qs')

    const options = {
        method: 'POST',
        headers: { 'content-type': 'application/x-www-form-urlencoded' },
        data: qs.stringify(body),
        url: urlFinal
    }

    axios(options)
    .then(function(response) {
        console.log(response.data)
    })
    .catch(function(error) {
        console.log(error)
    })
}


function setAction(tipo, valores) {
    const formulario = document.getElementsByTagName('form')[0];
    const queryParameters = valores.queryParameters ? '?' + valores.queryParameters : '';
    const apiKey = valores.apiKey;
    const jsonBody = valores.jsonBody;
    switch (tipo) {
        case 'ver':
            let resultado = 'localhost:8000/crm/v3/objects/contacts/' + apiKey + queryParameters
            return resultado;
            break;

        case 'criar':
            postar('localhost:8000/crm/v3/objects/contacts/' + apiKey, jsonBody);
            break;

        case 'atualizar':
            formulario.action = 'localhost:8000/crm/v3/objects/contacts/' + apiKey + valores.contact;
            // body = jsonBody;
            break;

        default:
            break;
    }
}	


function formatJSON(tipo, json) {
    const apiKey = json.apiKey;
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
            break;

        case 'criar':
            delete json.apiKey;
            return {
                jsonBody: json,
                apiKey: apiKey
            };
            break;

        case 'atualizar':
            let contact = 'contact=' + json.contact;
            delete json.apiKey;
            return {
                jsonBody: json,
                apiKey: apiKey,
                contact: contact
            }
            break;

        default:
            throw new Error('ERRO');
            break;
    }
}


function linkFinal() {
    let formulario = document.getElementsByTagName('form')[0];
    let tipo = formulario.id.split('_')[1];
    let json = formDataToJSON();
    valores = formatJSON(tipo, json);
    return 'http://' + setAction(tipo, valores);
}
