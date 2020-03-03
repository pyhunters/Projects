'''
المشروع الأول 
برنامج تخمين 

الوصف 

سيقوم البرنامج أولاً بإنشاء عدد غير معروف للمستخدم بشكل عشوائي. يحتاج المستخدم إلى تخمين ما هو هذا الرقم. (بمعنى آخر 
، يحتاج المستخدم إلى أن يكون قادرًا على إدخال المعلومات.) إذا كان تخمين المستخدم خاطئًا ، فيجب أن يعرض البرنامج نوعًا 
من الدلائل على مدى الخطأ (على سبيل المثال ، الرقم مرتفع جدًا أو منخفض جدًا). إذا كان المستخدم يخمن بشكل صحيح 
، يجب أن تظهر إشارة إيجابية. ستحتاج إلى وظائف للتحقق مما إذا كان إدخال المستخدم رقمًا حقيقيًا
، لمعرفة الفرق بين رقم الإدخال والأرقام التي تم إنشاؤها عشوائيًا ، ثم لمقارنة الأرقام.



مثل ماقلت سابقًا الوصف ليس تحديد لكم الجميع له حرية الإبداع 
سوا برامج تخمين ارقام و احرف كلمات سرية حسابات مستخدمين ...الخ  ومن يؤد ان يضعها ايضًا في واجهة رسومية 


ارونا ابداعتكم  pyHunters 😋

'''


#------------------ @start:zaid------------------------------

import random
print("This program is creating a random number from 0 to 9, have a moment to think...\n")
t=4
for i in range(1):
  rnd=random.randint(0,9)
  l=int(input(f"you have {t} attempts left, inser your geuss here:  "))
  while t>0:
    if l==rnd :
      print('very good guess is correct 👍🏻')
      break
    
    else:
      t-=1
      if t==0:
        print("sorry you have consumed all your attempts, goodluck next time🌹")
        break
      else:
        l=int(input(f"you have {t} attempts left, inser your geuss here:  "))
    
  
#-------------------- @end:zaid------------------------------



#------------------ @start:hadeel------------------------------












#-------------------- @end:hadeel------------------------------




#------------------ @start:khalid------------------------------
import random
wordList = ['cat', 'car', 'rat', 'dog', 'pan', 'pen', 'fox', 'gun', 'wax']
word = random.choice(wordList)
var1 = "_"
var2 = "_"
var3 = "_"
guess = 0
guessCharacter = ""
print("""
                *******************************************************************
                *   WELCOME! To the Word Guessing game                            *
                *   Game Rules:                                                   * 
                *   1- There is a word that consist of 3 letters, try to guess    *
                *   2- You will be guessing the letters not the word              *
                *   2- If you made 5 wrong attempts you will lose                 *
                *   3- Read the previous rules carefully                          *
                *******************************************************************
                """)
while guess < 10:
    if guess < 6:
        guessCharacter = input("What is your guess? ").lower()
        # if guess is true
        if guessCharacter == word[0]:
            var1 = guessCharacter
            print("*" * 20)
            print("Your guess is right")
            print(f"The word is     {var1} {var2} {var3}")
            # check if the word was guessed successfully
            if var1 == word[0] and var2 == word[1] and var3 == word[2]:
                print("""
                                ***********************************
                                *  Congratulations you have won!  *
                                ***********************************
                                """)
                break
        # if guess is true
        elif guessCharacter == word[1]:
            var2 = guessCharacter
            print("*" * 20)
            print("Your guess is right")
            print(f"The word is     {var1} {var2} {var3}")
            # check if the word was guessed successfully
            if var1 == word[0] and var2 == word[1] and var3 == word[2]:
                print("""
                                ***********************************
                                *  Congratulations you have won!  *
                                ***********************************
                                """)
                break
        # if guess is true
        elif guessCharacter == word[2]:
            var3 = guessCharacter
            print("*" * 20)
            print("Your guess is right")
            print(f"The word is     {var1} {var2} {var3}")
            # check if the word was guessed successfully
            if var1 == word[0] and var2 == word[1] and var3 == word[2]:
                print("""
                ***********************************
                *  Congratulations you have won!  *
                ***********************************
                """)
                break
        # if guess is wrong!
        else:
            guess += 1
            print("Sorry, your guess is wrong!")
            print("*" * 20)
            print("You can try again ^_^")
            print(f"You have {5 - guess} attempts left")
            # if it is the 1st wrong attempt
            if guess == 1:
                print(
                    "         |\n"
                    "         | \n"
                    "         |\n"
                    "          ")
            # if it is the 2nd wrong attempt
            elif guess == 2:
                print("\n"
                      "         |\n"
                      "         |\n"
                      "         |\n"
                      "         |\n"
                      "         | \n"
                      "         |\n"
                      "          ")
            # if it is the 3rd wrong attempt
            elif guess == 3:
                print("\n"
                      "     ____\n"
                      "    |    |\n"
                      "    o    |\n"
                      "         |\n"
                      "         |\n"
                      "         | \n"
                      "         |\n"
                      "          ")
            # if it is the 4th wrong attempt
            elif guess == 4:
                print("\n"
                      "     ____\n"
                      "    |    |\n"
                      "    o    |\n"
                      "   /|\   |\n"
                      "         |\n"
                      "         | \n"
                      "         |\n"
                      "          ")
            # if it is the last wrong attempt
            elif guess == 5:
                print("\n"
                      "     ____\n"
                      "    |    |\n"
                      "    o    |\n"
                      "   /|\   |        GAME OVER\n"
                      "    |    |\n"
                      "   / \   | \n"
                      "         |\n"
                      "          ")
                print("""
                **************************************************
                *   Sorry, the 5 attempts are finished           *
                *   You can run the game again if you like ^_^   *
                **************************************************
                """)
                print(f"The word was {word}")
                break
#-------------------- @end:khalid------------------------------



#------------------ @start:عبدالرحمن------------------------------











#-------------------- @end:عبدالرحمن------------------------------


#------------------ @start:ممدوح------------------------------










#-------------------- @end:ممدوح------------------------------

#------------------ @start:العنود------------------------------










#-------------------- @end:العنود------------------------------

#------------------ @start:أحمد------------------------------
from random import randint
for _ in range (100):
    value=randint(0,100)
player=int(input("plz enter your guess in integer : "))
if player < value :
    print("your number is less than the value ")
elif player > value :
    print("your number is greater than the value ")
else:
    print("Congratulations, you won ")
#-------------------- @end:أحمد------------------------------
