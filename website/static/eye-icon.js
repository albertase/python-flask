// FOR PASSWORD
const password = document.querySelector('#password1');
const show_hide = document.querySelector('#show_hide');

const password2 = document.querySelector('#password2');
const show_hided = document.querySelector('#show_hided');

show_hide.onclick = function(){
    if(password.type == "password"){
        password.type = "text";
        show_hide.style.color = "green";
    }else{
        password.type = "password";
        show_hide.style.color = "red";
    }
}



show_hided.onclick = function(){
    if(password2.type === "password"){
        password2.type = "text";
        show_hided.style.color = "green";
    }else{
        password2.type = "password";
        show_hided.style.color = "red";
    }
}
