const datos = window.location.search;
console.log(datos);

const parametros = new URLSearchParams(datos);

const nom = parametros.get('usuario')
document.getElementById(id = "usuario").innerHTML = nom
