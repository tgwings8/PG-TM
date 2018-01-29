import pyautogui as pg
import time

points = 0

answer = pg.prompt (
"""
Which would you rather do?

a) fight aliens and travel to different universes 
b) doing things that are unnescesary for you 
c)taking advantage of father in laws science stuff

"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
answer = pg.prompt (
"""
Which would you rather do?

a) go on crazy science trip 
b) use science for personale problems 
c) or hate your father in law 

"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
answer = pg.prompt (
"""
What is your greatest achievment?

a)being a scientist 
b) 
c)staying home

"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3



#END OF SURVEY
pg.alert("You are...")

#Rick
if points < 5:
    pg.alert("Rick")
webbrowser.open("https://www.google.com/search?q=rick+and+morty&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjW6ojLo_3YAhVpmuAKHbP8Bf0Q_AUICigB&biw=1350&bih=610#imgrc=8XiYzgjz9HeUMM:")

#Morty
if points >= 5 and points <8:
    pg.alert("Morty")
webbrowser.open("https://www.google.com/search?q=morty+from+rick+and+morty&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwje3_aNpP3YAhWKON8KHalbCCgQ_AUICigB&biw=1350&bih=610#imgrc=exaea1gsrJsQyM:")

#Jerry
if points >=8:
    pg.alert ("Jerry")
    

    
