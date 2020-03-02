import random
print("Я ощущаю вашу энергетику. От моего экрана не скрыто ни одно из ваших чувств.")
print("Итaк. ваше настроение ... ")
mood = random.randint(1,3)
if mood == 1:
    print("Ты радостный")
elif mood == 2:
    print("Пойдет")
elif mood == 3:
    print("Плохое")
input("\n\nPress the enter key to exit.")
