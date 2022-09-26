function login(){
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var data = {
        'email': email,
        'password': password
    };
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/login', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if(response.status){
                window.location.href = '/';
            }else{
                alert(response.message);
            }
        } else {
            alert('Erro ao realizar chamada!');
        }
    }
    xhr.send(JSON.stringify(data));
}

document.getElementsByClassName('btn-signin')[0].addEventListener('click', login);
document.getElementById('password').addEventListener('keydown', function(e){
    if(e.key === "Enter"){
        login();
    }
});