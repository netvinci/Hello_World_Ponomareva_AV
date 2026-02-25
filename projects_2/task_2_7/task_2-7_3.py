seq = [ "ATATACGCGTA", "CTTCGGNGGA" ]

print("Последовательность целиком:")
for letter in seq:
    print(letter)

print("Последовательность построчно:")
for element in seq:
    for letter in element:
        print(letter)