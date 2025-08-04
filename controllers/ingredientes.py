import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg
from tabulate import tabulate # type: ignore

def anadirIngrediente():
    sc.limpiar_pantalla()
    ingredientes_data = cf.readJson(cfg.BD_INGREDIENTES)
    if not isinstance(ingredientes_data, dict) or 'ingredientes' not in ingredientes_data:
        ingredientes_data = {"ingredientes": {}}

    print("-> Añadir un nuevo ingrediente")
    nombre = vd.validate_string("Ingrese el nombre del ingrediente: ").title().strip()
    for ingrediente in ingredientes_data.get("ingredientes", {}).values():
        if ingrediente.get("nombre", "").lower() == nombre.lower():
            print(f"Error: El ingrediente con el nombre '{nombre}' ya está registrado.")
            sc.pausar_pantalla()
            return
    if not nombre:
        print("ERROR: El nombre del ingrediente no puede estar vacío.")
        sc.pausar_pantalla()
        return
    descripcion = vd.validatetext("Ingrese la descripcion del ingrediente: ").strip()
    if not descripcion:
        print("ERROR: La descripcion del ingrediente no puede estar vacía.")
        sc.pausar_pantalla()
        return
    precio = vd.validatefloat("Ingrese el precio del ingrediente: ")
    if precio < 0:
        print("ERROR: El precio del ingrediente debe ser superior a 0")
        sc.pausar_pantalla()
        return
    stock = vd.validatefloat("Ingrese el stock del ingrediente: ")
    if stock < 0:
        print("ERROR: El stock del ingrediente debe ser superior a 0")
        sc.pausar_pantalla()
        return
    
    if not ingredientes_data.get("ingredientes"):
        id_ingrediente = "1"
    else:
        max_id = max(int(k) for k in ingredientes_data["ingredientes"].keys())
        id_ingrediente = str(max_id + 1)

    nuevo_ingrediente = {
        "id": id_ingrediente,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "stock": stock
    }
    
    ingredientes_data["ingredientes"][id_ingrediente] = nuevo_ingrediente
    cf.writeJson(cfg.BD_INGREDIENTES, ingredientes_data)

    print(f"\nIngrediente '{nombre}' registrado con éxito con el ID: {id_ingrediente}")
    sc.pausar_pantalla()

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