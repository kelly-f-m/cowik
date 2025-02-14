import requests
from utils import format_date

def get_character_info(name):
    tibia_data_url = f"https://api.tibiadata.com/v4/character/{name}"
    
    # Resposta da requisição
    response = requests.get(tibia_data_url)

    if response.status_code == 200:

        # Conteudos da requisição:
        content = response.json()
        informations = content["character"]["character"]

        char_name = informations["name"]
        char_level = informations["level"]
        char_voc = informations["vocation"]
        char_world = informations["world"]
        
        result = f"Character: {char_name} - Level: {char_level} - Vocation: {char_voc} - World: {char_world}"

        return result
    
    return f"Character {name} doesn't exist."

def get_guild_info(name):
    tibia_guild_url = f"https://api.tibiadata.com/v4/guild/{name}"

    # Resposta da requisição
    response = requests.get(tibia_guild_url)

    if response.status_code == 200:

        # Conteúdos da requisição
        content = response.json()
        informations = content["guild"]
        info_levels = content["guild"]["members"]

        guild_name = informations["name"]
        world_name = informations["world"]
        online_members = informations["players_online"]
        total_members = informations["members_total"]
        founded_date = format_date(informations["founded"])

        # Média dos níveis
        info_levels = content["guild"]["members"]

        avg_levels = 0

        for item in info_levels:
            levels = item['level']
            avg_levels += levels / total_members
        print(avg_levels)
        total_levels = round(avg_levels)

        result = f"{guild_name} (World: {world_name} - Avg Level: {total_levels}) has {online_members}/{total_members} members online right now. This guild was founded on {founded_date}."

        return result
    
    return f"Guild {name} doesn't exist."