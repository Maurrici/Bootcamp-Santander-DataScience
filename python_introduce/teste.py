import pyautogui
import time

card6 = "544731"

name = "Evelyn"
lastName = "Braga Mendonça"
cpf = "06029211390"
birthday = "12/11/2001"
cie = "36159511163661316"
dateCard = "30/04/2024"
instituition = "Universidade Federal do Ceará - UFC"
city = "Caucaia"
state = "CE"
course = "Sistemas e Mídias Digitais"

# while False:
#     # Refresh
#     pyautogui.moveTo(2000, 50, duration = 0.3)
#     pyautogui.click()

#     # Botão Ingressos
#     pyautogui.moveTo(4200, 1150, duration = 0.3)
#     pyautogui.click()

#     # Premium
#     pyautogui.moveTo(3381, 730, duration = 0.3)
#     pyautogui.click()

#     # Inferior
#     pyautogui.moveTo(3519, 754, duration = 0.8)
#     pyautogui.click()

#     time.sleep(2)

# # Clique 1 - Seguro (629, 677)
# pyautogui.click(629, 677)

# # Clique 2 - Next page (904, 892)
# pyautogui.click(904, 892)
 
# # Clique 3 - Confirmação (942, 847)
# pyautogui.click(942, 847)

# # Clique 4 - Campo de 6 dígitos do cartão (443, 579)
# pyautogui.click(443, 579)

# # Digitar 6 dígitos
# pyautogui.typewrite(card6) 

# # Clique 5 - Confirmar cartão (687, 678)
# pyautogui.click(687, 678)


# time.sleep(5)

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
pyautogui.click(1097, 872)
pyautogui.scroll(1000)