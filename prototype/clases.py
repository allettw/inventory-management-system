class Producto:
    def __init__(self, codigo, nombre, categoria, costo, precio, cantidad):
        self.codigo=codigo
        self.nombre=nombre
        self.categoria=categoria
        self.costo=costo
        self.precio=precio
        self.cantidad=cantidad
        
    def mostrar_informacion(self):
        print(f"INFORMACIÓN DEL PRODUCTO\nCódigo: {self.codigo}\nNombre: {self.nombre}\nCategoria: {self.categoria}\nCosto: ₡{self.costo}\nPrecio: ₡{self.precio}\nCantidad: {self.cantidad}\n")
        
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio>=0:
            self.precio=nuevo_precio
            print(f"Precio actualizado correctamente, nuevo precio: {self.precio}")
        else: print("Debe ingresar una cantidad mayor a cero.")
    
    def aumentar_stock(self, cantidad):
        if cantidad>0:
            self.cantidad+=cantidad
            print(f"Stock actualizado: {self.cantidad}")
        else: print("Debe ingresar una cantidad mayor a cero.")
    
    def disminuir_stock(self, cantidad):
        if cantidad>0 and cantidad<=self.cantidad:
            self.cantidad-=cantidad
            print(f"Stock actualizado: {self.cantidad}")
        else: print("Debe ingresar una cantidad mayor a cero.")
    
    def calcular_utilidad(self):
        utilidad=self.precio-self.costo
        return utilidad


class Inventario:
    def __init__(self):
        self.productos=[]
        self.historial_ventas=[]
    
    def agregar_producto(self, producto):
        if not self.buscar_producto(producto.codigo):
            self.productos.append(producto)
            print(f"Producto {producto.nombre} agregado exitosamente.")
        else:
            print(f"El producto {producto.nombre} ya se encuenta en el inventario.")
    
    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo==codigo:
                return producto
        return None
    
    def eliminar_producto(self, codigo):
        producto=self.buscar_producto(codigo)
        if producto!=None:
            self.productos.remove(producto)
            print(f"Producto eliminado exitosamente.")
        else:
            print(f"El producto no se encuentra en el inventario.")
            
    def mostrar_productos(self):
        if self.productos!=[]:
            for producto in self.productos:
                producto.mostrar_informacion()
        else:
            print("El inventario está vacío.")
    
    def buscar_por_categoria(self, categoria):
        productos_categoria=[]
        for producto in self.productos:
            if producto.categoria==categoria:
                productos_categoria.append(producto)
        return productos_categoria
        
    def mostrar_stock_bajo(self, limite):
        productos_stock_bajo=[]
        for producto in self.productos:
            if producto.cantidad<=limite:
                productos_stock_bajo.append(producto)
        return productos_stock_bajo
    
    def calcular_valor_inventario(self):
        valor=0
        for producto in self.productos:
            costo_total=producto.costo*producto.cantidad
            valor+=costo_total
        return valor
    
    def vender_producto(self, codigo, cantidad):
        producto=self.buscar_producto(codigo)
        if producto!=None:
            if cantidad>0 and cantidad<=producto.cantidad:
                producto.disminuir_stock(cantidad)
                total_venta=producto.precio*cantidad
                self.historial_ventas.append({"codigo":producto.codigo,
                                              "nombre":producto.nombre,
                                              "cantidad":cantidad,
                                              "precio":producto.precio,
                                              "total":total_venta
                                            })
                print(f"\nVENTA REALIZADA\nProducto: {producto.nombre}\nCantidad vendida: {cantidad}\nPrecio unitario: {producto.precio}\nTotal de venta: {total_venta}")
            else:
                print("La cantidad ingresada debe ser mayor a cero y no puede ser mayor al stock disponible.")
        else: print("El producto solicitado no se encuentra en el inventario.")
    
    def mostrar_historial(self):
        if self.historial_ventas!=[]:
            print("\nHISTORIAL DE VENTAS\n")
            for i in range(len(self.historial_ventas)):
                venta=self.historial_ventas[i]
                print(f"{i+1}.\nCodigo: {venta['codigo']}\nNombre: {venta['nombre']}\nCantidad: {venta['cantidad']}\nPrecio: {venta['precio']}\nTotal: {venta['total']}\n")
        else:
            print("No se han realizado ventas")
    
    def calcular_ingresos_totales(self):
        ingresos_totales=0
        if self.historial_ventas!=[]:
            for venta in self.historial_ventas:
                ingresos_totales+=venta["total"]
            return ingresos_totales
        else:
            return 0
    
    def producto_mayor_stock(self):
        cantidad_mayor=-1
        mayor_stock=[]
        if self.productos!=[]:
            for producto in self.productos:
                if producto.cantidad>cantidad_mayor:
                    cantidad_mayor=producto.cantidad
            for producto in self.productos:
                if producto.cantidad==cantidad_mayor:
                    mayor_stock.append(producto)
        return mayor_stock
    
    def producto_menor_stock(self):
        menor_stock=[]
        if self.productos!=[]:
            cantidad_menor=self.productos[0].cantidad
            for producto in self.productos:
                if producto.cantidad<cantidad_menor:
                    cantidad_menor=producto.cantidad
            for producto in self.productos:
                if producto.cantidad==cantidad_menor:
                    menor_stock.append(producto)
        return menor_stock
    
    def producto_mayor_utilidad(self):
        mayor_utilidad=[]
        if self.productos!=[]:
            utilidad_mayor=self.productos[0].calcular_utilidad()
            for producto in self.productos:
                if producto.calcular_utilidad()>utilidad_mayor:
                    utilidad_mayor=producto.calcular_utilidad()
            for producto in self.productos:
                if producto.calcular_utilidad()==utilidad_mayor:
                    mayor_utilidad.append(producto)
        return mayor_utilidad
    
    def total_productos(self):
        return len(self.productos)