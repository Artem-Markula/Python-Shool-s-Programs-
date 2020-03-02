import random
# начало игры 
WORDS =("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник") 
word = random.choice(WORDS)
correct = word
jumble = ""
if correct == ("простая"):
 for i in range(7):
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    
if correct == ("сложная"):
 for i in range(7):
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):] 
if correct == ("анаграмма"):
 for i in range(8):
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    
if correct == ("питон"):
 for i in range(5):
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):] 
if correct == ("ответ"):
 for i in range(5):
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    
if correct == ("подстаканник"):
 for i in range(12):
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]         
print(""" Добро пожаловать в игру 'Анаграммы'! Надо переставить буквы так.""")
print("""чтобы получилось осмысленное слово.""") 
print("Boт анаграмма:", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ") 
while guess != correct and guess != "":
   print("K сожалению. вы неправы.")
   break 
if guess == correct: 
   print("Дa. именно так! Вы отгадали!\n") 
print("Cnacибo за игру.") 
input("\n\nHaжмитe Enter. чтобы выйти.")
#Сделал Королёв
