import os
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
import app.submenus as sm

opcionesMenu = ['Gestionar ingredientes', 'Gestionar categorias', 'Gestionar chefs', 'Gestionar hamburguesas', 'Reportes', 'Salir']

def main_menu() -> None:
    while True: 
        sc.limpiar_pantalla()
        print("=========================================================")
        print("         GESTION DE INVENTARIO DE HAMBURGUESERIA         ")
        print("=========================================================")
        print("-> Bienvenido al Menú Principal del sistema <-")
        for i, opcion in enumerate(opcionesMenu, start=1):
            print(f"{i}. {opcion}")
        op = vd.validateInt("Seleccione una opción: ") - 1
        
        if op < 0 or op >= len(opcionesMenu): 
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue 
        
        match op:
            case 0:
                sm.gestion_ingredientes()
            case 1:
                sm.gestion_categorias()
            case 2:
                sm.gestion_chefs()
            case 3:
                sm.gestion_hamburguesas()
            case 4:
                pass
            case 5:
                print("Saliendo del programa...")
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")
        