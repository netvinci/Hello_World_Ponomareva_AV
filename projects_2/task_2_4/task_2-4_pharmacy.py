capsule_count = int(input("Введите общее количество произведенных капсул: "))
capacity = int(input("Введите количество капсул в одной упаковке: "))

print("--- Отчёт фасовочного цеха ---")
print("Полных упаковок: ", capsule_count // capacity)
print("Остаток капсул: ", capsule_count % capacity)