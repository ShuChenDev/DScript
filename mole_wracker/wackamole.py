#https://crazygames-poki.com/hypercasual/whack-a-mole-3

import os
import pyautogui, sys

try:
    while True:
        try:
            targetLocation = pyautogui.locateAllOnScreen('target.png', confidence=0.9, region=(1140, 250, 1750-1140, 750-250))
            for i in targetLocation:
                pyautogui.click(i)            
            boss_round = False
        except:
            try:
                while True:
                    targetLocation = pyautogui.locateOnScreen('target2.png', confidence=0.85, region=(1140, 250, 1750-1140, 750-250))
                    pyautogui.click(targetLocation, clicks=5, interval=0)
            except:
                pass            
                    

            
except KeyboardInterrupt:
    pass

# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')
