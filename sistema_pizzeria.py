cantidad_pedidos = 0
cantidad_pizzas = 0

cantidad_chicas = 0
cantidad_medianas = 0
cantidad_grandes = 0

recaudacion = 0
mayor_pedido = 0

continuar = "s"
def mostrar_menu():
    print("\n--- TAMAÑOS DE PIZZA ---")
    print("1. Pizza chica   - $6000")
    print("2. Pizza mediana - $8000")
    print("3. Pizza grande  - $10000")

while continuar == "s":
        
    mostrar_menu()

    opcion = int(input("Seleccione un tamaño (1-3): "))


    while opcion < 1 or opcion > 3:
        print("Opción incorrecta.")
        opcion = int(input("Seleccione un tamaño (1-3): "))

    if opcion == 1:
        tamaño = "Chica"
        precio = 6000

    elif opcion == 2:
        tamaño = "Mediana"
        precio = 8000

    else:
        tamaño = "Grande"
        precio = 10000

    def calcular_descuento(subtotal):
        if subtotal >= 30000:
            descuento = subtotal * 0.10
        else:
            descuento = 0

        return descuento


    cantidad = int(input("Cantidad de pizzas: "))

    while cantidad <= 0:
        print("La cantidad debe ser mayor que 0.")
        cantidad = int(input("Cantidad de pizzas: "))


    continuar = input("¿Desea cargar otro pedido? (s/n): ")

    while continuar != "s" and continuar != "n":
        print("Opción incorrecta.")
        continuar = input("Ingrese s para continuar o n para terminar: ")