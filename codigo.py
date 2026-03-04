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

pyautogui.PAUSE = 2 # tempo de pausa entre cada comando 
# Passo 1

pyautogui.press('win')
pyautogui.write('whatsapp')
pyautogui.press('enter')
# Passo 2
time.sleep(3) # dar tempo para o whatsapp abrir
pyautogui.click(x=258, y=253) # clicar no primeiro contato da lista
time.sleep(2) # dar tempo para o contato abrir
# Passo 3
pyautogui.click(x=863, y=977) # clicar na caixa de texto
pyautogui.write('Bom dia!')
pyautogui.press('enter')
pyautogui.write('Um instante, estou enviando esta mensagem automaticamente usando PyAutoGUI!')
pyautogui.press('enter')
pyautogui.write('Tenha um ótimo dia!')
pyautogui.press('enter')
pyautogui.hotkey('alt', 'f4') # fechar o whatsapp

