document.addEventListener("DOMContentLoaded", () => {
    /* get the about section content from server */
    const aboutSelect = document.getElementById("about");
    aboutSelect.addEventListener("click", () => {
        fetch("/about")
            .then(res => res.text())
            .then(html => {
                document.getElementById("main-content-div").innerHTML = html;
            })
            .catch(err => {
                alert(err);
            });
    });
    
    /* get the games selection content from server */
    const gameSelect = document.getElementById("games");
    gameSelect.addEventListener("click", () => {
        fetch("/games")
            .then(res => res.text())
            .then(html => {
                document.getElementById("main-content-div").innerHTML = html;
                attachGameSelectionListeners();
            })
            .catch(err => {
                alert(err);
            });
    });
})

function attachGameSelectionListeners() {
    document.querySelectorAll("#game").forEach(div => {
        div.addEventListener("click", () => {
            const id = div.dataset.id;

            fetch(`/games/${id}`, {
                method: "POST",
                headers: { "Content-Type": "application/json" }
            })
                .then(res => res.text())
                .then(html => {
                    document.getElementById("main-content-div").innerHTML = html;
                })
                .catch(err => {
                    alert(err);
                });
        });
    });
}

