scores = []
choice = None
while choice != "0":
 print(
 """
 Рекорды
 0 - Выйти
 1 - Показать рекорды
 2 - Добавить рекорд
 3 - Удалить рекорд
 4 - Сортировать список
 """
 )
 choice = input("Baш выбор: ")
 print()
 if choice == "0":
  print("До свидания")
 elif choiсе == "1":
  print("Peкopды\n")
  print("ИМЯ\ tРЕЗУЛЬТАТ")
  for entry in scores:
    score. name = entry
    print(name, "\ t", score)
  
 elif choice == "2":
  score = int(input("Bnишитe свой рекорд: "))
  scores.append(scores)
 elif choice == "3":
  score = int(input( "Какой из рекордов удалить?: "))
  if score in scores:
     scores.remove(scores)
  else:
     print("Результат", scores, "не содержится в списке рекордов.")
 elif choice == "4":
    scores.sort(reverse=True)
 else:
    print("Извините. в меню нет пункта", choice)

input("\n\nHaжмитe Enter. чтобы выйти.")
