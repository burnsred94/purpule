price = int(input("Цена товара: "))
fee = int(input("Процент скидки: "))

result = price - price * (fee / 100)

print(f"Цена со скидкой: {result}")