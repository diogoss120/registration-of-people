
document.querySelectorAll(".person").forEach( person => {
    let person_id = person.dataset.id;
    console.log(person_id)
    person.addEventListener('click', e => {
        location.href = `/edit-person/${person_id}`;
        //location.href = `/`;
    });
});

document.querySelector(".btn-new-person").addEventListener("click", e => {
    location.href = `/`;
});