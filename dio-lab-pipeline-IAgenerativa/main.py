import pandas as pd
import json

# Extração dos dados do arquivo CSV
data = pd.read_csv('SDW2023.csv')
columns = data.columns.values.tolist()
lines = data.values.tolist()
print(lines)
print(columns)

# Transformação dos dados
def generateDict(keys=[], values=[]):
    newDict = dict()
    
    for i in range(len(keys)):
        newDict[keys[i]] = values[i]

    return newDict

users = [generateDict(columns, values) for values in lines]
print(users)

# Carregamento de dados no formato JSON
with open('SDW2023.json', 'w') as outfile:
    json.dump(users, outfile, indent=4)