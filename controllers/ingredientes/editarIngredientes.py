import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def editarIngrediente():
    sc.limpiar_pantalla()
    print("\n--- Ingredientes disponibles ---")
    data = cf.readJson(cfg.BD_INGREDIENTES)
    ingredientes = data.get("ingredientes", {})

    if not ingredientes:
        print("No hay ingredientes.")
        sc.pausar_pantalla()
        return

    for cod, ingrediente in ingredientes.items():
        print(f"{cod}: {ingrediente['nombre']}")

    id = input("Id del ingrediente a editar: ")

    if id not in ingredientes:
        print("Código no válido.")
        return
    
    ingrediente = ingredientes[id]
    sc.limpiar_pantalla()
    print("\n--- Datos actuales ---")
    for k, v in ingrediente.items():
        print(f"{k.capitalize()}: {v}")

    nombre = vd.validatetext("Nuevo nombre (enter para mantener): ").title().strip()
    descripcion = vd.validatetext("Nueva descripcion (enter para mantener): ").title().strip()
    precio = vd.validatefloat("Nuevo precio (enter para mantener): ")
    stock = vd.validateInt("Nuevo stock (enter para mantener")

    
    ingrediente["nombre"] = nombre or ingrediente["nombre"]
    ingrediente["descripcion"] = descripcion or ingrediente["descripcion"]
    ingrediente["precio"] = precio or ingrediente["precio"]
    ingrediente["stock"] = stock or ingrediente["stock"]

    ingredientes[id] = ingrediente
    data["ingredientes"] = ingredientes
    cf.writeJson(cfg.BD_INGREDIENTES, data)
    print("Ingrediente actualizado correctamente.")
    sc.pausar_pantalla()