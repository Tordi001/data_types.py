from colorama import Fore
from colorama import Fore

print(Fore.RED + ("WELCOME TO TORDI'S BET"))
print(Fore.GREEN + "You must be up to 18 years")
signup_1 = input("to sign up click (YES/NO): ")
if(signup_1 == 'YES' or signup_1 == 'yes'):
    print("Thank you for signing up...")
elif(signup_1 == 'NO' or signup_1 == 'no'):
    print("Thanks for cancelling....")
else:
    print("Click here to go back")

print(Fore.RED + "You can start your verification now")

first_name = str(input("Enter your first name here: "))
second_name = str(input("Enter your middle name here: "))
third_name = str(input("Enter you last name here: "))
forth_name = (input("Enter your date of birth here: "))
fifth_name = int(input("Enter you mobile number here: "))
sixth_name = str(input("Enter the name of you country here: "))
print("Thank you for signing up......")

a = 'The below game is a game were a player is expected to select a number from 1 - 10, if the playes number fall into the reqired number, Then his a winner...'
b = 'We have different levels for different players'
c = 'From 0-10 will be rewarded a sum of 5,000 naira'
d = 'From 0-15 will be rewarded a sum of 20,000 naira'
e = 'From 0-20 will be rewarded a sum of 40,000 naira'
f = 'From 0-30 will be rewarded a sum of 100,000 naira'
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
import random
print("Throw a dice to wine a lotto")
select_game = int(input("Select the level you want to play, choose level(1/2/3/4)"))

1 == random.randint(0, 10)
if (1 == (int(input("Now input the value you want to play from 0-10 here: ")))):
    print("You have won the sum of 5,000 naira, please redeem your prize")
else:
    print("You entered a wrong number, please try again....")
print(1)

2 == random.randint(0, 15)
if(2 == (int(input("Now input the value ypu want to play from 0-15 here")))):
    print("You have won the sum of 10,000 naira, please redeem your prize")
else:
    print("You entered a wrong number, please try again....")
print(2)

3 == random.randint(0, 20)
if(3 == int(input("now input the value you want to play from 0-20 here: "))):
    print("You have won the sum of 40,000 naira, please redeem your prize")
else:
    print("You entered a wrong number, please try again....")
print(3)

4 == random.randint(0, 30)
if(4 == (int(input("now input the value you want to play from 0-30 here: ")))):
    print("You have won the sum of 100,000 naira, please redeem your prize")
else:
    print("You entered a wrong number, please try again....")
print(4)

print(Fore.RED + "THIS SECTION IS FOR ONLY FOOTBALL BETTING SECTION")
import random
football = str(input("Enter the club name you love so, you might the lucky to win the prize.....Choose either (mancity/chelse): "))

mancity = random.randrange(1, 2)
if(mancity == input("Enter the number to win your prize here: ")):
    print("You have won, kindly redeem you prize from our vendor....")
else:
    print("You failed, please try again")

chelse = random.randrange(2, 3)
if(chelse == input("Enter the number to win your prize here: ")):
    print("You have won, kindly redeem you prize from our vendor....")
else:
    print("You failed, please try again")
print("Thanks for playing....")