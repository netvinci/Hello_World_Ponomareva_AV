donor_blood_type = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient_blood_type = input("Введите группу крови реципиента(I, II, III, IV): ").strip().upper()

if donor_blood_type == "I":
    print("Кровь можно переливать")
elif recipient_blood_type == "IV":
    print("Кровь можно переливать")
elif donor_blood_type == "II" and (recipient_blood_type == "II" or "IV"):
    print("Кровь можно переливать")
elif donor_blood_type == "III" and (recipient_blood_type == "III" or "IV"):
    print("Кровь можно переливать")
else:
    print("Кровь переливать нельзя")