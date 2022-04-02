import pyautogui 
from time import sleep

pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True
#переміщення
#pyautogui.move(-19, -19, duration=0.5)
#one click
#pyautogui.click(interval=0.5)
#правий клік
#pyautogui.rightClick()

#двоїне 
#pyautogui.doubleClick()
#скрол верх
#pyautogui.vscroll(200)
#cкрол вниз
#pyautogui.hscroll(200)

#переміщення з зажатою кнопкою
#print(pyautogui.position())
#pyautogui.moveTo(337, 271, duration=1)
#pyautogui.dragTo(67, 270, duration=1)


#sleep(0.5)
#pyautogui.typewrite('niaaaaaa',interval=0.2)

#press hotkey нажиття 
#pyautogui.press('enter')
#нажиття комбінованих клавіш
#pyautogui.hotkey('ctrl', 'a')

#пошук по фотографії (x, y більш надійно)
#sleep(2)
#x, y = print(pyautogui.locateCenterOnScreen(r"C:\Users\denis\Documents\Lightshot\Screenshot_43.png"))
sleep(5)
#pyautogui.click(x, y)
#print(pyautogui.size())
print(pyautogui.position())