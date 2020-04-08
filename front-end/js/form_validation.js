const login_button=document.getElementById('login');
const username=document.querySelector('#username');


alert(username.nodeName);;

login_button.addEventListener('click',()=>{
    login_button.innerText="Logging In ...";
    login_button.style.color="rgba(255, 255, 255, 0.664)";
});