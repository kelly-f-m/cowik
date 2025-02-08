import requests

def get_character_info(name):
    tibia_data_url = f"https://api.tibiadata.com/v4/character/{name}"
    
    # Resposta da requisição
    response = requests.get(tibia_data_url)

    # Conteudos da requisição:
    content = response.json()
    informations = content["character"]["character"]

    char_name = informations["name"]
    char_level = informations["level"]
    char_voc = informations["vocation"]
    char_world = informations["world"]
    
    result = f"Character: {char_name} - Level: {char_level} - Vocation: {char_voc} - World: {char_world}"

    return result
