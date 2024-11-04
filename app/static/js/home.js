

function toggleSelectedServiceSection(button){
    let buttons = document.getElementsByClassName('service-selection-btn');
    for (let i = 0; i < buttons.length; i++){
        buttons[i].style.background = "var(--primary)";
        buttons[i].style.boxShadow = "var(--standard-shadow)";
        buttons[i].style.color = "var(--text)";
    }

    let service_info_containers = document.getElementsByClassName('service-info-container');
    for (let i = 0; i < service_info_containers.length; i++){
        service_info_containers[i].style.display = "none";

    }

    let shown_service_info_container = document.getElementById(`${button.id}-container`);
    shown_service_info_container.style.display = "flex";

    button.style.background = "var(--dark-blue)";
    button.style.boxShadow = "var(--standard-accent-shadow)";
    button.style.color = "var(--white-text)";
}