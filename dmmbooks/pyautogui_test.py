import pyautogui
import time

# print('Ctrl+Cを押すと終了します')
# try:
#     while True:
#         x,y = pyautogui.position()
#         position = 'X:'+str(x).rjust(4) + ' Y:'+str(y).rjust(4)
#         print(position,end='')
#         print('\b' * len(position),end='',flush=True)
#         pyautogui.sleep(1)
# except KeyboardInterrupt:
#     print('\n終了')

# # # # pyautogui.moveTo(100,100,3)

pyautogui.moveTo(1838, 792, 3)
pyautogui.click()

# pyautogui.write('Hello world!', interval=0.25)



for num in range(5):
    pyautogui.press('left')
    time.sleep(1)
# pyautogui.press(['left', 'left', 'left', 'left'])

# Hello world!Hello world!
# # 2249 1160
# # 1604 168
# # 2548 981
# 1838 792