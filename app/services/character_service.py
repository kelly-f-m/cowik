from app.utils.tibiadata import fetch_tibiadata


async def get_character_info(name: str) -> str:
    """
    Busca informações de um personagem na API do TibiaData.

    :param name: Nome do personagem.
    :return: Uma string com as informações do personagem ou um erro.
    """
    try:
        response = await fetch_tibiadata(f"character/{name}")
        character_data = response.get("character", {}).get("character", {})

        if not character_data:
            return f"Character {name} doesn't exist."

        char_name = character_data.get("name", "Unknown")
        char_level = character_data.get("level", "Unknown")
        char_voc = character_data.get("vocation", "Unknown")
        char_world = character_data.get("world", "Unknown")

        return f"Character: {char_name} - Level: {char_level} - Vocation: {char_voc} - World: {char_world}"

    except Exception as e:
        return f"Error fetching character data: {str(e)}"
