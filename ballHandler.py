import time

lastSent = time.time()

def check_stamp():
    print(int(time.time() - lastSent))
    if time.time() - lastSent > 10:
        lastSent = time.time()
        return True
    else:
        return False
    
