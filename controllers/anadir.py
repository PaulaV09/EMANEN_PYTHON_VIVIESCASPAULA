import utils.corefiles as cf
import utils.screenControllers as sc
import utils.validateData as vd
import config as cfg

def anadirIngrediente():
    sc.limpiar_pantalla()
    ingredientes_data = cf.readJson(cfg.BD_INGREDIENTES)
    if not isinstance(ingredientes_data, dict) or 'ingredientes' not in ingredientes_data:
        ingredientes_data = {"ingredientes": {}}

    print("-> Añadir un nuevo ingrediente")
    nombre = vd.validatetext("Ingrese el nombre del ingrediente: ").title().strip()
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

def anadirCategoria():
    sc.limpiar_pantalla()
    categorias_data = cf.readJson(cfg.BD_CATEGORIAS)
    if not isinstance(categorias_data, dict) or 'categorias' not in categorias_data:
        categorias_data = {"categorias": {}}

    print("-> Añadir un nueva categoria")
    nombre = vd.validatetext("Ingrese el nombre de la categoria: ").title().strip()
    for categoria in categorias_data.get("categorias", {}).values():
        if categoria.get("nombre", "").lower() == nombre.lower():
            print(f"Error: La categoria con el nombre '{nombre}' ya está registrada.")
            sc.pausar_pantalla()
            return
    if not nombre:
        print("ERROR: El nombre de la categoria no puede estar vacío.")
        sc.pausar_pantalla()
        return
    descripcion = vd.validatetext("Ingrese la descripcion de la categoria: ").strip()
    if not descripcion:
        print("ERROR: La descripcion de la categoria no puede estar vacía.")
        sc.pausar_pantalla()
        return
    
    if not categorias_data.get("categorias"):
        id_categoria = "1"
    else:
        max_id = max(int(k) for k in categorias_data["categorias"].keys())
        id_categoria = str(max_id + 1)

    nueva_categoria = {
        "id": id_categoria,
        "nombre": nombre,
        "descripcion": descripcion,
    }
    
    categorias_data["categorias"][id_categoria] = nueva_categoria
    cf.writeJson(cfg.BD_CATEGORIAS, categorias_data)

    print(f"\nCategoria '{nombre}' registrada con éxito con el ID: {id_categoria}")
    sc.pausar_pantalla()

def anadirChef():
    sc.limpiar_pantalla()
    chef_data = cf.readJson(cfg.BD_CHEFS)
    if not isinstance(chef_data, dict) or 'chefs' not in chef_data:
        chef_data = {"chefs": {}}

    print("-> Añadir un nuevo chef")
    nombre = vd.validatetext("Ingrese el nombre del chef: ").title().strip()
    for chef in chef_data.get("chefs", {}).values():
        if chef.get("nombre", "").lower() == nombre.lower():
            print(f"Error: El chef con el nombre '{nombre}' ya está registrado.")
            sc.pausar_pantalla()
            return
    if not nombre:
        print("ERROR: El nombre del chef no puede estar vacío.")
        sc.pausar_pantalla()
        return
    especialidad = vd.validatetext("Ingrese la especialidad del chef: ").strip()
    if not especialidad:
        print("ERROR: La especialidad del chef no puede estar vacía.")
        sc.pausar_pantalla()
        return
    
    if not chef_data.get("chefs"):
        id_chef = "1"
    else:
        max_id = max(int(k) for k in chef_data["chefs"].keys())
        id_chef = str(max_id + 1)

    nuevo_chef = {
        "id": id_chef,
        "nombre": nombre,
        "especialidad": especialidad
    }
    
    chef_data["chefs"][id_chef] = nuevo_chef
    cf.writeJson(cfg.BD_CHEFS, chef_data)

    print(f"\Chef '{nombre}' registrado con éxito con el ID: {id_chef}")
    sc.pausar_pantalla()


def anadirHamburguesa():
    sc.limpiar_pantalla()
    hamburguesa_data = cf.readJson(cfg.BD_HAMBURGUESAS)
    ingredientes_data = cf.readJson(cfg.BD_INGREDIENTES)
    categorias_data = cf.readJson(cfg.BD_CATEGORIAS)
    chefs_data = cf.readJson(cfg.BD_CHEFS)
    chefs = chefs_data.get("chefs", {})
    categorias = categorias_data.get("categorias", {})
    ingredientes = ingredientes_data.get("ingredientes", {})

    if not (ingredientes_data) and not (categorias_data):
        print("No hay categorias o ingredientes registrados.")
        sc.pausar_pantalla()
        return

    if not isinstance(hamburguesa_data, dict) or 'hamburguesas' not in hamburguesa_data:
        hamburguesa_data = {"hamburguesas": {}}

    print("-> Añadir un nueva hamburguesa")
    nombre = vd.validatetext("Ingrese el nombre de la hamburguesa: ").title().strip()
    for hamburguesa in hamburguesa_data.get("hamburguesas", {}).values():
        if hamburguesa.get("nombre", "").lower() == nombre.lower():
            print(f"Error: La hamburguesa con el nombre '{nombre}' ya está registrada.")
            sc.pausar_pantalla()
            return
    if not nombre:
        print("ERROR: El nombre del ingrediente no puede estar vacío.")
        sc.pausar_pantalla()
        return
    
    print("----Lista de categorias----")
    for cod, categoria in categorias.items():
        print(f"{cod}: {categoria['nombre']}")

    id = input("Id de la categoria: ")

    if id not in categorias:
        print("Código no válido.")
        return
    
    categoria = categorias[id]['nombre']

    ingredientes_copy = ingredientes.copy()
    agregarIngredientes = True
    ingredientesHamburguesa = []
    while agregarIngredientes:
        sc.limpiar_pantalla()
        print("----Lista de ingredientes disponibles----")
        for cod, ingrediente in ingredientes_copy.items():
            print(f"{cod}: {ingrediente['nombre']}")

        id = input("Id del ingrediente a seleccionar: ")

        if id not in ingredientes_copy:
            print("Código no válido.")
            return
        
        ingredienteHamburguesa = ingredientes_copy[id]['nombre']
        ingredientesHamburguesa.append(ingredienteHamburguesa)
        agregarIngredientes = vd.validateBoolean("Desea agregar otro ingrediente? (S/N)")

    precio = vd.validatefloat("Ingrese el precio del ingrediente: ")
    if precio < 0:
        print("ERROR: El precio del ingrediente debe ser superior a 0")
        sc.pausar_pantalla()
        return
    
    print("----Lista de chefs----")
    for cod, chef in chefs.items():
        print(f"{cod}: {chef['nombre']}")

    id = input("Id del chef: ")

    if id not in chefs:
        print("Código no válido.")
        return
    
    chef = chefs[id]['nombre']
    
    if not hamburguesa_data.get("hamburguesas"):
        id_hamburguesa = "1"
    else:
        max_id = max(int(k) for k in hamburguesa_data["hamburguesas"].keys())
        id_hamburguesa = str(max_id + 1)

    nueva_hamburguesa = {
        "id": id_hamburguesa,
        "nombre": nombre,
        "categoria": categoria,
        "ingredientes": ingredientesHamburguesa,
        "precio" : precio,
        "chef" : chef
    }
    
    hamburguesa_data["hamburguesas"][id_hamburguesa] = nueva_hamburguesa
    cf.writeJson(cfg.BD_HAMBURGUESAS, hamburguesa_data)

    print(f"\nHamburguesa'{nombre}' registrada con éxito con el ID: {id_hamburguesa}")
    sc.pausar_pantalla()