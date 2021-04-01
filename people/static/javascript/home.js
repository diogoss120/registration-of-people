class Home {
    constructor() {
        this.inputSearch = document.querySelector('.input_search');
        this.events();
    }

    events() {

        document.querySelectorAll('.person').forEach(person => {
            let id = person.dataset.id;
            person.addEventListener('click', e => {
                location.href = `/edit-person/${id}`;
            });
        });

        document.querySelector('.btn-new-person').addEventListener('click', e => {
            location.href = `/`;
        });

        document.querySelectorAll('.birth').forEach(b => {
            let dateConverted = new Date(b.innerHTML).toLocaleDateString()
            b.innerHTML = dateConverted;
        })


        this.inputSearch.addEventListener('keypress', e => {
            let text = this.inputSearch.value;
            if (e.key === "Enter" && text != '') {
                location.href = `/search/${text}`;
            }
        })

        document.getElementById('btn_search').addEventListener('click', e => {
            let text = this.inputSearch.value;
            if (text != '') {
                location.href = `/search/${text}`;
            }
        });

    }
}

let home = new Home();