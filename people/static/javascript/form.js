class Form {
    constructor() {
        this.form = document.querySelector('form');
        this.btn_get_name = document.querySelector(".btn-get-name");
        this.btn_submit = document.querySelector(".btn-submit");
        this.btn_delete = document.querySelector(".btn-delete");
        this.events();
    }

    events() {
        // chanding the type of input birth date
        document.querySelector("input[name='birth']").type = 'date';
        
        // event for add names in fields
        this.btn_get_name.addEventListener("click", e => {
            this.insertAleatorsNamesInFields();
        });

        if (this.btn_delete) {
            let id = this.btn_delete.dataset.id_person;
            this.btn_delete.addEventListener('click', e => {
                this.changeFormAction(e, `/delete/${id}/`);
            })
        }
    }

    insertAleatorsNamesInFields() {
        let name = document.getElementById('id_name');
        let lastName = document.getElementById('id_last_name');

        // getting the data from the request that my server has make and adding in the fields
        this.getNamesFromApi().then(data => {
            name.value = data[0];
            lastName.value = `${data[1]} ${data[2]}`;
        });
    }

    getNamesFromApi() {
        // this api does not is accessible from javascript
        let url2 = 'http://gerador-nomes.herokuapp.com/nome/aleatorio';

        // making request into my server and returning for the front end
        let url = 'http://127.0.0.1:8000/get-name/';
        return new Promise((resolve, reject) => {
            fetch(url)
                .then(res => {
                    return res.json();
                })
                .then(data => {
                    resolve(data);
                })
                .catch(error => reject(error));
        });

    }

    changeFormAction(event, path) {
        event.preventDefault();
        this.form.action = path;
        this.form.submit();
    }
}

let form = new Form();