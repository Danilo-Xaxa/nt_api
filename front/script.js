function formDataToJSON() {
    let form = document.getElementById('formulario');
    let formData = new FormData(form);
    let obj = {};
    formData.forEach(function(value, key){
      obj[key] = value;
    });

    // let json = JSON.stringify(obj);
    // console.log(json);

    //form.action = 'http://localhost:8000/crm/v3/objects/contacts/' + obj.apiKey;
    //return true;

    return false; // false to cancel form action, true to submit form
}
