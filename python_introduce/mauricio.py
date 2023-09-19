import pyautogui
import time

card6 = "544731"

name = "Maurício"
lastName = "de Moura dos Santos"
cpf = "60641998309"
birthday = "03/04/2001"
cie = "36158981678334212"
dateCard = "30/04/2024"
instituition = "Universidade Federal do Ceará - UFC"
city = "Caucaia"
state = "CE"
course = "Engenharia de Computação"

cartao = "5502097913456909"
ccv = "853"
expDate = "02/28"

# PREENCHIMENTO DOS DADOS

# Clique 6 - Estudante (249, 884)
pyautogui.click(249, 884)
pyautogui.scroll(-500)

# Clique name
pyautogui.click(314, 264)
pyautogui.typewrite(name)

# Clique sobrenome
pyautogui.click(754, 263)
pyautogui.typewrite(lastName)

# Clique Cpf
pyautogui.click(517, 377)
pyautogui.typewrite(cpf)

# Clique nascimento
pyautogui.click(358, 485)
pyautogui.typewrite(birthday)

# CLique CIE
pyautogui.click(766, 486)
pyautogui.typewrite(cie)

# Clique data expiração
pyautogui.click(388, 603)
pyautogui.typewrite(dateCard)

# Clique Instituição
pyautogui.click(789, 599)
pyautogui.typewrite(instituition)

#Clique Cidade
pyautogui.click(389, 712)
pyautogui.typewrite(city)

# Clique estado
pyautogui.click(866, 704)
pyautogui.typewrite(state)

# Clique Curso
pyautogui.click(298, 821)
pyautogui.typewrite(course)

# Clique Declaraçãoo
pyautogui.click(247, 926)
pyautogui.scroll(-500)

# Clique Save
# pyautogui.click(1097, 872)
# pyautogui.scroll(1000)