import random 

carDoor= random.randint(1,3) 

guess= int(input("Do you want to choose Door 1, 2, or 3?")) 

print("You picked Door #" ,guess ,"." ,sep='') 

print("-------------------------") 

 
 
 
 

if carDoor!= guess: 

    if carDoor== 1 and guess== 2: 

        goat= 3 

elif carDoor== 1 and guess== 3: 

        goat= 2 

elif carDoor== 2 and guess== 1: 

        goat= 3 

elif carDoor== 2 and guess== 3: 

        goat= 1 

elif carDoor== 3 and guess== 1: 

        goat= 2 

elif carDoor== 3 and guess== 2: 

        goat= 1 

 




if carDoor== guess: 

    if carDoor== 1: 

        print("One of the goats behind Door #2")  

ans= input("Do you want to change your guess to Door 3?") 

if ans.lower()== 'yes': 

        print("The car was behind door number #1!") 

        print("You lost.") 

elif ans.lower()== 'no': 

        print("The car was behind door number #1!")  

        print("You won!") 
 





elif carDoor== 2: 

        print("One of the goats behind Door #3") 

ans= input("Do you want to change your guess to Door 1?") 

if ans.lower()== 'yes': 

        print("The car was behind door number #2!") 

        print("You lost.") 

elif ans.lower()== 'no': 

        print("The car was behind door number #2!")  

        print("You won!") 

 




elif carDoor == 3: 

        print("One of the goats behind Door #1") 

ans= input("Do you want to change your guess to Door 2?") 

if ans.lower()== 'yes': 

        print("The car was behind door number #3!") 

        print("You lost.") 

elif ans.lower()== 'no': 

        print("The car was behind door number #3!")  

        print("You won!") 

 
 

 

elif carDoor!= guess: 

    if carDoor== 1: 

        print("One of the goats behind Door #" ,goat ,sep='') 

ans= input("Do you want to change your guess?") 

if ans.lower()== 'yes': 

        print("The car was behind door number #1!") 

        print("You won!") 

elif ans.lower()== 'no': 

        print("The car was behind door number #1!")  

        print("You lost.") 

 
 



elif carDoor== 2: 

        print("One of the goats behind Door #" ,goat ,sep='') 

ans= input("Do you want to change your guess?") 

if ans.lower()== 'yes': 

        print("The car was behind door number #2!") 

        print("You won!") 

elif ans.lower()== 'no': 

        print("The car was behind door number #2!")  

        print("You lost.") 

 
 



elif carDoor== 3: 

        print("One of the goats behind Door #" ,goat ,sep='') 

ans= input("Do you want to change your guess?") 

if ans.lower()== 'yes': 

        print("The car was behind door number #3!") 

        print("You won!") 

elif ans.lower()== 'no': 

        print("The car was behind door number #3!")  

        print("You lost.") 