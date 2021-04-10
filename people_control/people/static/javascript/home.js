class Home {
    constructor() {
        this.inputSearch = document.querySelector('.input_search');
        this.events();
    }

    events() {
        // event for redirect to page of the person
        document.querySelectorAll('.person').forEach(person => {
            let id = person.dataset.id;
            person.addEventListener('click', e => {
                location.href = `/edit-person/${id}`;
            });
        });

        // event for redirect to the page of register new person
        document.querySelector('.btn-new-person').addEventListener('click', e => {
            location.href = `/`;
        });

        // update in front end the birth date of the person
        document.querySelectorAll('.birth').forEach(b => {
            let dateConverted = new Date(b.innerHTML).toLocaleDateString()
            b.innerHTML = dateConverted;
        })

        // event for make search when press Enter key
        this.inputSearch.addEventListener('keypress', e => {
            let text = this.inputSearch.value;
            if (e.key === "Enter" && text != '') {
                location.href = `/search/${text}`;
            } else if (e.key === "Enter" && text == ''){
                location.href = `/people`;
            }
        })

        // event for make search when press button search
        document.getElementById('btn_search').addEventListener('click', e => {
            let text = this.inputSearch.value;
            if (text != '') {
                location.href = `/search/${text}`;
            } else {
                location.href = `/people`;
            }
        });

    }
}

let home = new Home();