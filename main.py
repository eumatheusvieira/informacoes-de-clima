import requests

API_Key = "58c340d4b48bb52d0810a8a5d1bde50e"

cidade = input("DIGITE O NOME DA CIDADE:\n")

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_Key}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
temperatura = int(temperatura)
print(descricao, f"{temperatura}ºC")