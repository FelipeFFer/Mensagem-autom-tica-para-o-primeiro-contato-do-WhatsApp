import time
import pyautogui
# dar tempo para o usuário abrir o whatsapp e posicionar o mouse no local correto
time.sleep(6)
pyautogui.position()
print(pyautogui.position())