import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
from tabulate import tabulate # type: ignore

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

def buscarPorID():
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
                buscarPorID()
                sc.limpiar_pantalla()
            case 2:
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")