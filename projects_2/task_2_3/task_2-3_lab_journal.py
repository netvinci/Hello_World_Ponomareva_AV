researcher_name = input("Введите имя исследователя: ")
date = input("Введите дату исследования: ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите заключение: ")

with open(r"C:\Users\WladlexD\Documents\inf\journal.txt", "w", encoding="utf-8") as file:
    file.write("+" + "-" * 50 + "+" + "\n| Электронный лабораторный журнал \t|\n+" + "-" * 50 + "+" + f"\n| ФИО Исследователя: {researcher_name}|\n| Дата: {date}|\n| Эксперимент: {experiment_name}|\n+" + "-" * 50 + f"+\n| Вывод: |\n| {conclusion}|\n+" + "-" * 50 + "+")