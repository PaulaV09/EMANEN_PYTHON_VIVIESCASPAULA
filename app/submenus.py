import os
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
import controllers.anadir as ca
import controllers.ver as cv
import controllers.buscar as cb
import controllers.editar as ce
import controllers.eliminar as cel

def gestion_ingredientes():
    opcionesMenu = ["Crear ingrediente","Ver ingredientes","Buscar ingrediente", "Editar ingrediente", "Eliminar ingrediente","Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("===========================================")
        print("         Gestion de ingredientes           ")
        print("===========================================")
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
                ca.anadirIngrediente()
                sc.limpiar_pantalla()
            case 1:
                cv.verIngredientes()
                sc.limpiar_pantalla()
            case 2:
                cb.subSubMenuBuscarIngrediente()
                sc.limpiar_pantalla()
            case 3:
                ce.editarIngrediente()
                sc.limpiar_pantalla()
            case 4:
                cel.subSubMenuEliminarIngrediente()
                sc.limpiar_pantalla()
            case 5:
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")

def gestion_categorias():
    opcionesMenu = ["Crear categoria","Ver categorias","Buscar categoria", "Editar categoria", "Eliminar categoria","Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("=========================================")
        print("         Gestion de categorias           ")
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
                ca.anadirCategoria()
                sc.limpiar_pantalla()
            case 1:
                cv.verCategorias()
                sc.limpiar_pantalla()
            case 2:
                cb.subSubMenuBuscarCategoria()
                sc.limpiar_pantalla()
            case 3:
                ce.editarCategoria()
                sc.limpiar_pantalla()
            case 4:
                cel.subSubMenuEliminarCategoria()
                sc.limpiar_pantalla()
            case 5:
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")

def gestion_chefs():
    opcionesMenu = ["Crear chef","Ver chefs","Buscar chef", "Editar chef", "Eliminar chef","Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("====================================")
        print("         Gestion de chefs           ")
        print("====================================")
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
                ca.anadirChef()
                sc.limpiar_pantalla()
            case 1:
                cv.verChef()
                sc.limpiar_pantalla()
            case 2:
                cb.subSubMenuBuscarChef()
                sc.limpiar_pantalla()
            case 3:
                ce.editarChef()
                sc.limpiar_pantalla()
            case 4:
                cel.subSubMenuEliminarChef()
                sc.limpiar_pantalla()
            case 5:
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")

def gestion_hamburguesas():
    opcionesMenu = ["Crear hamburguesa","Ver hamburguesas","Buscar hamburguesa", "Editar hamburguesa", "Eliminar hamburguesa","Regresar al menú principal"]
    while True: 
        sc.limpiar_pantalla()
        print("===========================================")
        print("         Gestion de hamburguesas           ")
        print("===========================================")
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
                ca.anadirHamburguesa()
                sc.limpiar_pantalla()
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                input("Presione Enter para continuar...")
                return 
            case _:
                print("Opción no implementada aún.")
                input("Presione Enter para continuar...")

