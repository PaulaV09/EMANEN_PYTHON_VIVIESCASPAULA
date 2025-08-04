import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
from tabulate import tabulate # type: ignore

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

def buscarPorIDIngrediente():
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

    
def buscarIngredientePrecio():
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
        op = vd.validateInt("Selecciona una opción (1-5): ") - 1
        
        if op < 0 or op >= len(opcionesMenu): 
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue 
        
        match op:
            case 0:
                buscarIngredienteNombre()
                sc.limpiar_pantalla()
            case 1:
                buscarPorIDIngrediente()
                sc.limpiar_pantalla()
            case 2:
                buscarIngredientePrecio()
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

def buscarCategoriaNombre():
    sc.limpiar_pantalla()
    categorias_data = cf.readJson(cfg.BD_CATEGORIAS)

    if not (categorias_data):
        print("No hay categorias registradas.")
        sc.pausar_pantalla()
        return

    nombre_buscar = vd.validatetext("Ingrese el nombre de la categoria a buscar: ").title().strip()
    if not (nombre_buscar):
        print("ERROR: El nombre no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    encontrado = None 

    for categoria in categorias_data.get("categorias", {}).values():
        if (categoria.get("nombre", "").lower() == nombre_buscar.lower()):
            encontrado = categoria
            break 

    if (encontrado):
        print(f"\Categoria encontrada:")
        headers = ["ID", "Nombre", "Descripcion"]

        datos = [
            [
                encontrado.get('id'), 
                encontrado.get('nombre'), 
                encontrado.get('descripcion')
            ]
        ]        
        print(tabulate(datos, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"\nNo se encontró ninguna categoria con el nombre '{nombre_buscar}'.")
        
    sc.pausar_pantalla()
    return

def buscarPorIDCategoria():
    sc.limpiar_pantalla()
    categorias_data = cf.readJson(cfg.BD_CATEGORIAS)

    if not (categorias_data):
        print("No hay categorias registradas.")
        sc.pausar_pantalla()
        return
    
    siConoce = vd.validateBoolean("¿Conoce el ID de la categoria a buscar? (S/N): ")
    if not siConoce:
        buscarCategoriaNombre()
        return
    sc.limpiar_pantalla()
    
    id_buscar = vd.validate_string("Ingrese el ID del ingrediente a buscar: ").title().strip()
    if not (id_buscar):
        print("ERROR: El ID no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    encontrado = None 

    for categoria in categorias_data.get("categorias", {}).values():
        if (categoria.get("id", "").lower() == id_buscar.lower()):
            encontrado = categoria
            break 

    if (encontrado):
        print(f"\nCategoria encontrada:")
        headers = ["ID", "Nombre", "Descripcion"]

        datos = [
            [
                encontrado.get('id'), 
                encontrado.get('nombre'), 
                encontrado.get('descripcion')
            ]
        ]        
        print(tabulate(datos, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"\nNo se encontró ninguna categoria con el ID '{id_buscar}'.")
        
    sc.pausar_pantalla()
    return

def subSubMenuBuscarCategoria():
    opcionesMenu = ["Buscar por nombre","Buscar por ID", "Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("=====================================")
        print("         Buscar categorias           ")
        print("=====================================")
        print("¿Qué opcion desea realizar?")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Selecciona una opción (1-3): ") - 1
        
        if op < 0 or op >= len(opcionesMenu): 
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue 
        
        match op:
            case 0:
                buscarCategoriaNombre()
                sc.limpiar_pantalla()
            case 1:
                buscarPorIDCategoria()
                sc.limpiar_pantalla()
            case 2:
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")

def buscarChefNombre():
    sc.limpiar_pantalla()
    chef_data = cf.readJson(cfg.BD_CHEFS)

    if not (chef_data):
        print("No hay chefs registrados.")
        sc.pausar_pantalla()
        return

    nombre_buscar = vd.validatetext("Ingrese el nombre del chef a buscar: ").title().strip()
    if not (nombre_buscar):
        print("ERROR: El nombre no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    encontrado = None 

    for chef in chef_data.get("chefs", {}).values():
        if (chef.get("nombre", "").lower() == nombre_buscar.lower()):
            encontrado = chef
            break 

    if (encontrado):
        print(f"\nChef encontrado:")
        headers = ["ID", "Nombre", "Especialidad"]

        datos = [
            [
                encontrado.get('id'), 
                encontrado.get('nombre'), 
                encontrado.get('especialidad')
            ]
        ]        
        print(tabulate(datos, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"\nNo se encontró ningún chef con el nombre '{nombre_buscar}'.")
        
    sc.pausar_pantalla()
    return

def buscarPorIDChef():
    sc.limpiar_pantalla()
    chefs_data = cf.readJson(cfg.BD_CHEFS)

    if not (chefs_data):
        print("No hay chefs registrados.")
        sc.pausar_pantalla()
        return
    
    siConoce = vd.validateBoolean("¿Conoce el ID del chef a buscar? (S/N): ")
    if not siConoce:
        buscarChefNombre()
        return
    sc.limpiar_pantalla()
    
    id_buscar = vd.validatetext("Ingrese el ID del chef a buscar: ").title().strip()
    if not (id_buscar):
        print("ERROR: El ID no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    encontrado = None 

    for chef in chefs_data.get("chefs", {}).values():
        if (chef.get("id", "").lower() == id_buscar.lower()):
            encontrado = chef
            break 

    if (encontrado):
        print(f"\nChef encontrado:")
        headers = ["ID", "Nombre", "Especialidad"]

        datos = [
            [
                encontrado.get('id'), 
                encontrado.get('nombre'), 
                encontrado.get('especialidad')
            ]
        ]        
        print(tabulate(datos, headers=headers, tablefmt="fancy_grid"))
    else:
        print(f"\nNo se encontró ningún chef con el ID '{id_buscar}'.")
        
    sc.pausar_pantalla()
    return

def subSubMenuBuscarChef():
    opcionesMenu = ["Buscar por nombre","Buscar por ID", "Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("================================")
        print("         Buscar chefs           ")
        print("================================")
        print("¿Qué opcion desea realizar?")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Selecciona una opción (1-3): ") - 1
        
        if op < 0 or op >= len(opcionesMenu): 
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue 
        
        match op:
            case 0:
                buscarChefNombre()
                sc.limpiar_pantalla()
            case 1:
                buscarPorIDChef()
                sc.limpiar_pantalla()
            case 2:
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")