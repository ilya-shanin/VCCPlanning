document.addEventListener("DOMContentLoaded", function(event) {
   
    const showNavbar = (toggleId, sidebarId, bodyId, headerId, headTgId) =>{
        const toggle = document.getElementById(toggleId),
        nav = document.getElementById(sidebarId),
        bodypd = document.getElementById(bodyId),
        headerpd = document.getElementById(headerId),
        head_toggle = document.getElementById(headTgId)
    
        // Validate that all variables exist
        if(toggle && nav && bodypd && headerpd && head_toggle){
            toggle.addEventListener('click', ()=>{
                // show navbar
                nav.classList.toggle('show')
                // change icon
                toggle.classList.toggle('bx-right-arrow-alt')
                toggle.classList.toggle('bx-left-arrow-alt')
                // add padding to body
                bodypd.classList.toggle('body-pd')
                // add padding to header
                headerpd.classList.toggle('body-pd')
                head_toggle.classList.toggle('bx-x')
            })
            head_toggle.addEventListener('click', ()=>{
                // show navbar
                nav.classList.toggle('show')
                // change icon
                toggle.classList.toggle('bx-right-arrow-alt')
                toggle.classList.toggle('bx-left-arrow-alt')
                // add padding to body
                bodypd.classList.toggle('body-pd')
                // add padding to header
                headerpd.classList.toggle('body-pd')
                head_toggle.classList.toggle('bx-x')
            })
        }
    }
    
    showNavbar('toggle_sidebar','sidebar','body','header','htg-sidebar')
    
});