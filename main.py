import requests
import pandas as pd

table = pd.read_excel("Envios.xlsx")

phones = [table.loc[linha, "telefone"] for linha in table.index]
names = [table.loc[linha, "nome"] for linha in table.index]
values = [table.loc[linha, "valor"] for linha in table.index]

data = []
for i in range(len(names)):
    tupla = (names[i], phones[i], values[i])
    data.append(tupla)


for result in data:
    name, phone, value = result

    inf = {
        "number": f"55{phone}",
        "message": f"OI {name}, caloteiro seu valor dessa semana é esse {value}",
    }

    req = requests.post("http://localhost:7005/send-message", data=inf)
    print(req)
