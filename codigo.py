#  Mandar mensagem de bom dia para seu primeiro contato do whatsapp automático usando PyAutoGUI
# Passo a passo:
# 1 - Abrir o app do whatsapp: 
# Clicar tecla windows
# digitar "whatsapp"
# clicar enter
# 2 - Clicar no primeiro contato da lista
# 3 - Digitar a mensagem "Bom dia!" e clicar enter
import pyautogui
import time

pyautogui.PAUSE = 1 # tempo de pausa entre cada comando 
# Passo 1

pyautogui.press('win')
pyautogui.write('whatsapp')
pyautogui.press('enter')
# Passo 2
time.sleep(5) # dar tempo para o whatsapp abrir
pyautogui.click(x=258, y=253) # clicar no primeiro contato da lista
time.sleep(2) # dar tempo para o contato abrir
# Passo 3
pyautogui.click(x=863, y=977) # clicar na caixa de texto
pyautogui.write('Bom dia!')
pyautogui.press('enter')

