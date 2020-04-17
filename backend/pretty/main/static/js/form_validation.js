//login_form validation (frontend validation)
const prompt=document.forms['login_form']['prompt'].value;
const password=document.forms['login_form']['password'].value;

const login_button=document.getElementById('login');

login_button.addEventListener('click',()=>{
    console.log(prompt);
    console.log(password);
    
    
});


//sign_up form validation (frontend)