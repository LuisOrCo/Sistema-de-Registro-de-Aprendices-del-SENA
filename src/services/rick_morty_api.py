import httpx
import random

API_URL = "https://rickandmortyapi.com/api/character"

async def get_random_character(character_id=None):
    """Obtiene un personaje aleatorio o uno específico por ID."""

    if character_id is None:
        character_id = random.randint(1, 826)

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}/{character_id}", timeout=5.0)

            if response.status_code == 200:
                data = response.json()

                return {
                    "id": data.get("id"),
                    "name": data.get("name"),
                    "status": data.get("status"),
                    "species": data.get("species"),
                    "gender": data.get("gender"),
                    "origin": data.get("origin"),
                    "location": data.get("location"),
                    "image": data.get("image")
                }

    except Exception as e:
        print(f"Error: {e}")

    return None