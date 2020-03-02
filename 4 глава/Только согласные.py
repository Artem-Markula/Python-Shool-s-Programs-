message = input("Введите текст: ")
new_message = ""
A = "аеiоuаеёиоуыэюя"
print()
for letter in message:
    if letter.lower() not in A:
        new_message += letter
        print("Создана новая строка:", new_message)
print("\nBoт текст с изъятыми гласными буквами:", new_message)
input("\n\nHaжмитe Enter. чтобы выйти.")
