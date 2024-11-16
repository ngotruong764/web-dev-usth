let signUpForm = document.getElementById('sign-up-form');
signUpForm.addEventListener('submit', e =>{
    e.preventDefault();
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const retypePass = document.getElementById('retype-pass');

    if(password.value !== retypePass.value){
        alert('Password !== retype pass');
    } else{
        alert('Create account successful');
    }
});
