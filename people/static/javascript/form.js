document.querySelector("input[name='obervation']").required = false;
document.querySelector("input[name='nickname']").required = false;

document.querySelector(".btn-alert").addEventListener("click", e => {

    let form = document.querySelector('form');
    e.preventDefault();
    form.action = '/get_name/';
    form.submit();

});

document.querySelector(".btn-submit").addEventListener("click", e => {

    let form = document.querySelector('form');
    e.preventDefault();
    form.action = '/';
    form.submit();

});


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