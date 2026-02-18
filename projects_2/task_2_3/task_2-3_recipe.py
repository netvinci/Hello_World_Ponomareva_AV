culture_medium = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации (°C): ")

with open(r"C:\Users\WladlexD\Documents\Ponomareva_av\projects_2\task_2_3\recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"Питательная среда: {culture_medium}\nКонцентрация агара: {agar_concentration}\nТемпература стерилизации: {sterilization_temperature}°C\n")

print("Файл 'recipe.txt' успешно сформирован!")