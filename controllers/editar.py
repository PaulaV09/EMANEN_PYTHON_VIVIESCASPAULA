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

def editarCategoria():
    sc.limpiar_pantalla()
    print("\n--- Categorias disponibles ---")
    data = cf.readJson(cfg.BD_CATEGORIAS)
    categorias = data.get("categorias", {})

    if not categorias:
        print("No hay categorias.")
        sc.pausar_pantalla()
        return

    for cod, categoria in categorias.items():
        print(f"{cod}: {categoria['nombre']}")

    id = input("Id de la categoria a editar: ")

    if id not in categorias:
        print("Código no válido.")
        return
    
    categoria = categorias[id]
    sc.limpiar_pantalla()
    print("\n--- Datos actuales ---")
    for k, v in categoria.items():
        print(f"{k.capitalize()}: {v}")

    nombre = vd.validatetext("Nuevo nombre (enter para mantener): ").title().strip()
    descripcion = vd.validatetext("Nueva descripcion (enter para mantener): ").title().strip()
   
    categoria["nombre"] = nombre or categoria["nombre"]
    categoria["descripcion"] = descripcion or categoria["descripcion"]
    categorias[id] = categoria
    data["categorias"] = categorias
    cf.writeJson(cfg.BD_CATEGORIAS, data)
    print("Categoria actualizada correctamente.")
    sc.pausar_pantalla()

def editarChef():
    sc.limpiar_pantalla()
    print("\n--- Chefs disponibles ---")
    data = cf.readJson(cfg.BD_CHEFS)
    chefs = data.get("chefs", {})

    if not chefs:
        print("No hay chefs.")
        sc.pausar_pantalla()
        return

    for cod, chef in chefs.items():
        print(f"{cod}: {chef['nombre']}")

    id = input("Id del chef a editar: ")

    if id not in chefs:
        print("Código no válido.")
        return
    
    chef = chefs[id]
    sc.limpiar_pantalla()
    print("\n--- Datos actuales ---")
    for k, v in chef.items():
        print(f"{k.capitalize()}: {v}")

    nombre = vd.validatetext("Nuevo nombre (enter para mantener): ").title().strip()
    especialidad = vd.validatetext("Nueva especialidad (enter para mantener): ").title().strip()

    chef["nombre"] = nombre or chef["nombre"]
    chef["descripcion"] = especialidad or chef["descripcion"]

    chefs[id] = chef
    data["chefs"] = chefs
    cf.writeJson(cfg.BD_CHEFS, data)
    print("Chef actualizado correctamente.")
    sc.pausar_pantalla()