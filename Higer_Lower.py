#moduls
from art import logo,vs
from game_data import data
from random import choice
from os import system
#variables 
score=0
game_over=False  #flag


def check_answer(flower_accounta,flower_accountb,guess):
    """comparing the highest with the guess and  return the true or false result """
    if flower_accounta>flower_accountb:
        return guess=="a"
    else:
        return guess=="b"

def format_data(account):
    
     return f'{account["name"]} a {account["description"]} from {account["country"]}'

print(logo)
#countiue the game until the player guess a wrong answer
while game_over == False:
    
    
      
    
    #picking two random celebrities for the game 
    a=choice(data)
    b=choice(data)
    
    # choose another one if the secound celebritie is equal to first one
    while b==a:
        b=choice(data)
    
    
    print(f"Compare A: {format_data(a)}")
    print(vs)
    print(f"Against B: {format_data(b)}\n")
    
    flowera=a["follower_count"]
    flowerb=b["follower_count"]
    #compare
    guess=input("who has more folowers? type 'A' or 'B': ").lower()
    guess=check_answer(flowera,flowerb,guess)
    
    system("cls")
    print(logo)    
    
    if guess:
        score+=1
        print(f"you are right! corrent score: {score} ")
           
    else:
        print(f"sorry that's wrong! final score {score} ")
        game_over=True   #flag
        
    
    