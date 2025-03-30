import time
import json
import pathlib
from random import randint


with open("./ballsData.json", "r") as f:
    ballsConfig = json.load(f)

lastSent = time.time()

def check_stamp():
    global lastSent

    if time.time() - lastSent > 60 * 5:
        lastSent = time.time()
        return True
    else:
        return False
    
def get_ball():
    selectedBall = ballsConfig[0]

    for data in reversed(ballsConfig):
        if randint(1, 3) == 1:
            selectedBall = data
            break

    return selectedBall

def get_ball_by_id(id):
    for ball in ballsConfig:
        if ball["id"] == id:
            return ball
        
    return None

def get_config():
    return ballsConfig
        
    

    
