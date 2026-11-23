from clases import Producto, Inventario

def mostrar_menu():
    print("""
=================================
      SISTEMA DE INVENTARIO
=================================
1. Agregar producto
2. Buscar producto
3. Modificar precio
4. Aumentar existencias
5. Eliminar producto
6. Mostrar todos los productos
7. Mostrar productos con stock bajo
8. Realizar venta
9. Mostrar historial de ventas
10. Mostrar reportes
0. Salir\n
          """)

def mostrar_submenu_buscar():
    print("""
====== BUSCAR PRODUCTO ======

1. Buscar por código
2. Buscar por categoría
0. Volver al menú principal\n
          """)

def mostrar_submenu_reportes():
    print("""
========== REPORTES ==========

1. Valor total del inventario
2. Ingresos totales por ventas
3. Producto(s) con mayor stock
4. Producto(s) con menor stock
5. Producto(s) con mayor utilidad
0. Volver al menú principal\n
          """)

def main():
    inventario=Inventario()
    
    #Objetos de prueba
    inventario.agregar_producto(Producto("001","Bolsa de basura pequeña","Bolsas",800,1200,50))
    inventario.agregar_producto(Producto("002","Bolsa de basura mediana","Bolsas",1200,1800,35))
    inventario.agregar_producto(Producto("003","Bolsa de basura grande","Bolsas",1800,2500,20))
    inventario.agregar_producto(Producto("004","Desinfectante multiusos","Limpieza",1500,2200,40))
    inventario.agregar_producto(Producto("005","Cloro 1 litro","Limpieza",900,1400,60))
    inventario.agregar_producto(Producto("006","Detergente en polvo","Limpieza",2100,2900,15))
    inventario.agregar_producto(Producto("007","Jabón líquido","Limpieza",2500,3500,8))
    inventario.agregar_producto(Producto("008","Esponja multiusos","Accesorios",300,600,100))
    inventario.agregar_producto(Producto("009","Guantes de limpieza","Accesorios",700,1100,5))
    inventario.agregar_producto(Producto("010","Escoba","Accesorios",2500,3800,0))
    
    while True:
        mostrar_menu()
        try:
            opcion=int(input("Ingrese el número de opción que desea seleccionar: "))
            
            if opcion==1:
                while True:
                    codigo=input("Ingrese el código del producto: ")
                    nombre=input("Ingrese el nombre del producto: ")
                    categoria=input("Ingrese la categoría del producto: ")
                    try: #TODO evitar que el usuario deba ingresar todos los datos de nuevo si solo ingresó mal uno.
                        costo=float(input("Ingrese el costo del producto: "))
                        precio=float(input("Ingrese el precio de venta del producto: "))
                        cantidad=int(input("Ingrese la cantidad del producto: "))
                        if any([costo<0, precio<0, cantidad<0]):
                            raise ValueError
                        inventario.agregar_producto(Producto(codigo, nombre, categoria, costo, precio, cantidad))
                        break
                    except ValueError:
                        print("Debe ingresar únicamente valores númericos no negativos. Vuelva a intentarlo.")
                            
            elif opcion==2:
                while True:
                    mostrar_submenu_buscar()
                    try:
                        opcion_submenu=int(input("Ingrese el número de opción que desea seleccionar: "))
                        
                        if opcion_submenu==1:
                            print("\nBUSCAR POR CÓDIGO\n")
                            codigo=input("Ingrese el código del producto que desea buscar: ")
                            producto=inventario.buscar_producto(codigo)
                            if producto is None:
                                print("El código ingresado no corresponde a ningún producto en el inventario.")
                            else:
                                print(f"El código ingresado corresponde a: ")
                                producto.mostrar_informacion()
                        
                        elif opcion_submenu==2:
                            print("\nBUSCAR POR CATEGORÍA\n")
                            categoria=input("Ingrese la categoría que desea buscar: ")
                            productos=inventario.buscar_por_categoria(categoria)
                            if productos==[]:
                                print("No hay elementos de la categoría buscada registrados en el inventario.")
                            else:
                                print(f"Los productos de la categoría {categoria} son: ")
                                for producto in productos:
                                    producto.mostrar_informacion()
                                    
                        elif opcion_submenu==0:
                            print(f"Volviendo al menú principal...")
                            break
                        
                        else:
                            print("La opcion ingresada no corresponde a una opción válida. Vuelva a intentarlo.")
                            
                    except ValueError:
                        print("Debe ingresar únicamente el número de la opción que desea seleccionar. Vuelva a intentarlo.")
            
            elif opcion==3:
                codigo_producto=input("Ingrese el código del producto al que se le modificará el precio: ")
                try:
                    nuevo_precio=float(input("Ingrese el nuevo precio del producto: "))
                    producto=inventario.buscar_producto(codigo_producto)
                    if producto!=None:
                        producto.actualizar_precio(nuevo_precio)
                        producto.mostrar_informacion()
                    else:
                        print("El código ingresado no corresponde a ningún producto del inventario.")
                except ValueError:
                    print("Debe ingresar únicamente valores numéricos.")
                
            elif opcion==4:
                codigo_producto=input("Ingrese el código del producto al que se le añadirán existencias: ")
                try:
                    nueva_cantidad=int(input("Ingrese la cantidad de existencias que desea aumentar: "))
                    producto=inventario.buscar_producto(codigo_producto)
                    if producto!=None:
                        producto.aumentar_stock(nueva_cantidad)
                        producto.mostrar_informacion()
                    else:
                        print("El código ingresado no corresponde a ningún producto del inventario.")
                except ValueError:
                    print("Debe ingresar únicamente números enteros.")
            
            elif opcion==5:  #TODO volver atrás si se seleccionó por error esta opción
                flag=True
                while flag:
                    codigo_producto=input("Ingrese el código del producto que desea eliminar: ")
                    producto=inventario.buscar_producto(codigo_producto)
                    if producto is None:
                        print("El código ingresado no corresponde a ningún producto del inventario.")
                        continue
                    else: 
                        while True:
                            producto.mostrar_informacion()
                            eleccion=input("Ingrese 'S' si está seguro de eliminar el producto del inventario, 'N' en caso contrario: ")
                            if eleccion.upper()=="S":
                                inventario.eliminar_producto(codigo_producto)
                                print("INVENTARIO\n")
                                inventario.mostrar_productos()
                                flag=False
                                break
                            elif eleccion.upper()=="N":
                                flag=False
                                print("Eliminación cancelada.")
                                break
                            else:
                                continue
            
            elif opcion==6: 
                inventario.mostrar_productos()
            
            elif opcion==7: 
                try:
                    limite=int(input("Mostrar productos con existencias iguales o inferiores a: "))
                    if limite<0:
                        raise ValueError
                    productos_bajo_stock=inventario.mostrar_stock_bajo(limite)
                    if productos_bajo_stock!=[]:
                        for producto in productos_bajo_stock:
                            producto.mostrar_informacion()
                    else:
                        print("No hay productos con existencias menores o iguales al número ingresado.")
                except ValueError:
                    print("Debe ingresar únicamente números enteros no negativos.")
            
            elif opcion==8: 
                codigo_producto=input("Ingrese el código del producto que desea vender: ")
                try:
                    cantidad_venta=int(input("Ingrese la cantidad a vender: "))
                    inventario.vender_producto(codigo_producto, cantidad_venta)
                except ValueError:
                    print("Debe ingresar una cantidad expresada únicamente en valores enteros.")
            
            elif opcion==9:
                inventario.mostrar_historial()
            
            elif opcion==10:
                while True:
                    mostrar_submenu_reportes()
                    try:
                        opcion_submenu=int(input("Ingrese el número de opción que desea seleccionar: "))
                        
                        if opcion_submenu==1:
                            print(f"Valor total del inventario: ₡{inventario.calcular_valor_inventario()}")
                            
                        elif opcion_submenu==2:
                            print(f"Ingresos totales por ventas: ₡{inventario.calcular_ingresos_totales()}")
                            
                        elif opcion_submenu==3:
                            print(f"Producto(s) con mayor stock: \n")
                            productos=inventario.producto_mayor_stock()
                            if productos!=[]:
                                for producto in productos:
                                    producto.mostrar_informacion()
                            else:
                                print("No hay productos registrados.")
                        
                        elif opcion_submenu==4:
                            print(f"Producto(s) con menor stock: \n")
                            productos=inventario.producto_menor_stock()
                            if productos!=[]:
                                for producto in productos:
                                    producto.mostrar_informacion()
                            else:
                                print("No hay productos registrados.")
                        
                        elif opcion_submenu==5:
                            print(f"Producto(s) con mayor utilidad: \n")
                            productos=inventario.producto_mayor_utilidad()
                            if productos!=[]:
                                for producto in productos:
                                    producto.mostrar_informacion()
                                    print(f"Utilidad: ₡{producto.calcular_utilidad()}")
                            else:
                                print("No hay productos registrados.")
                        
                        elif opcion_submenu==0:
                            print("Volviendo al menú principal...")
                            break
                        
                        else:
                            print("La opcion ingresada no corresponde a una opción válida. Vuelva a intentarlo.")

                    except ValueError:
                        print("Debe ingresar únicamente el número de la opción que desea seleccionar. Vuelva a intentarlo.")
            
            elif opcion==0:
                print("Saliendo del sistema...")
                break
            else:
                print("El número ingresado no corresponde a ninguna opción. Vuelva a intentarlo.")
        except ValueError:
            print("Debe ingresar únicamente el número de la opción que desea seleccionar. Vuelva a intentarlo.")
        

main()