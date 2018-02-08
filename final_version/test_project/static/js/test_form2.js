var addfield = document.querySelector("#addd");
var fieldContainer = document.querySelector('#forms_wrapper2');
var b = 0;
addfield.addEventListener("click", function() {
    var similarField = document.querySelector("#similar-field").content;
    var fieldElement = similarField.cloneNode(true);
    b++;
    fieldElement.querySelector("input").id = "login-field" + b;
    fieldElement.querySelector("label").setAttribute("for", "login-field" + b );
    fieldElement.querySelector("input").name = "name" + b;
    fieldElement.querySelector("label").textContent = "Name" + b;
    fieldContainer.appendChild(fieldElement);
});

