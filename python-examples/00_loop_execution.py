import numpy as np
import time

EXEC_TIME = 5
FREQ = 200
DT = 1/FREQ

if __name__ == "__main__":
    start = time.time()
    t = 0.0

    # Print "ROB311 @UM-ROBOTICS" for 5 seconds @200Hz
    
    end = time.time() + EXEC_TIME;
    counter = 0.0
    t = time.time()
    while t < end:
        print("ROB311 @UM-ROBOTICS")
        time.sleep(DT - .0002)
        counter += 1
        t = time.time()

print("# prints: ",counter)
print("actual freq: ",counter/(end-start))