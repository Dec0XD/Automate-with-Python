import pyautogui 
from time import sleep

#Passos para fazer a aplicação
#Registar meu usuario
    # 1- Clicar em cadastrar novo usuário
pyautogui.click(983,596, )
    # 2- Clicar em usuario
pyautogui.click(1015,540, )
pyautogui.write('Andre')
    # 3- Clicar em senha
pyautogui.click(1011,569, )
pyautogui.write('12345')
    # 4- Clicar em registrar
pyautogui.click(873,597, )
# Logar usuário
    #1- Clicar em digitar usuarios
pyautogui.click(1015,540, )
pyautogui.write('Andre')
    #2- CLicar em digitar a senha
pyautogui.click(1011,569, )
pyautogui.write('12345')
    #3- clicar em "Entrar"
pyautogui.click(873,597, )
# - Extrair cada produto 
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preço = linha.split(',')[2]
        # - Clicar e digitar produto
        pyautogui.click(699,527, )
        pyautogui.write(produto)
        # - Clicar e digitar quantidade
        pyautogui.click(713,553, )
        pyautogui.write(quantidade)
        # - Clicar e digitar preço
        pyautogui.click(711,577, )
        pyautogui.write(preço)
        # - Clicar em registar
        pyautogui.click(592,735, )
        
