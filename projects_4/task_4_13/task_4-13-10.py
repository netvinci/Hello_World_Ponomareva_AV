N = int(input("Введите количество элементов массива: "))
M = []
sum = 0

i = 0
while i < N:
    j = float(input(f"Введите элемент {i+1}: "))
    M.append(j)
    i = i + 1

i = 1
while i < N:
    sum = sum + M[i]
    i = i + 2

print(f"Сумма всех элементов массива с нечетными индексами {sum}")