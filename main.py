import time
import pyautogui
import keyboard
import os

safety_words = {'delay', 'press', 'write', 'click', 'clickall', 'moveto', '#', '\n', 'start:', 'end:', 'repeat:', 'delay:'}
#pyautogui.FAILSAFE = False

def click_image(path):
    while True:
        try:
            pyautogui.click(pyautogui.locateOnScreen(path, confidence=0.9))
            break
        except:
            pass

def click_all_image(path):
        try:
            targetLocation = pyautogui.locateAllOnScreen(path, confidence=0.9)
            for i in targetLocation:
                pyautogui.click(i)            
        except:
            pass
        
def moveto_image(path):
    while True:
        try:
            pyautogui.moveTo(pyautogui.locateOnScreen(path, confidence=0.9))
            break
        except:
            pass

def key_detection(start_key, end_key, mode): 
    '''
    Return True if start key is pressed, False if end key is pressed
    '''
    try:
        if 'None' in end_key and 'None' not in mode:
            print('Must have a end key')
            raise SyntaxError
        if start_key == end_key and 'None' not in start_key:
            print('Must have different start and end key')
            raise SyntaxError
        
        if 'None' in start_key:
            return True

        print('Waiting for key to be pressed')
        while True:
            if keyboard.is_pressed(start_key) == True:
                print(start_key + ' Pressed')
                return True
            if keyboard.is_pressed(end_key) == True:
                print(end_key + ' Pressed')
                return False
    except:
        print('Error when getting key inputs. \nEnd program')
        quit()
    
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
        
        ############ Delay ############
        # delay arg secondsss before executing next command
        if command == 'delay':
            print('Pause for ' + str(arg) + ' seconds')
            time.sleep(int(arg))
            continue

        ############ Click ############
        # Click a Place on screen, 1 arg will click on image, 2 arg will click on coordinate
        elif command == 'click': 
            if arg == '':
                print('click')
                pyautogui.click()
                continue
            arg = arg.split()                
            if len(arg) == 1:
                print('click image: ' + path + arg[0])
                click_image(path + arg[0])
                print('image clicked: ' + path + arg[0])
            elif len(arg) == 2:
                pyautogui.click(int(arg[0]), int(arg[1]))
                print('click coordinate x: ' + arg[0] + ' y: ' + arg[1])
        
        ############ Click all ############        
        elif command == 'clickall':
            print('click all image: ' + path + arg)
            click_all_image(path + arg)

        ############ Move ############    
        # Move to a Place on screen, 1 arg will move to an image, 2 arg will move to coordinate
        elif command == 'moveto': 
            arg = arg.split()                
            if len(arg) == 1:
                print('Move to image: ' + path + arg[0])
                moveto_image(path + arg[0])
            elif len(arg) == 2:
                pyautogui.moveTo(int(arg[0]), int(arg[1]))            
                print('Move to coordinate x: ' + arg[0] + ' y: ' + arg[1])

        ############ Write ############        
        # keyboard input arg
        elif command == 'write':
            arg = arg.replace('\n', '')
            print('write ' + arg)
            pyautogui.write(arg)

        ############ Press ############        
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



for item in os.listdir('/'):
    item_path = os.path.join('/scripts', item)
    if os.path.isdir(item_path):
        print(item)
        
        
script_name = 'open spotify'

start, end, repeat, delay  = get_script_info(script_name)
repeat_count = 0
while ('None' in repeat or 'Inf' in repeat) or repeat.isdigit() and repeat_count < int(repeat):
    
    if not key_detection(start, end, repeat):
        print('End key detected. End program')
        quit()            
    
    os.system('cls')
    run_script(script_name, delay)
    repeat_count += 1
    
    if 'None' in repeat:
        print('Repeat end. End program')
        quit()    

print('Repeat end. End program')
quit()
