import os
class Automation:
    def __init__(self, script_name):
        self.script_name = script_name
        self.path = 'automation/' + self.script_name
        self.script_path = self.path + "/script.txt"
        
        self.command = {}
        
    def script_init(self):
        try:
            try:
                os.mkdir('automation/' + self.script_name)
                print(f"Directory '{self.script_name}' created successfully.")
        
            except Exception as e:
                
                try:
                    os.mkdir('automation/')
                    print(f"Directory automation created successfully.")
                    os.mkdir('automation/' + self.script_name)
                    print(f"Directory '{self.script_name}' created successfully.")
                except Exception as e:
                    print(f"An error occurred: {e}")
            
            f = open(self.script_path, "w")
            f.close()        
        except Exception as e:
            print(f"An error occurred: {e}")

        
        
        
    def select_image(self):
        try:
            from tkinter import Tk
            from tkinter.filedialog import askopenfilename
            import shutil
            
            Tk().withdraw()
            filename = askopenfilename()
            print(filename)
            shutil.copy(filename, self.path)

        except Exception as e:
            print(f"An error occurred: {e}")
   

    def check_script(self):
        
        f = open(self.script_path, "r")
        for line in f:
            if line not in self.command:
                pass
            
        f.close()

                
        
s = Automation('mole_wracker')
s.check_script()