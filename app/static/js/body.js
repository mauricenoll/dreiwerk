function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function navigate(path){
    window.open(path, '_top');
}

function toggleMobileNavigation(){

    let navMenu = document.getElementById('mobile_nav_menu');

    if(navMenu.style.display === "flex"){
        navMenu.style.display = "none";
    }else{
        navMenu.style.display = "flex";
    }
}


function closeMobileNavigation(){

     let navMenu = document.getElementById('mobile_nav_menu');
     navMenu.style.display = "none";
}

window.addEventListener('click', function(e){
  //   This is here, so you can click outside of navigation to close it
  if (document.getElementById('mobile_nav_menu').contains(e.target) || document.getElementById('open_nav_button').contains(e.target)){
    //   click inside the menu
  } else{
    closeMobileNavigation();
  }
});


function toggleDropdownNavigation(){
    let dropdownContent = document.getElementById('mobile_dropdown_content');
    let navBtnIcon = document.getElementById('nav_btn_icon');

    if (dropdownContent.style.display === "flex"){
        dropdownContent.style.display = "none";
        navBtnIcon.style.transform = "rotate(0deg)";
    }else{
        dropdownContent.style.display = "flex";
        navBtnIcon.style.transform = "rotate(180deg)";
    }
}