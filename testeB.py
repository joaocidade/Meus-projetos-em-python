import requests
import webbrowser

api_key = "V7wcscMm12k2aJcrJh7oacrgKyDdmYxzt7nuASY5"
url = "https://api.nasa.gov/planetary/apod"
params = {'api_key': api_key}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    image_url = data.get('url')
    title = data.get('title')
    explanation = data.get('explanation')   

    if image_url:
        print(f"Título: {title}")
        print(f"Descrição: {explanation}")
        webbrowser.open(image_url)
    else:
        print("Nenhuma imagem disponível.")
else:
    print("Erro ao obter a imagem:", response.status_code)
