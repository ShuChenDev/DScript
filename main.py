import time
import pyautogui
import keyboard
       
commands = {'delay', 'press', 'write', 'click', 'moveto', '#', '\n'}

def click_image(path):
    while True:
        try:
            pyautogui.click(pyautogui.locateOnScreen(path, confidence=0.9))
            break
        except:
            pass

def key_detection(start_key, end_key): 
    '''
    Return True if start key is pressed, False if end key is pressed
    '''

    if start_key == 'None':
        return True

    if end_key == 'None':
        return False

    try:
        print('Waiting for key to be pressed')
        while True:
            if keyboard.is_pressed(end_key) == True:
                print(end_key + ' Pressed')
                return False
            if keyboard.is_pressed(start_key) == True:
                print(start_key + ' Pressed')
                return True
    except:
        print('Error when getting key inputs')

def get_script_info(script_name):
    '''
    return (start_key, end_key, mode)
    '''
    path = 'scripts/' + script_name + '/script.txt'
    try:
        with open(path, 'r') as f:
            lines = [line.strip() for line in f.readlines()[:4]]
        
        if len(lines) < 3:
            raise ValueError("File does not contain enough lines for start key, end key, and mode.")
        
        print('Start key:' + lines[0])
        print('end key:' + lines[1])
        print('mode:' + lines[2])
        print('standard delay:' + lines[3])

        return (lines[0], lines[1], lines[2], int(lines[3]))
    except:
        print('Error when getting script info')
        quit()
       
def run_script(script_name):
    print('\n' * 3 + 'Running Script')
    
    path = 'scripts/' + script_name + '/'
    try:
        with open(path + 'script.txt') as f:
            lines = f.readlines()
        print('*' * 16 + '\n')

        for i in range(4, len(lines)):            
            l = lines[i].split(' ', 1)
            command = l[0]
            arg = l[1]
            if command not in commands:
                raise SyntaxError('Line ' + str(i + 1) + ' contains unknown command: ' + command + '\nEnd program')
            
            # Execute Commands
            
            if command == 'click':
                arg = arg.split()
                
                if len(arg) == 1:
                    print('click image: ' + path + arg[0])
                    click_image(path + arg[0])
                    print('image clicked: ' + path + arg[0])

                elif len(arg) >= 2:
                    print('click coordinate x: ' + arg[0] + ' y: ' + arg[1])
                    
            elif command == 'write':
                print('write ' + arg)
                pyautogui.write(arg)
        
        print('*' * 16 + '\n')

    except:
        print('Error when running the script')
        quit()



script_name = 'test'

start, end, repeat, delay  = get_script_info(script_name)

repeat_count = 0

while (repeat == 'None' or repeat == 'Inf') or repeat.isdigit() and repeat_count <= int(repeat):
    if not key_detection(start, end):
        print('End program')
        quit()            

    run_script(script_name)
    repeat_count += 1
    
    if repeat == 'None' or repeat == 'Inf' and end == 'None':
        print('End program')
        quit()    


print('End program')
quit()
    