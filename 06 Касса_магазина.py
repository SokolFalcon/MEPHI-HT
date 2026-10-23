prices = {
    "хлеб": 50,
    "молоко": 90,
    "сыр": 400,
    "яблоки": 120,
    "кофе": 350
}


def greet_cashier():
    name = input("Введите имя кассира: ").strip()
    print(f"Здравствуйте, {name}! Касса открыта")
    return name


def print_menu(prices):
    print("Товары в продаже:")
    for product in prices:
        print(f"  {product} — {prices[product]} руб.")


def ask_quantity(product):
    quantity = int(input(f"Сколько «{product}»? "))
    return quantity


def item_cost(price, quantity):
    return price * quantity


def collect_cart(prices):
    cart = []

    while True:
        print()
        product = input(
            'Товар (или "оплата", чтобы перейти к оплате): '
        ).strip().lower()

        if product == "оплата":
            break

        if product in prices:
            quantity = ask_quantity(product)
            cost = item_cost(prices[product], quantity)

            cart.append((product, quantity, cost))
            print(f"Добавлено: {product} × {quantity} = {cost} руб.")
        else:
            print(f"Товара «{product}» нет в продаже")

    return cart


def ask_card():
    print()
    answer = input("Есть карта магазина? (да/нет): ").strip().lower()
    return answer == "да"


def print_receipt(cart):
    print("\n--- Чек ---")
    total = 0
    number = 1

    for product, quantity, cost in cart:
        print(f"{number}. {product} × {quantity} = {cost} руб.")
        total += cost
        number += 1

    print(f"Сумма: {total} руб.")
    return total


def apply_discount(total, card=False):
    if card:
        discount = total * 10 // 100
    elif total >= 1000:
        discount = total * 5 // 100
    else:
        discount = 0

    to_pay = total - discount
    return discount, to_pay


def print_result(cart, discount, to_pay, name):
    different_products = set()

    for product, quantity, cost in cart:
        different_products.add(product)

    print(f"Скидка: {discount} руб.")
    print(f"К оплате: {to_pay} руб.")
    print(f"Разных товаров в чеке: {len(different_products)}")
    print(f"\nСпасибо за работу, {name}!")


# Основная программа
cashier = greet_cashier()
print_menu(prices)
cart = collect_cart(prices)
has_card = ask_card()
total = print_receipt(cart)
discount, to_pay = apply_discount(total, card=has_card)
print_result(cart, discount, to_pay, cashier)