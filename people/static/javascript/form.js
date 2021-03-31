document.querySelector("textarea[name='obervation']").required = false;
document.querySelector("input[name='nickname']").required = false;

let form = document.querySelector('form');

let btn_get_name = document.querySelector(".btn-get-name")
let btn_submit = document.querySelector(".btn-submit");

if (btn_get_name) {
    btn_get_name.addEventListener("click", e => {
        
        e.preventDefault();
        form.action = '/get-name/';
        form.submit();

    });

    if (btn_submit) {
        btn_submit.addEventListener("click", e => {
            
            e.preventDefault();
            form.action = 'http://127.0.0.1:8000/';
            form.submit();
            
        });
    }
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