from app.utils.tibiadata import fetch_tibiadata
from app.utils.date import format_date


async def get_guild_info(name: str) -> str:
    """
    Busca informações de uma guild na API do TibiaData.

    :param name: Nome da guild.
    :return: Uma string com as informações da guild ou um erro.
    """
    try:
        response = await fetch_tibiadata(f"guild/{name}")
        guild_data = response.get("guild", {})
        members = guild_data.get("members", [])

        if not guild_data:
            return f"Guild {name} doesn't exist."

        guild_name = guild_data.get("name", "Unknown")
        world_name = guild_data.get("world", "Unknown")
        online_members = guild_data.get("players_online", 0)
        total_members = guild_data.get("members_total", 0)
        founded_date = format_date(guild_data.get("founded", "Unknown"))

        avg_levels = 0
        for member in members:
            levels = member["level"]
            avg_levels += levels / total_members

        total_levels = round(avg_levels)

        result = (
            f"{guild_name} (World: {world_name} - Avg Level: {total_levels}) "
            f"has {online_members}/{total_members} members online right now. "
            f"This guild was founded on {founded_date}."
        )

        return result

    except Exception as e:
        return f"Error fetching guild data: {str(e)}"
