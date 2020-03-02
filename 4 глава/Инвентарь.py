inventory = ()
if not inventory:
    print( "Вы безоружны." )
input("\nHaжмитe Enter. чтобы продолжить.")
inventory = ("меч" , "кольчуга", "щит" , "целебное снадобье")
print("\nСодержимое кортежа : ")
print(inventory)
print("\nИтaк. в вашем арсенале:")
for item in inventory:
    print(item)
input("\n\nHaжмитe Enter. чтобы выйти. ")
