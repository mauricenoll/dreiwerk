
function displayErrorMessage(msg){
    let errorMsgDiv = document.getElementById('error_msg');

    errorMsgDiv.innerHTML = msg;
    errorMsgDiv.style.display = "inline-block";
}

function showRequiredField(div_id){
    let error_msg_div = document.getElementById(div_id);

    error_msg_div.innerHTML = "Dieses Feld ist ein Pflichtfeld";

}

function resetErrorMsg(div_id){
    let error_msg_div = document.getElementById(div_id);

    error_msg_div.innerHTML = "";
}

async function sendMsg(){

    let form_ok = true;

    let url = window.location.href;

    document.body.style.cursor = "wait";

    let anrede = document.getElementById("anrede");
    let name = document.getElementById('name');
    let email = document.getElementById('email');
    let num = document.getElementById('number');
    let msg = document.getElementById('message');

    let business_name = document.getElementById('business');
    let branche = document.getElementById('branche');

    let budget = document.getElementById('budget');
    let interest = document.getElementById('sw_dev_type');

    let checkbox = document.getElementById('data-protection-checkbox');

    if(name.value === ""){
        showRequiredField('name_input_err');
        form_ok = false;
    }
    if(email.value === ""){
        showRequiredField('email_input_err');
        form_ok = false;
    }
    if(msg.value === ""){
        showRequiredField('msg_input_err');
        form_ok = false;
    }

    if(checkbox.checked === false){
        showRequiredField('checkbox_input_err');
        form_ok = false;
    }

    if(!form_ok){
        return;
    }

    const formData = new FormData();

    formData.append("anrede", anrede.value);
    formData.append("name", name.value);
    formData.append("email", email.value);
    formData.append("num", num.value);
    formData.append("msg", msg.value);
    formData.append("data_protection", checkbox.checked);
    formData.append("business", business_name.value);
    formData.append("branche", branche.value);
    formData.append('budget', budget.value);
    formData.append('interest', interest.value);


    try {
        const response = await fetch(`${url}`, {
            method: "POST",
            body: formData
        });
        let contact_form = document.getElementById('contact_form');
        let success_msg = document.getElementById('success_msg');

        if(response.status === 202){
            contact_form.style.display = "none";
            success_msg.style.display = "inline-block";
            console.log("request accepted");
        }else{
            displayErrorMessage("Etwas ist schief gelaufen, bitte versuche es später erneut!");
        }


    } catch (e){
        displayErrorMessage("Etwas ist schief gelaufen, bitte versuche es später erneut!");
        console.log(e);
    }

    document.body.style.cursor = "unset";




}