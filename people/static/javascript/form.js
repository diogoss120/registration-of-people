class Form {
    constructor() {
        this.form = document.querySelector('form');
        this.btn_get_name = document.querySelector(".btn-get-name");
        this.btn_submit = document.querySelector(".btn-submit");
        this.btn_delete = document.querySelector(".btn-delete");
        this.events();
    }

    events() {
        document.querySelector("textarea[name='obervation']").required = false;
        document.querySelector("input[name='nickname']").required = false;
        document.querySelector("input[name='birth']").type = 'date';

        if (this.btn_get_name) {
            this.btn_get_name.addEventListener("click", e => {
                this.changeFormAction(e, '/get-name/');
            });

            this.btn_submit.addEventListener("click", e => {
                this.changeFormAction(e, '/');
            });
        }

        if (this.btn_delete) {
            let id = this.btn_delete.dataset.id_person;
            this.btn_delete.addEventListener('click', e => {
                location.href = `/delete/${id}`;
            })
        }
    }
    changeFormAction(event, path) {
        event.preventDefault();
        this.form.action = path;
        this.form.submit();
    }
}

let form = new Form();