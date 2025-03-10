lista = ["pan", "jamon", "cheddar", "huevos", "leche", "mantequilla", "Lechuga", "tomate", "mayonesa", "cebolla", "pepibillo", "moztasa "]


while True:
    print("Menu: 1. agregar 2. Ver lista 3. borrar una cosa 4. borrar todo 5. Salir")
    ele = input("escoge una opcion: ")

    if ele == "1":
        articulo = input("agrega un articulo: ")
        lista.append(articulo)
    elif ele == "2":
        print("Shopping List:", lista)
    elif ele == "3":
        articulo = input("Enter item to remove: ")
        if articulo in lista:
            lista.remove(articulo)
    elif ele == "4":
        lista.clear()
    elif ele == "5":
        break
    else:
        print("ta mal mi bro, dale pa atra")

#Ai was use for the creation of the list