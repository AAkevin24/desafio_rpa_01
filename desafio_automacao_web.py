import pyautogui
import time

#Abrir o navegador e abrir o site 
pyautogui.hotkey("win", "r")
pyautogui.typewrite("https://www.gabrielcasemiro.com.br/atividade_pyautogui \n")
pyautogui.press("enter")

time.sleep(5)

#Loop através dos registros no CSV
with open("membros.csv") as f:
    next(f)

    for line in f:
        line=line.strip()
        line=line.split(";")
        print("Dados: ", line)

        name=line[0]
        sex=line[1]
        email=line[2]
        phone=line[3]

        pyautogui.click(pyautogui.locateCenterOnScreen("nome.png", confidence=0.8), duration=1)
        pyautogui.typewrite(name, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("email.png", confidence=0.8), duration=1)
        pyautogui.typewrite(email, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("telefone.png", confidence=0.8), duration=1)
        pyautogui.typewrite(phone, interval=0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("sexo.png", confidence=0.8), duration=1)

        if sex=="Masculino":
            pyautogui.click(pyautogui.locateCenterOnScreen("masculino.png", confidence=0.8), duration=1)
        else:
            pyautogui.click(pyautogui.locateCenterOnScreen("feminino.png", confidence=0.8), duration=1)

        pyautogui.screenshot(f"cadastro_{name}.png")
        pyautogui.click(pyautogui.locateCenterOnScreen("cadastrar.png", confidence=0.8), duration=1)

        time.sleep(3)

        pyautogui.alert(text="Programa finalizado com sucesso!", title="Aviso do sistema", button="OK")
