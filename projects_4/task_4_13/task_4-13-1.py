A = float(input("Введите число A: "))
B = float(input("Введите число B: "))
C = float(input("Введите число C: "))
D = float(input("Введите число D: "))

if A < B:
     min = A
else:
     min = B

if C < min:
     min = C
if D < min:
     min = D
else:
     min = min

print("Минимальное число:", min)


