document.addEventListener("DOMContentLoaded", function() {
    const menuicn = document.getElementById("menuicn");
    const nav = document.querySelector(".navcontainer");
    if (menuicn && nav) {
        menuicn.addEventListener("click", () => {
            nav.classList.toggle("navclose");
        });
    }

    // Mini menu usuário
    const userMenu = document.getElementById("userMenu");
    if (userMenu) {
        userMenu.addEventListener("click", function(e) {
            e.stopPropagation();
            userMenu.classList.toggle("active");
        });
        document.addEventListener("click", function() {
            userMenu.classList.remove("active");
        });
    }
});