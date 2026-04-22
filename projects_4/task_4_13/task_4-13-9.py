N = int(input("Введите количество элементов массива: "))
M = []
sum = 0

i = 0
while i < N:
    j = float(input(f"Введите элемент {i+1}: "))
    M.append(j)
    i = i + 1

i = 0
while i < N:
    if not M[i] % 2 == 0:
        sum = sum + M[i]
    i = i + 1

print("Сумма всех нечетных чисел:", sum)