# auto mining script

# make sure you have the following modules
import pyautogui as pag
import time
import random
from PIL import ImageGrab # we only want imagegrab module

# ground color (in rgb), adjust as needed
groundColor = (103, 80, 76)

# adjust this if you want to expand or shrink the mining region (x, y)  
minpoint = (690, 629)
maxpoint = (1130, 840)

# the main function
def mine():
    # get random position
    x, y = random.randint(minpoint[0], maxpoint[0]), random.randint(minpoint[1], maxpoint[1]) 
    
    # using pillows imagegrab module to get the mining region
    image = ImageGrab.grab((x-5, y-5, x+5, y+5))

    # prevent accidental clicks on other penguins
    color = (0, 0, 0)
    for dx in range(10):
        for dy in range(10):
            color = image.getpixel((dx, dy))
            if(color != groundColor):
                return
            
    # click to walk
    print("walking to "+str(x)+", "+str(y))
    pag.click(x, y)
    time.sleep(2.5 + random.uniform(-1.0, 1.0)) # average walking time (adjust as needed)

    # start dancing which is mining in a average situation
    print("starting mining")
    pag.press("d") 
    time.sleep(30 random.uniform(-5.0, 5.0)) # wait 30 seconds which is enough to get most of money (adjust as needed)
    
# we dont want to run this if it is getting used as a module
if __name__ == "__main__":
    while True:
        mine()