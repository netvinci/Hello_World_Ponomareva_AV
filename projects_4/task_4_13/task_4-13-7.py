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
    sum = sum + M[i]
    i = i + 1

avg = sum / N

print(f"Среднее арифметическое: {avg}")