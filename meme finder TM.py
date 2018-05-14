import pyautogui as pg
import webbrowser 

answer= pg. confirm (text="What kind of memes?", title="Choose your meme", buttons =['dank','old','new'])

if answer == "dank":
    webbrowser.open("")

elif answer == "Old":


elif answer == "new":
    
