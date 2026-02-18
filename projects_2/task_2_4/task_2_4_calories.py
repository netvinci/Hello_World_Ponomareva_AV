protein = int(input("Введите массу белков в продукте (г): "))
fats = int(input("Введите массу жиров в продукте (г): "))
carbohydrates = int(input("Введите массу углеводов в продукте (г): "))
calories = (protein * 4) + (fats * 9) + (carbohydrates * 4)

print(f"Калорий в продукте - {calories}")