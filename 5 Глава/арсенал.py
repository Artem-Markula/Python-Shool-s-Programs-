inventory = ["меч", "кольчуга", "щит", "целебное снадобье"]
print("\nИтaк. в вашем арсенале:")
for item in inventory:
   print(item)
input("\nНажмите Enter. чтобы узнать сколько предметов")
print("Сейчас в вашем распоряжении", len(inventory), "предмета/ -ов.")
if "целебное снадобье" in inventory:
   print("Bы еще поживете и повоюете.")
index = int(input("\nBвeдитe индекс одного из предметов арсенала: "))
print("Под индексом", index, "в арсенале находится", inventory[index])
start = int(input("\nBвeдитe начальный индекс среза: "))
finish = int(input("Bвeдитe конечный индекс среза: "))
print(inventory[start:finish])
chest = ["золото", "драгоценные камни"]
print("Bы нашли ларец. Вот что в нем есть:")
print(chest)
print("Bы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении:")
print(inventory)
print("Bы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print("Teпepь ваш арсенал содержит следующие предметы:")
print(inventory)
print("Зa золото и драгоценные камнV: вы купили магический кристалл. способный предсказывать будущее.")
inventory[4:6] = ["магический кристалл"]
print("Teпepь в вашем распоряжении:")
print(inventory)
print("B тяжелом бою был раздроблен ваш щит.")
del inventory[2]
print("Boт что осталось в арсенале:")
print(inventory)
input("\n Но что то пошло не так.")
print("Bopы лишили вас арбалета и кольчуги.")
del inventory[:2]
print("B арсенале теперь только:")
print(inventory)
input("А чего дальлше?")
print("Вас убили с арбалета")
del inventory[0:2]
print("B арсенале теперь только:")
print(inventory)
input("Нажмите Enter. чтобы выйти.")
