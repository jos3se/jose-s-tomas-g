from proveedor import Proveedor
from producto import Productos
from venta import Ventas
print("--- ------------------------------------------------------------")
print("OPCIONES: ventas , proveedor, productos")
print("---------------------------------------------------------------")
eleccion = str(input("¿En que tabla queres trabajar? res: "))
match(eleccion):
    case "proveedor":
        print("---------------------------------------------------------------")
        print("OPCIONES: ingresar, leer,actualizar,eliminar")
        print("---------------------------------------------------------------")
        accion = str(input("¿Que accion queres realizar? res: "))
        print("---------------------------------------------------------------")
        match(accion):
            case "ingresar":
                nombre = str(input("Ingrese el nombre del proveedor: "))
                apellido = str(input("Ingrese el apellido del proveedor: "))
                empresa = str(input("Ingrese la empresa del proveedor: "))
                num_contacto = int(input("Ingrese el numero del proveedor: "))
                proveedor = Proveedor(nombre,apellido,empresa,num_contacto)
                proveedor.agregarProvedor()
            case "leer":
                proveedor = Proveedor()
                proveedor.leerProveedores()
            case "actualizar":
                nombre = str(input("Ingrese el nombre del proveedor: "))
                apellido = str(input("Ingrese el apellido del proveedor: "))
                empresa = str(input("Ingrese la empresa del proveedor: "))
                num_contacto = int(input("Ingrese el numero del proveedor: "))
                proveedor = Proveedor(nombre,apellido,empresa,num_contacto)
                proveedor.actualizarProveedores(1)
            case "eliminar":
                proveedor = Proveedor()
                proveedor.eliminarProveedor(1)
    case "productos":
        print("---------------------------------------------------------------")
        print("OPCIONES: ingresar, leer,actualizar,eliminar,monto,mostrar")
        print("---------------------------------------------------------------")
        accion = str(input("¿Que accion queres realizar? res: "))
        print("---------------------------------------------------------------")
        match(accion):
            case "ingresar":
                precio = int(input("ingrese el precio del producto: "))
                stock  =  int(input("ingrese el stock del producto: "))
                nombre  =  str(input("ingrese la nombre de producto: "))
                prov = Proveedor()
                prov.mostrarProvedores()
                id_proveedor = int(input("ingrese la id del proveedor que desees: "))
                producto = Productos(precio,stock,nombre,id_proveedor)
                producto.agregarProductos()
            case "leer":
                producto = Productos()
                producto.leerProductos()
            case "actualizar":
                 precio = int(input("ingrese el precio del producto: "))
                 stock  =  int(input("ingrese el stock del producto: "))
                 nombre  =  str(input("ingrese la nombre de producto: "))               
                 producto = Productos(precio,stock,nombre)
                 producto.actualizarProductos(1)
            case "eliminar":
                producto = Productos()
                producto.eliminarproducto(1)
            case "monto":
                producto = Productos()
                producto.mostrarMonto()
            case "mostrar":
                producto = Productos()
                producto.mostrarProductos()
    case "ventas":
        print("---------------------------------------------------------------")
        print("OPCIONES: ingresar, leer,actualizar,eliminar,mostrar")
        print("---------------------------------------------------------------")
        accion = str(input("¿Que accion queres realizar? res: "))
        print("---------------------------------------------------------------")
        match(accion):
            case "ingresar":
                metodo_pago = ""
                metodos_permitidos = ["transferencia","tarjeta","efectivo"]
                prod = Productos()
                prod.mostrarProductosDisponibles()
                id_producto = int(input("ingrese la id del producto quw se vendio: "))
                nombre = str(input("ingrese el nombre del producto: "))
                fecha = str(input("Ingrese la fecha correspondiente a la venta: "))
                metodo_pago = str(input("Ingrese cual fue el metodo de pago que fue utilizado en la venta: "))
                metodo_pago = metodo_pago.strip()
                if metodo_pago in metodos_permitidos:
                    cantidad_vendida = int(input("ingrese la cantidad de veces que se vendio el producto: "))
                    venta = Ventas(id_producto,nombre,fecha,metodo_pago,cantidad_vendida)
                    venta.restar_stock(id_producto,cantidad_vendida)
                    venta.agregarVentas()

                else:
                    print("ingrese el metodo de pago correctamente")
            case "leer":
                venta = Ventas()
                venta.leerVentas()
            case "actualizar":
                metodo_pago = ""
                metodos_permitidos = ["transferencia","tarjeta","efectivo"]
                prod = Productos()
                prod.mostrarProductosDisponibles()
                id_producto = int(input("ingrese la id del producto quw se vendio: "))
                nombre = str(input("ingrese el nombre del producto: "))
                fecha = str(input("Ingrese la fecha correspondiente a la venta: "))
                metodo_pago = str(input("Ingrese cual fue el metodo de pago que fue utilizado en la venta: "))
                metodo_pago = metodo_pago.strip()
                if metodo_pago in metodos_permitidos:
                    cantidad_vendida = int(input("ingrese la cantidad de veces que se vendio el producto"))
                    venta = Ventas()
                    venta.actualizarVentas(1)
                
            case "eliminar":
                venta = Ventas()
                venta.eliminarVenta(1)
            case "mostrar":
                venta = Ventas()
                venta.mostrar_vendidos()
                
        