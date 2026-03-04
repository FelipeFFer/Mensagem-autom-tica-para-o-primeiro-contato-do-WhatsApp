# 🤖 Automação de "Bom Dia" no WhatsApp

Este projeto é uma automação simples desenvolvida em **Python** que utiliza a biblioteca **PyAutoGUI** para abrir o WhatsApp Desktop e enviar uma mensagem automática para o primeiro contato da lista.

## 📋 Como o Script Funciona
O robô segue os seguintes passos:
1. Pressiona a tecla `Windows`, digita "WhatsApp" e abre o aplicativo.
2. Aguarda o carregamento e clica na posição do primeiro contato.
3. Clica no campo de digitação e envia uma sequência de mensagens.
4. Finaliza fechando a janela do WhatsApp.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **PyAutoGUI**: Para controle do mouse e teclado.
* **Time**: Para gerenciar os intervalos de espera entre as ações.

## 🚀 Como Configurar e Rodar

### 1. Instale as dependências
Abra o seu terminal e instale a biblioteca necessária:
- bash
- ip install pyautogui
