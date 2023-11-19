# main.py
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

DOG_API_BASE_URL = "https://dog.ceo/api"

@app.get("/api/v1/dogs")
async def get_dogs():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{DOG_API_BASE_URL}/breeds/list/all")

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        data = response.json()
        top_level_breeds = list(data["message"].keys())

        return {"dogs": data["message"]}
    except httpx.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Error fetching data from Dog API")
