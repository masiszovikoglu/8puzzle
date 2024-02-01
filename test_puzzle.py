import heuristic_random as e
import numpy as np
import random
import time

average=0
games=0
moves=0

for i in range(100):
    # Play the game
    game=np.array([(1,8),(2,1),(3,3),(4,4),(5,0),(6,2),(7,7),(8,6),(9,5)])
    
    #initial state
    # |1|2|3|
    # |4|5|6|
    # |7|8|0|


    goal=False
    #e.print_board(game)
    count=0
    start=time.time()
    while (goal==False):
       
        e.play(game)
        count=count+1
        
        goal=e.check_goal(game)
        
    end=time.time()
    e.print_board(game)
    print(count)
    print("The time of execution is :",
          (end-start)*10*10*10 , "ms")
    average=average+end-start
    games=games+1
    moves=moves+count
    
print(average/games*1000,"miliseconds on avearge")
print(moves/games,"moves on average")