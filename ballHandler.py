import time
import json
import pathlib
from random import randint


with open("./ballsData.json", "r") as f:
    ballsConfig = json.load(f)

lastSent = time.time()

def check_stamp():
    global lastSent

    if time.time() - lastSent > 10:
        lastSent = time.time()
        return True
    else:
        return False
    
def get_ball():
    selectedBall = ballsConfig[0]

    for data in reversed(ballsConfig):
        if randint(1, 2) == 1:
            selectedBall = data
            break

    return selectedBall
        
    

    
