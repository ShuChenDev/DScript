import time
import pyautogui
import keyboard
import os
safety_words = {'delay', 'press', 'write', 'click', 'moveto', '#', '\n', 'start:', 'end:', 'repeat:', 'delay:'}

def click_image(path):
    while True:
        try:
            pyautogui.click(pyautogui.locateOnScreen(path, confidence=0.9))
            break
        except:
            pass

def key_detection(start_key, end_key, mode): 
    '''
    Return True if start key is pressed, False if end key is pressed
    '''

    try:
        if 'None' in start_key:
            if 'Inf' not in mode:
                return True
            else:
                print ('Must enter a start key if repeat is infinate')
                raise SyntaxError
        print('Waiting for key to be pressed')
        while True:
            if keyboard.is_pressed(end_key) == True:
                print(end_key + ' Pressed')
                return False
            if keyboard.is_pressed(start_key) == True:
                print(start_key + ' Pressed')
                return True
    except:
        print('Error when getting key inputs. \nEnd program')
        return False
    
def get_script_info(script_name):
    '''
    return (start_key, end_key, mode)
    '''
    try:
        path = 'scripts/' + script_name + '/script.txt'
        with open(path, 'r') as f:
            lines = f.readlines()

        start = 'None'
        end = 'None'
        mode = 'None'
        delay = '0'
        
        
        for i in range(len(lines)):
            setting = lines[i].split(' ')
            if setting[0] == 'start:':
                start = setting[1]
            elif setting[0] == 'end:':
                end = setting[1]
            elif setting[0] == 'repeat:':
                mode = setting[1]
            elif setting[0] == 'delay:':
                delay = setting[1]
                
        start = start.split('\n')[0]
        end = end.split('\n')[0]
        mode = mode.split('\n')[0]
        delay = delay.split('\n')[0]
        
        print('Start key: ' + start)
        print('end key: ' + end)
        print('repeat: ' + mode)
        print('standard delay: ' + delay)

        return (start, end, mode, float(delay))
    except:
        print('Error when getting script info')
        quit()

def run_script(script_name, interval):
    print('\n' * 3 + 'Running Script')
    path = 'scripts/' + script_name + '/'
    try:
        with open(path + 'script.txt') as f:
            lines = f.readlines()
        print('*' * 16 + '\n')
    except:
        print('Error when running the script. \nEnd program')
        quit()


    for i in range(len(lines)):            
        l = lines[i].split(' ', 1)
        command = l[0]
        if len(l) > 1:
            arg = l[1]
        
        if command not in safety_words:
            raise SyntaxError('Line ' + str(i + 1) + ' contains unknown command: ' + command + '\nEnd program')
        
        ############ Execute script ############
        # delay arg secondsss before executing next command
        if command == 'delay':
            print('Pause for ' + str(arg) + ' seconds')
            time.sleep(int(arg))
            continue

        # Click a Place on screen, 1 arg will click on image, 2 arg will click on coordinate
        elif command == 'click': 
            arg = arg.split()                
            #Click Image
            if len(arg) == 0:
                print('click')
                pyautogui.click()
            if len(arg) == 1:
                print('click image: ' + path + arg[0])
                click_image(path + arg[0])
                print('image clicked: ' + path + arg[0])
            #Click Coordinate
            elif len(arg) == 2:
                pyautogui.click(arg[0],arg[1])
                print('click coordinate x: ' + arg[0] + ' y: ' + arg[1])
        # Move to a Place on screen, 1 arg will move to an image, 2 arg will move to coordinate
        elif command == 'moveto': 
            arg = arg.split()                
            #Move to Image
            if len(arg) == 1:
                print('Move to image: ' + path + arg[0])
                pyautogui.moveTo(path + arg[0])
            #Move to Coordinate
            elif len(arg) == 2:
                pyautogui.moveTo(arg[0],arg[1])            
                print('Move to coordinate x: ' + arg[0] + ' y: ' + arg[1])
        
        
        # keyboard input arg
        elif command == 'write':
            arg = arg.replace('\n', '')
            print('write ' + arg)
            pyautogui.write(arg)
        
        # press key in keyboard --- for more information ref to https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys 
        elif command == 'press':
            print('press ' + arg)
            pyautogui.press(arg)

        if l[0] == '\n' or command == 'start:' or command == 'end:' or command == 'repeat:' or command == 'delay:' or command == '#':
            continue
        else:
            print('Pause for ' + str(interval) + ' seconds')
            time.sleep(interval)
    
    print('*' * 16 + '\n')

script_name = 'test'
start, end, repeat, delay  = get_script_info(script_name)
pyautogui.FAILSAFE = False


repeat_count = 0
while ('None' in repeat or 'Inf' in repeat) or repeat.isdigit() and repeat_count < int(repeat):
    
    if not key_detection(start, end, repeat):
        print('1 End program')
        quit()            
    os.system('cls')
    run_script(script_name, delay)
    repeat_count += 1
    
    if 'None' in repeat:
        print('2 End program')
        quit()    


print('3 End program')
quit()
