import sqlite3
conexion = sqlite3.connect("proveedor.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS proveedor(id_proveedor  INTEGER PRIMARY KEY AUTOINCREMENT , nombre TEXT, apellido TEXT , empresa TEXT, num_contacto INTEGER)")
class Proveedor:
    def __init__(self,nombre = "",apellido = "",empresa = "",num_contacto = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.empresa = empresa
        self.num_contacto = num_contacto       
    def agregarProvedor(self):
        cursor.execute(f"INSERT INTO proveedor(nombre, apellido,empresa,num_contacto)VALUES('{self.nombre}','{self.apellido}','{self.empresa}','{self.num_contacto}')")
        conexion.commit()
        conexion.close()
    def leerProveedores(self):
        prov = cursor.execute("SELECT * FROM proveedor ")
        resultado =prov.fetchall()
        for item in resultado:
            print(item)
    def actualizarProveedores(self,id_proveedor):
        cursor.execute(f'''UPDATE proveedor SET nombre = "{self.nombre}" , apellido = "{self.apellido}" , empresa = "{self.empresa}" , num_contacto = "{self.num_contacto}"  WHERE id_proveedor = "{id_proveedor}"''')
        conexion.commit()
        conexion.close()
    def eliminarProveedor(self,id_proveedor):
        cursor.execute(f'''DELETE FROM proveedor WHERE "{id_proveedor}" ''')
        conexion.commit()
        conexion.close()
    def mostrarProvedores(self):
        prov = cursor.execute("SELECT id_proveedor,nombre,empresa FROM proveedor ")
        resultado = prov.fetchall()
        for item in resultado:
            print(item)