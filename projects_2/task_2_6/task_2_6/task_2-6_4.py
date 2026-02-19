direction = input("Куда пойдешь? Налево, прямо, направо?").strip().lower()

if direction == "налево":
    print("Коня потеряешь")
elif direction == "прямо":
    print("Жив будешь, но себя позабудешь")
elif direction == "направо":
    print("Жизнь потеряешь")
else:
    print("Ошибка братан")