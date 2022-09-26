function controlSave(){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/panel/api/control/save', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            alert(response.message);

        } else {
            alert('Erro ao realizar chamada!');
        }
    }
    xhr.send(JSON.stringify({
        'link_buy': document.getElementsByName('link-buy')[0].value,
    }));
}

document.getElementsByClassName('btn-form-create')[0].addEventListener('click', controlSave)