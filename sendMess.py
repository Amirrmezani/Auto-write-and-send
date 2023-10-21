import pyautogui
import time
from colorama import Fore
try:
    number = int(input(Fore.RED +'Enter number of messages>>> '))
except:
    print("Enter Number not Character >>> ")
message = input('Enter message content >>> ')

time.sleep(2)

for num in range(number):
    pyautogui.write(message)
    pyautogui.press('enter')

print(Fore.GREEN +'Script executed successfully'+Fore.WHITE)