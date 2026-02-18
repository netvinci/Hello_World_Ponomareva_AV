print("=== Анализ последовательности ДНК ===")

DNA = input("Введите последовательность ДНК: ")

print(f"Последовательность в верхнем регистре: {DNA.upper()}")

count_A = DNA.count("a")
count_T = DNA.count("t")
count_G = DNA.count("g")
count_C = DNA.count("c")
a_percent = count_A / len(DNA) * 100
t_percent = count_T / len(DNA) * 100
g_percent = count_G / len(DNA) * 100
c_percent = count_C / len(DNA) * 100

print(f"Подсчёт нуклеотидов:\nA: {count_A}\nT: {count_T}\nG: {count_G}\nC: {count_C}\n\nОбщая длина: {len(DNA)} нуклеотидов\n")
print(f"Нуклеотида А - {a_percent:.2f}%\nНуклеотида T - {t_percent:.2f}%\nНуклеотида G - {g_percent:.2f}%\nНуклеотида C - {c_percent:.2f}%\n")