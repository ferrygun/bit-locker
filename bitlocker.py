from microbit import *
import random
import os
from array import *
import music


def SetSecretPin():
    data = 0
    index = 0
    myPin = list(range(4))
    loop = True
    
    stage = 0
    
    while (loop):
        loop1 = True
        if (button_a.was_pressed() and stage == 0):
            if (data >= 9): 
                data = 0
            else:
                data += 1
            display.show(str(data))
            
        if (button_b.was_pressed() and stage == 0): 
            display.show(str(data))
            if index < 4:
                myPin[index] = data
                for i in range(0,3):
                    display.show(str(myPin[index]))
                    sleep(200)
                    display.clear()
                    sleep(200)
                index += 1
                
                if index >=4:
                    stage = 1
                    display.scroll("Pin Is:")
                    sleep(1000)
                    
                    for i in range(len(myPin)):
                        display.show(str(myPin[i]))
                        sleep(1000)
                        display.clear()
                        sleep(1000)
                    
                    display.scroll("Confirm?")
                    
                    while (loop1):
                        if (button_a.was_pressed() and stage == 1): 
                            SetPin(myPin)
                            display.show("C")
                            music.play(music.JUMP_UP)
                            sleep(1000)
                            loop1 = False
                            stage = 0
                            loop = False
                            
                        if (button_b.was_pressed() and stage == 1):
                            display.show("N")
                            music.play(music.JUMP_UP)
                            stage = 0
                            index = 0
                            loop1 = False
def GetUnlock(p):
    display.show('E')
    music.play(music.JUMP_UP)
    mySPin = p
    mySPin = mySPin[1:]
    mySPin = mySPin[:-1]
    mySPin = mySPin.split(",")
    mySPin = list(mySPin)
        
    data = 0
    index = 0
    Pass = True
    myPin = list(range(4))
    
    loop = True
    while (loop):
        if (str(pin1.read_analog()) !="3"):
            if (get_value() == 1):
                music.play(music.PYTHON)
                
        if button_a.was_pressed():
            if (data >= 9): 
                data = 0
            else:
                data += 1
            display.show(str(data))
            
        if button_b.was_pressed(): 
            display.show(str(data))
            if index < 4:
                myPin[index] = data
                for i in range(0,3):
                    display.show(str(myPin[index]))
                    sleep(200)
                    display.clear()
                    sleep(200)
                index += 1
                
                if index >=4:
                    if(str(myPin[0]) != str(mySPin[0]).strip()):
                        Pass = False
                    if(str(myPin[1]) != str(mySPin[1]).strip()):
                        Pass = False
                    if(str(myPin[2]) != str(mySPin[2]).strip()):
                        Pass = False
                    if(str(myPin[3]) != str(mySPin[3]).strip()):
                        Pass = False   
                        
                    loop = False
                    display.clear()

    return Pass        
        
def PinExists():
    files = os.listdir()
    for f in files:
        if f=="secret.txt":
            return True
    return False
    
def SetPin(p):
    with open('secret.txt', 'w') as h:
        h.write(str(p))

def GetPin():
    with open('secret.txt', 'r') as h:
        a = h.read()
        return str(a)

def get_value():
    global global_variable
    return global_variable

def set_value(new_value):
    global global_variable
    global_variable = new_value
    
global_variable = 1 #1 = activated, 2 = deactivated

#######################################    
def Main():
    while True:
                  
        if (str(pin1.read_analog()) !="3"):
            if (get_value() == 1):
                music.play(music.PYTHON)
        else:
            display.clear()
            
        if (get_value() == 2):
            display.show(Image.HEART)
            if button_a.was_pressed(): 
                set_value(1)
                display.clear()
                music.play(music.JUMP_DOWN) 
                
            if button_b.was_pressed():
                display.show('R')
                music.play(music.JUMP_UP) 
                display.clear()  
                SetSecretPin()
                
        else: 
            if PinExists():
                myPin = GetPin()
               
                if GetUnlock(myPin):
                    for i in range(0,3):
                        display.show(Image.HAPPY)
                        sleep(200)
                        display.clear()
                        sleep(200)
                    music.play(music.POWER_UP) 
                    set_value(2)
                else:
                    for i in range(0,3):
                        display.show(Image.SAD)
                        sleep(200)
                        display.clear()
                        sleep(200)
                    music.play(music.POWER_DOWN) 
            else: 
                display.show('S')
                music.play(music.JUMP_UP)
                SetSecretPin()
        
        
    
Main()       


