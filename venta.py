import sqlite3
conexion2 = sqlite3.connect("producto.db")
cursor2 = conexion2.cursor()
conexion = sqlite3.connect("ventas.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ventas (id_ventas INTEGER PRIMARY KEY AUTOINCREMENT ,id_producto INTEGER,nombre TEXT,  fecha TEXT , metodo_pago TEXT,cantidad_vendida INTEGER,FOREIGN KEY (id_producto) REFERENCES producto (id_producto))")
class Ventas:
    def __init__(self,id_producto = 0,nombre = "",fecha = "", metodo_pago = "",cantidad_vendida = 0 ) -> None:
        self.id_producto = id_producto
        self.nombre = nombre
        self.fecha = fecha
        self.metodo_pago = metodo_pago
        self.cantidad_vendida = cantidad_vendida
    def agregarVentas(self):
        cursor.execute(f"INSERT INTO ventas(id_producto,nombre,fecha,metodo_pago,cantidad_vendida)VALUES('{self.id_producto}','{self.nombre}','{self.fecha}','{self.metodo_pago}','{self.cantidad_vendida}')")
        conexion.commit()
        conexion.close()
    def leerVentas(self):
        ventas = cursor.execute("SELECT * FROM ventas")
        resultado =ventas.fetchall()
        for item in resultado:
            print(item)
    def actualizarVentas(self,id_ventas):
        cursor.execute(f'''UPDATE ventas SET id_producto= "{self.id_producto},"nombre = "{self.nombre}" , fecha = "{self.fecha}"  , metodo_pago = "{self.metodo_pago} , cantidad_vendida = "{self.cantidad_vendida}"  WHERE id_ventas = "{id_ventas}"''')
        conexion.commit()
        conexion.close()
    def eliminarVenta(self,id_ventas):
        cursor.execute(f'''DELETE FROM ventas WHERE "{id_ventas}" ''')
        conexion.commit()
        conexion.close()
    def mostrar_vendidos(self):
            cursor = conexion.cursor()
            resultado = '''SELECT * FROM ventas ORDER BY id_ventas DESC LIMIT 5;'''
            cursor.execute(resultado)
            ultimas_ventas = cursor.fetchall()
            for item in ultimas_ventas:
                print(item)
    def restar_stock(self,id_producto, cantidad_vendida):
        print(type(id_producto))
        resultado = '''SELECT stock FROM productos WHERE id_producto = ?;'''
        cursor2.execute(resultado, (id_producto,))
        resultado = cursor2.fetchone()
        if resultado:
            stock_actual = int(resultado[0])
            if stock_actual >= cantidad_vendida:
                nuevo_stock = stock_actual - cantidad_vendida
                actualizar = '''UPDATE productos SET stock = ? WHERE id_producto = ?'''
                cursor2.execute(actualizar, (nuevo_stock, id_producto))
                conexion2.commit()
                productos = cursor2.execute("SELECT * FROM productos ")
                resultado =productos.fetchall()
                for item in resultado:
                    print(item)
 
