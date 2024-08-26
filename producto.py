import sqlite3
conexion = sqlite3.connect("producto.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS productos(id_producto INTEGER PRIMARY KEY AUTOINCREMENT, precio INTEGER,stock INTEGER,nombre TEXT,id_proveedor INTEGER,FOREIGN KEY (id_proveedor) REFERENCES proveedor (id_proveedor))")
class Productos:
    def __init__(self, precio = 0, stock = 0, nombre = "",id_proveedor = 0) -> None:
        self.precio = precio
        self.stock = stock
        self.nombre = nombre
        self.id_proveedor = id_proveedor
    def agregarProductos(self):
        cursor.execute(f"INSERT INTO productos(precio,stock,nombre,id_proveedor)VALUES('{self.precio}','{self.stock}','{self.nombre}','{self.id_proveedor}')")
        conexion.commit()
        conexion.close()
    def leerProductos(self):
        productos = cursor.execute("SELECT * FROM productos ")
        resultado =productos.fetchall()
        for item in resultado:
            print(item)
    def actualizarProductos(self,id_producto):
        cursor.execute(f'''UPDATE productos SET precio = "{self.precio}" , stock = "{self.stock}" , nombre = "{self.nombre}" ,id_proveedor = "{self.id_proveedor}" WHERE id_producto = "{id_producto}"''')
        conexion.commit()
        conexion.close()
    def eliminarproducto(self,id_producto):
        cursor.execute(f'''DELETE FROM productos WHERE "{id_producto}" ''')
        conexion.commit()
        conexion.close()
    def mostrarMonto(self):
        res = cursor.execute( '''SELECT SUM(precio) FROM productos;''')
        resultado = res.fetchall()
        resul = cursor.execute('''SELECT SUM(stock)FROM productos;''')
        resultado2 = resul.fetchall()
        monto = resultado[0][0] * resultado2[0][0]
        monto = monto / 2
        print(monto)
    
    def mostrarProductos(self):
        productos = cursor.execute("SELECT * FROM productos where stock>=10 ")
        resultado =productos.fetchall()
        for item in resultado:
            print(item)
    def mostrarProductosDisponibles(self):
        prod = cursor.execute("SELECT id_producto,precio,stock,nombre FROM productos  ")
        resultado = prod.fetchall()
        for item in resultado:
            print(item)

