function formDataToJSON(form) {
    let formData = new FormData(document.getElementById(form));
    let obj = {};
    formData.forEach(function(value, key){
      obj[key] = value;
    });
    let json = JSON.stringify(obj);

    console.log(json);
    return false; // false to cancel form action, true to submit form
}
