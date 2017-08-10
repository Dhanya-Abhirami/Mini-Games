#S.DHANYA ABHIRAMI
#Guess the number game
from random import *
import random
c="y"
while c=="y" or c=="Y":
    print("Guess a number between 1 and 100")
    k=randint(1,100)
    while True:
        n=int(input())
        if n!=k:
            if abs(n-k)<10:
                print("Close to answer,",end=" ")
            if n<k:
                print("Small, Guess Again")
            if n>k:
                print("Big, Guess Again")
        else:
            break
    print("Correct!")
    print("Play Again? Y/N: ")
    c=input()
print("Thanks for playing!")    
