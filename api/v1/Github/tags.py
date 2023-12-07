import aiohttp
from ..config import repo


async def GetLatestMarseyTag():
    url = f'https://api.github.com/repos/{repo}/tags'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            tags = await response.json()

    marsey_tags = [tag for tag in tags if tag['name'].endswith('-Marsey')]

    latest_tag = marsey_tags[0]['name'].rstrip('-Marsey') if marsey_tags else "v2.3.3"
    return latest_tag


async def GetLatestMarseyMTag():
    url = f'https://api.github.com/repos/{repo}/tags'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            tags = await response.json()

    marsey_m_tags = [tag for tag in tags if tag['name'].endswith('-Marsey-M')]

    latest_tag = marsey_m_tags[0]['name'].rstrip('-Marsey-M') if marsey_m_tags else "v2.3.3"
    return latest_tag
