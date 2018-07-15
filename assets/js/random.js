
function random() {
  // hay 1920 tiras
  var tiraNum = Math.floor(Math.random() * 1920) + 1;
  var numeroTira = convertirNumero(tiraNum);
  var list = document.getElementsByClassName("iis-slide")[0];
  var hola = document.getElementsByClassName("iis-current-slide")[0];
  hola.setAttribute('style', "transition-duration: 0ms; background-image: url(\"/TodaMafalda/historietas/" + numeroTira + ".png\");");
}

function convertirNumero(num) {
  var nString = num.toString();
  var len = nString.length;
  if (len != 4){
    for (var i = 0; i < 4-len ; i++){
      nString = '0'+nString;
    }
  }
  return nString
}
