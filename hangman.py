'''
Hangman Game
Code by S.Dhanya Abhirami
-----
    |
    |
    O
  -- --
    |
   / \
 
'''
from random import *
import random
l=['hangman', 'dinner', 'computer', 'america', 'olympics', 'football', 'minecraft', 'jacket', 'cabbage', 'electricity', 'dog',
            'pasta', 'japan', 'water', 'programming', 'anaconda', 'name', 'windows', 'curtains', 'bieber',
            'wheel', 'civilization', 'physics', 'bluebird' 'table', 'ACDC', 'guardian', 'maria', 'parachute',  'obama',
            'youtube', 'putin', 'dairy', 'christianity', 'penguin', 'coins', 'agitating', 'jumping', 'eating',
            'mother', 'executive', 'car', 'jade', 'abraham', 'sand', 'silver', 'uranium', 'bioshock', 'fizzle', 'moonlight', 'watermelon',
            'malayalam', 'computer', 'extreme', 'jeans', 'daring']


def disp(x,s):
    if x==1:
        s+='''
        -----'''
    elif x==2:
        s+='''
            |
            |'''
    elif x==3:
        s+='''
            O'''
    elif x==4:
        s+='''
          -- --'''
        
    elif x==5:
        s+='''
            |'''
        
    else:
        s+='''
           / \ \nBetter luck next time!'''
        
    print(s)
    return s       
        

print("Welcome to hangman game :)")
ch='y'
while(ch!='n'):
    x=l[randint(0, len(l)-1)]
    given=random.sample(range(0, len(x)), len(x)//3)
    hangman=0
    show=[x[i] if i in given else "_ " for i in range(len(x))]
    guessedalpha=""
    guessedword=[]
    s=""
    while(hangman<6):
        print("".join(show))
        ch1=input("1.Guess word \n2.Guess alphabet\n")
        if int(ch1) not in [1,2]:
            print("Enter a either 1 or 2")
            continue
        if ch1=='1':
            word=input("Enter word: ")
            if word not in guessedword:
                guessedword.append(word)
                if word==x:
                    print("\n",x)
                    print("\nCongrats, You win!")
                    break
                else:
                    hangman+=1
                    s=disp(hangman,s)
                    
            else:
                print("You have already guessed this word")
        elif ch1=='2':
            a=input("Enter alphabet: ").lower()
            if a not in guessedalpha:
                guessedalpha+=a
                if a in x:
                    aindex=[]
                    for i in range(0,len(x)):
                        if x[i]==a:
                            aindex.append(i)
                    for c in aindex:
                        show[c]=a
                    if "".join(show)==x:
                        print("\n",x)
                        print("\nCongrats, You win!")
                        break
                else:
                    hangman+=1
                    s=disp(hangman,s)
                    
                        
            else:
                print("\nYou have already guessed this alphabet")
    ch=input("\nTry Again? y/n ").lower()
print("\nThanks for spending time playing the game")   
