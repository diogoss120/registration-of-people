
document.querySelectorAll(".person").forEach( person => {
    let person_id = person.dataset.id;
    person.addEventListener('click', e => {
        location.href = `/edit-person/${person_id}`;
    });
});

document.querySelector(".btn-new-person").addEventListener("click", e => {
    location.href = `/`;
});