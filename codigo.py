import pyautogui
import time


# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> aperta 1 tecla
# pyautogui.write - > escrever um texto
# pyautogui.hotkey -> apertar combinação de teclas

pyautogui.PAUSE = 1
# passo 1: entrar site da empresa -> https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# digitar o site
pyautogui.click(x=311,y=72)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#espera 3 segundos
time.sleep(3)

#passo 2: fazer login
pyautogui.click(x=397,y=558)
pyautogui.write("pythonimptessionador@gmail.com")

pyautogui.press("tab")
pyautogui.write("minhasenhasupersecreta")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# passo 3 :> importar base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

#passo 4: cadastrar 1 procuto
for linha in tabela.index: #para cada linha da minha tabela
    pyautogui.click()

    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)

    marca =  tabela.loc[linha,"marca"]
    pyautogui.press("tab")
    pyautogui.write(marca)

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.press("tab")
    pyautogui.write(tipo)

    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)

    custo = str(tabela.loc[linha,"custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    obs = tabela.loc[linha,"obs"]
    pyautogui.press("tab")
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)

#passo 5: cadastrar todos os produtos
 
       
