
eat_sum = int(input("Траты на еду: "))
transport_sum = int(input("Траты на транспорт: "))
entertainment_sum = int(input("Траты на развлечения: "))

full_amount = eat_sum + transport_sum + entertainment_sum

print(f"Общая сумма трат: {full_amount}")
print(f"Средняя сумма трат: {full_amount / 3}")