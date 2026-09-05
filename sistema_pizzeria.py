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

mostrar_menu()


def calcular_descuento(subtotal):
    if subtotal >= 30000:
        descuento = subtotal * 0.10
    else:
        descuento = 0

    return descuento
