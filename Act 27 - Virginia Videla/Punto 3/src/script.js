/*3. Disponer dos campos de texto tipo password. Cuando se presione un
botón mostrar si las dos claves ingresadas son iguales o no (es muy
común solicitar al operador el ingreso de dos veces de su clave para
validar si las escribió correctamente, esto se hace cuando se crea una
password para el ingreso a un sitio o para el cambio de una existente).
Tener en cuenta que podemos emplear el operador == para ver si dos
string son iguales.*/

function verificar()
{
    let p1 = document.getElementById("p1").value;
    let p2 = document.getElementById("p2").value;
    let texto = document.getElementById("texto");
    
    if(p1 == p2)
    {
        texto.textContent = "Se confirmo su contraseña";
        texto.style.color = "green";
    }
    else
    {
        texto.textContent = "Las contraseñas no son iguales"
        texto.style.color = "red";
    }
}