N = int(input("Введите количество элементов массива: "))
M = []
pos = 0
i = 0
while i < N:
    j = float(input(f"Введите элемент {i+1}: "))
    M.append(j)
    i = i + 1

i = 0
while i < N:
    if M[i] > 0:
        pos = pos + 1
    i = i + 1

print(f"Кол-во положительных чисел: {pos}")