N = int(input("Введите число: "))
F = 1
i = 1

while i <= N:
    F = F * i
    i = i + 1

print("Факториал числа", N, "=", F)