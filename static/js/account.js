function togglePassword() {
    const pwd = document.getElementById('password');
    const eye = document.getElementById('eye-icon');
    if (pwd.type === "password") {
        pwd.type = "text";
        eye.classList.remove('fa-eye');
        eye.classList.add('fa-eye-slash');
    } else {
        pwd.type = "password";
        eye.classList.remove('fa-eye-slash');
        eye.classList.add('fa-eye');
    }
}