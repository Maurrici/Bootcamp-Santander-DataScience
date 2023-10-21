valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

def calcular_valor_juros(capital, taxa, tempo):
  return capital * (1 + taxa)**tempo
  
valor_final = calcular_valor_juros(valor_inicial, taxa_juros, periodo)

print("Valor final do investimento: R$", valor_final)