function clearDiv () {
    var div = document.getElementById('message');
    div.innerHTML = ""
}

function doRequest(url)
{
	if (url != null){
		if (window.ActiveXObject){
			httpRequest = new ActiveXobject("Microsoft.XMLHTTP");
		}else{
			httpRequest = new XMLHttpRequest();
		}
		httpRequest.open("GET", url, true);
		httpRequest.onprogress = function () {
            console.log('LOADING', httpRequest.status);
        };
        httpRequest.onload = function () {
            var code = httpRequest.status
            if (code == 200) {
                var p = document.getElementById('message');
                p.innerHTML += 'Sended successful command';
                myVar = setTimeout(clearDiv, 1000);
            }
            console.log('DONE', code);
        };
		httpRequest.send(null);
	}else{
		alert("Url je prazdne");
	}
}