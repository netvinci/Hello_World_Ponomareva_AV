N = int(input("Введите количество чисел N: "))

max = float(input("Введите число 1: "))

i = 2
while i <= N:
    num = float(input(f"Введите число {i}: "))
    if num > max:
        max = num
    i = i + 1

print(f"Максимальное число: {max}")