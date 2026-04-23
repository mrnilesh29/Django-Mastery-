document.getElementById("deleteForm").addEventListener("submit", function(e) {
    let confirmDelete = confirm("Are you absolutely sure? This action cannot be undone!");

    if (!confirmDelete) {
        e.preventDefault();
    }
});