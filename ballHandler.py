import time
import json
import pathlib
from random import randint


with open("./ballsData.json", "r") as f:
    ballsConfig = json.load(f)

lastSent = time.time()

def check_stamp():
    global lastSent
    print(int(time.time() - lastSent))
    if time.time() - lastSent > 10:
        lastSent = time.time()
        return True
    else:
        return False
    
def get_ball():
    selectedBall = len(ballsConfig) - 1

    for i in reversed(ballsConfig):
        print(i)
        if randint(1, 3) == 1:
            selectedBall = i

    return ballsConfig[selectedBall]
        
    

    
