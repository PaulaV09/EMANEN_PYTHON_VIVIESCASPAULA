import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
from tabulate import tabulate # type: ignore

def subSubMenuBuscarIngrediente ():
    opcionesMenu = ["Buscar por nombre","Buscar por ID","Buscar por precio", "Buscar por stock", "Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("=======================================")
        print("         Buscar ingredientes           ")
        print("=======================================")
        print("¿Qué opcion desea realizar?")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Selecciona una opción (1-6): ") - 1
        
        if op < 0 or op >= len(opcionesMenu): 
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue 
        
        match op:
            case 0:
                buscarIngredienteNombre()
                sc.limpiar_pantalla()
            case 1:
                buscarPorID()
                sc.limpiar_pantalla()
            case 2:
                buscarElementoPrecio()
                sc.limpiar_pantalla()
            case 3:
                buscarIngredienteStock()
                sc.limpiar_pantalla()
            case 4:
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")

def buscarIngredienteNombre():
    sc.limpiar_pantalla()
    ingredientes_data = cf.readJson(cfg.BD_INGREDIENTES)

    if not (ingredientes_data):
        print("No hay ingredientes registrados.")
        sc.pausar_pantalla()
        return

    nombre_buscar = vd.validatetext("Ingrese el nombre del ingrediente a buscar: ").title().strip()
    if not (nombre_buscar):
        print("ERROR: El nombre no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    encontrado = None 

    for ingrediente in ingredientes_data.get("ingredientes", {}).values():
        if (ingrediente.get("nombre", "").lower() == nombre_buscar.lower()):
            encontrado = ingrediente
            break 

    if (encontrado):
        print(f"\nIngrediente encontrado:")
        headers = ["ID", "Nombre", "Descripcion", "Precio", "Stock"]

        datos = [
            [
                encontrado.get('id'), 
                encontrado.get('nombre'), 
                encontrado.get('descripcion'), 
                encontrado.get('precio'), 
                encontrado.get('stock')
            ]
        ]        
        print(tabulate(datos, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"\nNo se encontró ningún ingrediente con el nombre '{nombre_buscar}'.")
        
    sc.pausar_pantalla()
    return

def buscarPorID():
    sc.limpiar_pantalla()
    ingredientes_data = cf.readJson(cfg.BD_INGREDIENTES)

    if not (ingredientes_data):
        print("No hay ingredientes registrados.")
        sc.pausar_pantalla()
        return
    
    siConoce = vd.validateBoolean("¿Conoce el ID del ingrediente a buscar? (S/N): ")
    if not siConoce:
        buscarIngredienteNombre()
        return
    sc.limpiar_pantalla()
    
    id_buscar = vd.validatetext("Ingrese el ID del ingrediente a buscar: ").title().strip()
    if not (id_buscar):
        print("ERROR: El ID no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    encontrado = None 

    for ingrediente in ingredientes_data.get("ingredientes", {}).values():
        if (ingrediente.get("id", "").lower() == id_buscar.lower()):
            encontrado = ingrediente
            break 

    if (encontrado):
        print(f"\nIngrediente encontrado:")
        headers = ["ID", "Nombre", "Descripcion", "Precio", "Stock"]

        datos = [
            [
                encontrado.get('id'), 
                encontrado.get('nombre'), 
                encontrado.get('descripcion'), 
                encontrado.get('precio'), 
                encontrado.get('stock')
            ]
        ]        
        print(tabulate(datos, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"\nNo se encontró ningún ingrediente con el ID '{id_buscar}'.")
        
    sc.pausar_pantalla()
    return

    

def buscarElementoPrecio():
    sc.limpiar_pantalla()
    ingredientes_data = cf.readJson(cfg.BD_INGREDIENTES)

    if not (ingredientes_data):
        print("No hay ingredientes registrados.")
        sc.pausar_pantalla()
        return
    
    precio_buscar = vd.validatefloat("Ingrese el precio del ingrediente(s) a buscar: ")
    if not (precio_buscar):
        print("ERROR: El precio no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    encontrado = []
    for ingrediente in ingredientes_data.get("ingredientes", {}).values():
        if (ingrediente.get("precio", "")== precio_buscar):
            encontrado.append(ingrediente)
    
    if (encontrado):
        print(f"\Ingredientes encontrados con el precio '{precio_buscar}':")
        headers = ["ID", "Nombre", "Descripcion", "Precio", "Stock"]

        datos_tabla = []
        for elem in encontrado:
            fila = [
                elem["id"],
                elem["nombre"],
                elem["descripcion"],
                elem["precio"],
                elem["stock"]
            ]
            datos_tabla.append(fila)
        
        print(tabulate(datos_tabla, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"No se encontró ningún ingrediente con el precio '{precio_buscar}'.")

    sc.pausar_pantalla()
    return

def buscarIngredienteStock():
    sc.limpiar_pantalla()
    ingredientes_data = cf.readJson(cfg.BD_INGREDIENTES)

    if not (ingredientes_data):
        print("No hay ingredientes registrados.")
        sc.pausar_pantalla()
        return
    
    stock_buscar = vd.validateInt("Ingrese el stock del ingrediente(s) a buscar: ")
    if not (stock_buscar):
        print("ERROR: El stock no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    encontrado = []
    for ingrediente in ingredientes_data.get("ingredientes", {}).values():
        if (ingrediente.get("stock", "")== stock_buscar):
            encontrado.append(ingrediente)
    
    if (encontrado):
        print(f"\Ingredientes encontrados con el stock '{stock_buscar}':")
        headers = ["ID", "Nombre", "Descripcion", "Precio", "Stock"]

        datos_tabla = []
        for elem in encontrado:
            fila = [
                elem["id"],
                elem["nombre"],
                elem["descripcion"],
                elem["precio"],
                elem["stock"]
            ]
            datos_tabla.append(fila)
        
        print(tabulate(datos_tabla, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"No se encontró ningún ingrediente con el stock '{stock_buscar}'.")

    sc.pausar_pantalla()
    return