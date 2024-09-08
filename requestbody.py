from fastapi import FastAPI, HTTPException
from schema import BandWithID, GenreURLChoices, Album, BandCreate

app = FastAPI()

# Data
BANDS = [
    {'id': 1, 'name': 'Linkin Park', 'genre': 'Rock'},
    {'id': 2, 'name': 'Creed', 'genre': 'Rock'},
    {'id': 3, 'name': 'Radiohead', 'genre': 'Metal'},
    {'id': 4, 'name': 'Maroon 5', 'genre': 'Pop'},
    {'id': 5, 'name': '5-SOS', 'genre': 'Rock'},
    {'id': 6, 'name': 'Coldplay', 'genre': 'Pop'}
]

@app.get('/bands')
async def get_bands(genre: GenreURLChoices | None = None, has_albums: bool = False) -> list[BandWithID]: 
    '''
    Fetch a list of bands with optional filters by genre and album availability.
    '''
    band_list = [BandWithID(**b) for b in BANDS]
    if genre:
        band_list = [b for b in band_list if b.genre.lower() == genre.value]

    if has_albums:
        band_list = [b for b in band_list if 'albums' in b and len(b.albums) > 0]
        
    return band_list

@app.get('/bands/{band_id}')
async def get_band_by_id(band_id: int) -> BandWithID:
    band = next((BandWithID(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

@app.get('/bands/genre/{genre}')
async def get_bands_by_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]

@app.post("/bands")
async def create_band(band_data: BandCreate) -> BandWithID:
    new_id = BANDS[-1]['id'] + 1
    band = BandWithID(id=new_id, **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band
# print(BANDS[-1]['id'] + 1)