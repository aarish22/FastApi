from fastapi import FastAPI,HTTPException
from schema import Band,GenreURLChoices,Album


app = FastAPI()


# Data
BANDS = [
    {'id': 1, 'name': 'Linkin Park', 'genre': 'Rock'},
    {'id': 2, 'name': 'Creed', 'genre': 'Rock'},
    {'id': 3, 'name': 'Radiohead', 'genre': 'Metal', 'albums': [
        {'title': 'Hello World', 'release_date': '2011-02-09'},
        {'title': 'Hello World2', 'release_date': '2011-04-04'}
    ]},
    {'id': 4, 'name': 'Maroon 5', 'genre': 'Pop'},
    {'id': 5, 'name': '5-SOS', 'genre': 'Rock'},
    {'id': 6, 'name': 'Coldplay', 'genre': 'Pop'}
]

@app.get('/bands')
async def bands(genre: GenreURLChoices | None = None, has_albums: bool = False) -> list[Band]: 
    '''
    None = none is default value, if not set fast api will expect a 
    query parameter from us
    '''
    band_list = [Band(**b) for b in BANDS]
    if genre:
        band_list = [
            b for b in band_list if b.genre.lower() == genre.value
        ]
    '''
    list of band types, which is defined in schema 
    '''
    if has_albums:
        band_list = [b for b in band_list if len(b.albums) >  0]
    return band_list ## default return entire list of bands


@app.get('/bands/{band_id}')
async def band(band_id:int) -> Band:
    band = next((Band(**b) for b in BANDS if b['id'] == band_id),None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

@app.get('/bands/genre/{genre}')
async def genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]