import random

#Possible Numbers
random1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
random2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
random3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]


#Person Choice the Numbers
number1 = int(input("Choose a Number between 1 and 49:"))
number2 = int(input("Choose a Number between 1 and 49:"))
number3 = int(input("Choose a Number between 1 and 49:"))


#lottery numbers are drawn
lotto1 = random.choice(random1)
lotto2 = random.choice(random2)
lotto3 = random.choice(random3)


#Check if a number is correct
if number1 == lotto1 and number2 == lotto2 and number3 == lotto3:
    print("You Won! 500€")
else:
    if number1 == lotto1 and number2 == lotto2 or number1 == lotto1 and number3 == lotto3 or number2 == lotto2 and number3 == lotto3:
        print("You have 2 Numbers right! 150€")
    else:
        if number1 == lotto1 or number2 == lotto2 or number3 == lotto3:
            print("You have 1 Number right! 50€")

