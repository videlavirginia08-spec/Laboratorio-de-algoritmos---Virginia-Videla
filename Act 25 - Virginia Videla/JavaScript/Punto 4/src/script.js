/*4-
Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
hardware.
 Crear una lista donde cada elemento sea una tupla de tres elementos que
represente: (nombre_articulo, precio, stock).
Desarrollar las siguientes funciones:
1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
armar las tuplas correspondientes.
2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
artículos desempaquetando la tupla de manera directa en el bucle for.
3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
(sumando el resultado de precio * stock de cada uno de los componentes).
4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
sea menor o igual a 10 unidades para emitir un aviso de compra urgente.*/


function cargar()
{
    let inventario = [];
    for(let i=0; i<5; i++)
    {
        console.log("Componente" + (i+1));
        let nombre = prompt("Escriba el nombre del artículo: ");
        let precio = parseFloat(prompt("Escriba el precio: "));
        let stock = Number(prompt("Escriba el stock: "));

        let articulo = [nombre, precio, stock];
        inventario.push(articulo);
    }
    return inventario;
}


function listado(inventario)
{
    console.log("Listado de articulos: ");
    for(let[nombre, precio, stock] of inventario)
    {
        console.log("Articulo: " + nombre);
        console.log("Precio: " + precio);
        console.log("Stock: " + stock);
    }
}

function inventario(inventario)
{
    let total = 0;
    for(let [nombre, precio, stock] of inventario)
    {
        total += precio* stock;
    }
    console.log("Valor total del inventario: " + total);
}

function alerta(inventario)
{
    console.log("Articulos que necesitan reposicion: ");
    for(let [nombre, precio, stock] of inventario)
    {
        if(stock<=10)
        {
            console.log("Comprar urgentemente: " + nombre);
        }
    }
}

let inventario = cargar();
listado(inventario);
inventario(inventario);
alerta(inventario);