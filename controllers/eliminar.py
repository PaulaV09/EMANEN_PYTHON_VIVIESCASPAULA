import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def eliminarPorNombreIngrediente():
    sc.limpiar_pantalla()
    ingredientes_data = cf.readJson(cfg.BD_INGREDIENTES)

    if not (ingredientes_data):
        print("No hay ingredientes registrados.")
        sc.pausar_pantalla()
        return
    
    nombre_buscar = vd.validatetext("Ingrese el nombre del ingrediente a eliminar: ").title().strip()
    if not nombre_buscar:
        print("ERROR: El nombre no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    eliminado = False
    for ingrediente in ingredientes_data.get("ingredientes", {}).values():
        if ingrediente.get("nombre", "").lower() == nombre_buscar.lower():
            elemento_id = ingrediente['id']
            del ingredientes_data["ingredientes"][elemento_id]
            cf.writeJson(cfg.BD_INGREDIENTES, ingredientes_data)
            print(f"Ingrediente '{nombre_buscar}' eliminado con éxito.")
            eliminado = True
            break 

    if not eliminado:
        print(f"No se encontró ningún ingrediente con el nombre '{nombre_buscar}'.")
        
    sc.pausar_pantalla()
    return

def eliminarPorIDIngrediente():
    sc.limpiar_pantalla()
    ingredientes_data = cf.readJson(cfg.BD_INGREDIENTES)

    if not (ingredientes_data):
        print("No hay ingredientes registrados.")
        sc.pausar_pantalla()
        return
    
    siConoce = vd.validateBoolean("¿Conoce el ID del ingrediente a eliminar? (S/N): ")
    if not siConoce:
        eliminarPorNombreIngrediente()
        return
    sc.limpiar_pantalla()
    
    if not ingredientes_data.get("ingredientes"):
        print("No hay ingredientes registrados.")
        sc.pausar_pantalla()
        return
    id_buscar = vd.validatetext("Ingrese el ID del ingrediente a eliminar: ").strip()
    if not id_buscar:
        print("ERROR: El ID no puede estar vacío.")
        sc.pausar_pantalla()
        return
        
    eliminado = False

    for ingrediente in ingredientes_data.get("ingredientes", {}).values():
        if ingrediente.get("id", "") == id_buscar:
            elemento_id = ingrediente['id']
            del ingredientes_data["ingredientes"][elemento_id]
            cf.writeJson(cfg.BD_INGREDIENTES, ingredientes_data)
            print(f"Ingrediente con ID '{id_buscar}' eliminado con éxito.")
            eliminado = True
            break

    if not eliminado:
        print(f"No se encontró ningún ingrediente con el ID '{id_buscar}'.")

    sc.pausar_pantalla()
    return

def subSubMenuEliminarIngrediente():
    opcionesMenu = ["Eliminar por ID","Eliminar por nombre", "Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("=========================================")
        print("         Eliminar ingredientes           ")
        print("=========================================")
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
                eliminarPorIDIngrediente()
                sc.limpiar_pantalla()
            case 1:
                eliminarPorNombreIngrediente()
                sc.limpiar_pantalla()
            case 2:
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")

def eliminarPorNombreCategoria():
    sc.limpiar_pantalla()
    categorias_data = cf.readJson(cfg.BD_CATEGORIAS)

    if not (categorias_data):
        print("No hay categorias registradas.")
        sc.pausar_pantalla()
        return
    
    nombre_buscar = vd.validatetext("Ingrese el nombre de la categoria a eliminar: ").title().strip()
    if not nombre_buscar:
        print("ERROR: El nombre no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    eliminado = False
    for categoria in categorias_data.get("categorias", {}).values():
        if categoria.get("nombre", "").lower() == nombre_buscar.lower():
            elemento_id = categoria['id']
            del categorias_data["categorias"][elemento_id]
            cf.writeJson(cfg.BD_CATEGORIAS, categorias_data)
            print(f"Categoria '{nombre_buscar}' eliminada con éxito.")
            eliminado = True
            break 

    if not eliminado:
        print(f"No se encontró ninguna categoria con el nombre '{nombre_buscar}'.")
        
    sc.pausar_pantalla()
    return

def eliminarPorIDCategoria():
    sc.limpiar_pantalla()
    categorias_data = cf.readJson(cfg.BD_CATEGORIAS)

    if not (categorias_data):
        print("No hay categorias registradas.")
        sc.pausar_pantalla()
        return
    
    siConoce = vd.validateBoolean("¿Conoce el ID de la categoria a eliminar? (S/N): ")
    if not siConoce:
        eliminarPorNombreCategoria()
        return
    sc.limpiar_pantalla()
    
    if not categorias_data.get("categorias"):
        print("No hay categorias registradas.")
        sc.pausar_pantalla()
        return
    id_buscar = vd.validatetext("Ingrese el ID de la categoria a eliminar: ").strip()
    if not id_buscar:
        print("ERROR: El ID no puede estar vacío.")
        sc.pausar_pantalla()
        return
        
    eliminado = False

    for categoria in categorias_data.get("categorias", {}).values():
        if categoria.get("id", "") == id_buscar:
            elemento_id = categoria['id']
            del categorias_data["categorias"][elemento_id]
            cf.writeJson(cfg.BD_CATEGORIAS, categorias_data)
            print(f"Categoria con ID '{id_buscar}' eliminada con éxito.")
            eliminado = True
            break

    if not eliminado:
        print(f"No se encontró ninguna categoria con el ID '{id_buscar}'.")

    sc.pausar_pantalla()
    return

def subSubMenuEliminarCategoria():
    opcionesMenu = ["Eliminar por ID","Eliminar por nombre", "Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("======================================")
        print("         Eliminar categoria           ")
        print("======================================")
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
                eliminarPorIDCategoria()
                sc.limpiar_pantalla()
            case 1:
                eliminarPorNombreCategoria()
                sc.limpiar_pantalla()
            case 2:
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")