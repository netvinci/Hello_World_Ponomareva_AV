reagent_name = input("Введите название нового реактива: ")
amount_of_reagent = input("Введите количество нового реактива: ")

f = open(r"C:\Users\WladlexD\Documents\inf\invenroty.txt", "w", encoding="utf-8")
print(f"Реактив {reagent_name} поступил на склад в количестве {amount_of_reagent} шт.", file=f)
f.close()
