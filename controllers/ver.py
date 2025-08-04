import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
from tabulate import tabulate # type: ignore

def verIngredientes():
    sc.limpiar_pantalla()
    ingredientes_data = cf.readJson(cfg.BD_INGREDIENTES)
    ingredientes = ingredientes_data.get("ingredientes", {})

    if not ingredientes:
        print("No hay ingredientes registrados.")
        sc.pausar_pantalla()
        return
    
    print("-------Ingredientes------")

    tabla = []
    headers = ["ID", "Nombre", "Descripcion", "Precio", "Stock"]
    for cod, ingrediente in ingredientes.items():
        tabla.append([
            cod,
            ingrediente.get("nombre", "N/A"),
            ingrediente.get("descripcion", "N/A"),
            ingrediente.get("precio", "N/A"),
            ingrediente.get("stock", "N/A")
        ])

    print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
    sc.pausar_pantalla()

def verCategorias():
    sc.limpiar_pantalla()
    categorias_data = cf.readJson(cfg.BD_CATEGORIAS)
    categorias = categorias_data.get("categorias", {})

    if not categorias:
        print("No hay categorias registradas.")
        sc.pausar_pantalla()
        return
    
    print("-------Categorias------")

    tabla = []
    headers = ["ID", "Nombre", "Descripcion"]
    for cod, categoria in categorias.items():
        tabla.append([
            cod,
            categoria.get("nombre", "N/A"),
            categoria.get("descripcion", "N/A"),
        ])

    print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
    sc.pausar_pantalla()

def verChef():
    sc.limpiar_pantalla()
    chefs_data = cf.readJson(cfg.BD_CHEFS)
    chefs = chefs_data.get("chef", {})

    if not chefs:
        print("No hay chefs registrados.")
        sc.pausar_pantalla()
        return
    
    print("-------Chefs------")

    tabla = []
    headers = ["ID", "Nombre", "Especialidad"]
    for cod, chef in chefs.items():
        tabla.append([
            cod,
            chef.get("nombre", "N/A"),
            chef.get("especialidad", "N/A")
        ])

    print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
    sc.pausar_pantalla()