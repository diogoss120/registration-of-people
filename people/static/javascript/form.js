document.querySelector("textarea[name='obervation']").required = false;
document.querySelector("input[name='nickname']").required = false;

let form = document.querySelector('form');

let btn_get_name = document.querySelector(".btn-get-name");
let btn_submit = document.querySelector(".btn-submit");
let btn_delete = document.querySelector(".btn-delete");

if (btn_get_name) {
    btn_get_name.addEventListener("click", e => {
        changeFormAction(e, '/get-name/');
    });

    btn_submit.addEventListener("click", e => {
        changeFormAction(e, '/');
    });
}

if (btn_delete) {
    let id = btn_delete.dataset.id_person;
    console.log('id person: ', id);
    btn_delete.addEventListener('click', e => {
        location.href = `/delete/${id}`;
    })
}

function changeFormAction(event, path) {

    event.preventDefault();
    form.action = path;
    form.submit();

}

function getNameFromAPI() {
    let url = 'http://gerador-nomes.herokuapp.com/nome/aleatorio';

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const options = {
        method: 'GET',
        mode: 'no-cors',
        //headers: myHeaders,
    }

    fetch(url, options)
        .then(response => {
            return response.text()
        })
        .then((data) => {
            console.log(data) //console.log(data ? JSON.parse(data) : {})
        })
        .catch((error) => {
            console.log(error)
        })

}