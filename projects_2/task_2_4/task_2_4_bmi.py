weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))
bmi = weight / ((height / 100 )** 2)

print("--- Отчёт о состоянии здоровья ---")
print(f"Рост:\t{height} см")
print(f"Вес:\t{weight} кг")
print(f"Индекс массы тела: {bmi:.2f}")