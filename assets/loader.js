$(document).ready(function(){
    $('.modal').modal();
    $('.sidenav').sidenav();


})

function toggleModal(){
    var instance =M.Modal.getInstance($('#modal3'))
    instance.open();
}

//Navbar

const elemsDropdown = document.querySelectorAll(".dropdown-trigger");
const instancesDropdown = M.Dropdown.init(elemsDropdown, {
    coverTrigger: false
});

