document.addEventListener("DOMContentLoaded", () =>{
    document.querySelector(".menu-toggle").addEventListener("click", event =>{
        document.querySelectorAll(".menu-toggle-item").forEach(item => {
            item.classList.toggle("clicked");
        })
        document.querySelector(".menu-nav").classList.toggle("clicked");
    })
})