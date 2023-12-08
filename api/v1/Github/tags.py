import aiohttp
from ..config import repo

async def GetLatestMarseyTag():
    url = f'https://api.github.com/repos/{repo}/tags'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            tags = await response.json()

    # Filter tags that end with '-Marsey' or '-Marsey-M'
    marsey_tags = [tag for tag in tags if tag['name'].endswith(('-Marsey', '-Marsey-M'))]

    # Remove the suffix and the first character from the latest tag
    latest_tag = marsey_tags[0]['name']
    if latest_tag.endswith('-Marsey-M'):
        latest_tag = latest_tag.rstrip('-Marsey-M')[1:]
    elif latest_tag.endswith('-Marsey'):
        latest_tag = latest_tag.rstrip('-Marsey')[1:]

    return latest_tag if marsey_tags else "2.3.3"



async def GetLatestMarseyMTag():
    url = f'https://api.github.com/repos/{repo}/tags'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            tags = await response.json()

    marsey_m_tags = [tag for tag in tags if tag['name'].endswith('-Marsey-M')]

    latest_tag = marsey_m_tags[0]['name'].rstrip('-Marsey-M')[1:] if marsey_m_tags else "2.3.3"
    return latest_tag
