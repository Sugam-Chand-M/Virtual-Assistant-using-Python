import os
import subprocess as sp

# -------------Specify the paths of the applications to be accessed--------------
paths={
    'notepad':"C:\\Windows\\System32\\notepad.exe",
    'calculator':"C:\\Windows\\System32\\calc.exe"
}

# -------------Functions used to open the Applications---------------------------
def open_camera():     #function is used to open the camera
    sp.run('start microsoft.windows.camera:',shell=True)

def open_notepad():    #function used to open the notepad
    os.startfile(paths['notepad'])

def open_calculator():  #function used to open the calculator
    sp.Popen(paths['calculator'])

def open_cmdprompt():   #function used to open the command prompt
    os.system('start cmd')



