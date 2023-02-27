import requests
import pandas as pd

tabela = pd.read_excel("Envios.xlsx")

telefones = [tabela.loc[linha, "telefone"] for linha in tabela.index]
nomes = [tabela.loc[linha, "nome"] for linha in tabela.index]

inf = {
	"number": "5511963862828",
	"message": "salve"
}

data = dict(zip(nomes, telefones))

for result in data.items():
    
    inf = {
        "number": f"55{result[1]}",
	    "message": f'olioioi {result[0]}'
    }
    req = requests.post('http://localhost:8005/send-message', data=inf)
    print(req)









# #     # wpp = str(telefone)
# #     # wpp = wpp[:-2]

# #     # import ipdb; ipdb.set_trace()

# #     texto = mensagem.replace("fulano", nome)
# #     texto = urllib.parse.quote(texto)

# #     link = f"https://web.whatsapp.com/send?phone=+55{telefone}&text={texto}"

# #     navegador.get(link)
# #     if len(navegador.find_elements(By.ID, 'side')) < 1:
# #         time.sleep(12)
    
# #     time.sleep(2)

    

# #     navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
# #     time.sleep(2)

# # # como voce vai selecionar, qual o codigo de selecionar





# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.by import By
# # import pandas as pd
# # import urllib
# # import time

# # navegador = webdriver.Chrome()

# # navegador.get("https://web.whatsapp.com/")

# # if len(navegador.find_elements(By.ID, 'side')) < 1:
# #     time.sleep(12)
    
# # time.sleep(2)