from fastapi import FastAPI,HTTPException
from enum import Enum
app = FastAPI()

class GenreURLChoices(Enum):
    ROCK = 'rock',
    POP = 'pop',
    METAL = 'metal'



BANDS = [
    {'id':1,'name':'Linkin Park','genre':'Rock'},
    {'id':2,'name':'Creed','genre':'Rock'},
    {'id':3,'name':'Radiohead','genre':'Metal'},
    {'id':4,'name':'Maroon 5','genre':'Pop'},
    {'id':5,'name':'5-SOS','genre':'Rock'},
    {'id':6,'name':'Coldplay','genre':'Pop'}
]


@app.get('/bands')
async def bands() -> list[dict]:
    return BANDS


@app.get('/bands/{band_id}')
async def band(band_id:int) -> dict:
    band = next((b for b in BANDS if b['id'] == band_id),None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

@app.get('/bands/genre/{genre}')
async def genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value()
    ]