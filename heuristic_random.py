import numpy as np
import random
import time

# function to find neighbours of empty cell
def find_neighbours(game, empty_pos):
    
   
    neighbours=[]
    # empty is at corners
    
    if empty_pos==0:
        neighbours.append(1)
        neighbours.append(3)

    if empty_pos==2:
        neighbours.append(1)
        neighbours.append(5)
    
    if empty_pos==6:
        neighbours.append(3)
        neighbours.append(7)
        
    if empty_pos==8:
        neighbours.append(5)
        neighbours.append(7)
        
    if empty_pos==1:
        neighbours.append(0)
        neighbours.append(2)
        neighbours.append(4)
        
    
    if empty_pos==3:
        neighbours.append(0)
        neighbours.append(4)
        neighbours.append(6)
        
    if empty_pos==5:
        neighbours.append(2)
        neighbours.append(4)
        neighbours.append(8)
        
    if empty_pos==7:
        neighbours.append(4)
        neighbours.append(6)
        neighbours.append(8)
        
    if empty_pos==4:
        neighbours.append(1)
        neighbours.append(3)
        neighbours.append(5)
        neighbours.append(7)
        
        
    return neighbours 
    

#The move function compares the neighbours and movesthe number that is closer to where it should be to the space.
#If there is more than one choice, it makes a random selection.
#To avoid infinite loops, it sometimes moves by rule and sometimes randomly

def play(game):
   
    moves=[]
    e=(np.where(game==0)[0][0])
    e=int(e)
    n=find_neighbours(game,e)
    
    
    for i in range (len(n)):
        if calculate_distance(game[n[i]][1],e+1)<=calculate_distance(game[n[i]][1],n[i]+1):
            moves.append(n[i])
          
    if len(moves)==0:
        r=int((random.random()*len(n))/1)
        game[e][1], game[n[r]][1]= game[n[r]][1], game[e][1] 
    if len(moves)!=0:    
        a=random.random()
        if a<0.5:
            r=int((random.random()*len(moves))/1)
        
            game[e][1], game[moves[r]][1]= game[moves[r]][1], game[e][1]
        
        if a>=0.5:
            r=int((random.random()*len(n))/1)
            game[e][1], game[n[r]][1]= game[n[r]][1], game[e][1] 
            
            

def check_goal(game):
    for i in range(8):
        if game[i][1]!=i+1:
            return False
            break
    return True
def find_row(x):
    row=int(x/3)
    return row

def find_column(x):
    column=x%3
    return column

def calculate_distance(x,y):
    
    distance=abs(find_column(x)-find_column(y))+ abs(find_row(x)-find_row(y))
    return distance

    

def print_board(game):
    print("_____________")
    print("|",game[0][1],"|", game[1][1], "|", game[2][1],"|")
    print("-------------")
    print("|",game[3][1],"|", game[4][1], "|", game[5][1],"|")
    print("-------------")
    print("|",game[6][1],"|", game[7][1], "|", game[8][1],"|")
    print("-------------")