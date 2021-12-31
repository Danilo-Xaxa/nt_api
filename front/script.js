const form = document.getElementsByTagName('form')[0];


function formDataToJSON() {
  let formData = new FormData(form);
  let obj = {};
  formData.forEach(function(value, key){
    obj[key] = value;
  });
  // let json = JSON.stringify(obj);
  return obj;
}


function setAction(tipo, json) {
    switch (tipo) {
        case 'ver':
            form.action = 'localhost:8000/crm/v3/objects/contacts/' + json.apiKey;
            break;

        case 'criar':
            form.action = 'localhost:8000/crm/v3/objects/contacts/' + json.apiKey;
            // mas e o body?
            break;

        case 'atualizar':
            form.action = 'localhost:8000/crm/v3/objects/contacts/' + json.apiKey + json.contact;
            // mas e o body?
            break;

        default:
            break;
    }
}	


function formatJSON(json) {
    // só falta você, meu querido
}


function handle() {
    let json = formDataToJSON();
    json = formatJSON(json);
    let tipo = form.id.split('_')[1]
    setAction(tipo, json)
    return true; // false to cancel form action, true to submit form
}
