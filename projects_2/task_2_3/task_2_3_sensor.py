operator_name = input("Введите имя оператора: ")
current_pressure = input("Введите текущее значение давления (Па): ")

with open(r"C:\Users\WladlexD\Documents\Ponomareva_av\projects_2\task_2_3\sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"Оператор\t{operator_name}\nЗначение\t{current_pressure}")

print("Данные успешно сохранены в sensor_log.txt")