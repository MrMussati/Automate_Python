import pyautogui as spam    
import time 

limite_msg = input('Enter numero de mengs :')
mgs = input ('Coloque a mesg:')

i = 0 

time.sleep(2)

while i<int(limite_msg):
    spam.typewrite(mgs)
    spam.press('Enter')

    i+=1

   