N = int(input("Введите количество элементов массива: "))
M = []
j = 0
k = 0

i = 0
while i < N:
    j = float(input(f"Введите элемент {i+1}: "))
    M.append(j)
    i = i + 1

i = 0
while i < N:
    k = k + M[i]
    j = j + 1
    i = i + 2
    avg = k / j

print(f"Среднее арифметическое всех элементов массива с четными индексами: {avg}")