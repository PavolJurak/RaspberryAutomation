function doRequest(url)
{
	if (url != null){
		if (window.ActiveXObject){
			httpRequest = new ActiveXobject("Microsoft.XMLHTTP");
		}else{
			httpRequest = new XMLHttpRequest();
		}
		httpRequest.open("GET", url, true);
		httpRequest.send(null);
	}else{
		alert("Url je prazdne");
	}
}