T=20
import math
def P(successor,current):
    deltaE=successor-current
    t=deltaE/T
    p=math.e**t
    return p

import random

minimum=999999
counter=0
def SimulatedAnnealing(T,current,counter,minimum):
    successor=random.randrange(current-30,current+30)
    p=P(successor,current)
    if(p<minimum):
        print(successor,"---",p)
        current=successor
        minimum=p
    if(counter<100):
        counter=counter+1
        SimulatedAnnealing(T,current,counter,minimum)
    return minimum

SimulatedAnnealing(T,16,0,minimum)
        
    
    