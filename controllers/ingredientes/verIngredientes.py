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