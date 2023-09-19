# Lower, Upper and Capitalize
name = "MAUricio"

print(name.upper())
print(name.lower())
print(name.title())
print("\n")

# Removing white spaces
course = "    Python  "

print(course.strip())
print(course.rstrip())
print(course.lstrip())
print("\n")

# Join and Center
anime = "One Piece"

print(anime.center(20, '#'))
print(".".join(anime))
print("\n")

#Interpolação

name = "Maurício"
age = 22
role = "dev"
num = 12.2134123

print("Olá me chamo %s. Eu tenho %d anos e trabalho com %s e sonho em ser um desenvolvedor inspirador!" % (name, age, role))
print("\n")
print("Olá me chamo {}. Eu tenho {} anos e trabalho com {} e sonho em ser um desenvolvedor inspirador!".format(name, age, role))
print("\n")
print(f"Olá me chamo {name}. Eu tenho {age} anos e trabalho com {role} e sonho em ser um desenvolvedor inspirador! Num {num: .2f}")
print("\n")

# Fatiamento
name = "Maurício de Moura dos Santos"

print(name[0])
print(name[:12])
print(name[12:])
print(name[22:28])
print(name[22:28:2])
print(name[:])
print(name[::-1])