'''
Created on Jan 31, 2019

@author: Alex
'''

import random

win= 0
numberOfTimes= int(input("How many times would you like to run the program? you must choose a number between 10 and 1000: "))
while numberOfTimes <10 or numberOfTimes >1000:
    numberOfTimes= int(input("You entered an invalid input. Please enter a number between 10 and 1000: "))
    

    switches= input("Do you want to switch or stay for every guess you make? ")
    while switches.lower() != 'switch' and switches.lower() != 'stay':
        switch= input("You entered an invalid input. Please enter the word switch, or the word stay:")
    
    for i in range(1, numberOfTimes+1):
        carDoor= random.randint(1,3)
        guess= random.randint(1,3)
    
    if carDoor== guess:
        if carDoor== 1:
            if switches.lower() == 'stay':
                win += 1
            
        elif carDoor== 2:
            if switches.lower() == 'stay':
                win += 1
            
        elif carDoor== 3:
            if switches.lower() == 'stay':
                win += 1
            
    if carDoor== guess:
        if carDoor== 1:
            if switches.lower() == 'switch':
                win += 1
            
        elif carDoor== 2:
            if switches.lower() == 'switch':
                win += 1
            
        elif carDoor== 3:
            if switches.lower() == 'switch':
                win += 1
    
    winPercentage= (win/numberOfTimes) *100
    print("The player won", win , "/", numberOfTimes, "games"(format(winPercentage, '.2f'), "%"), sep='')
