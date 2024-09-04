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
async def bands() -> list[Band]: 
    '''
    list of band types, which is defined in schema 
    '''
    return [
        Band(**b) for b in BANDS
    ]
'''
The **b syntax in Python is used for unpacking a dictionary into keyword arguments when calling a function or creating an object. In your code snippet, **b is being used to unpack a dictionary into the Band class constructor.

Here's a breakdown of what this means:

Context of the Code
BANDS is likely a list of dictionaries, where each dictionary represents a band's attributes (like name, genre, etc.).
Band is a class or a data structure (like a Pydantic model or a dataclass) that defines the schema or structure for a band object.
Explanation of **b
** is the "dictionary unpacking" operator.
b is each dictionary in the BANDS list.
When you use Band(**b), you are:

Unpacking the dictionary b into keyword arguments.
Passing those keyword arguments to the Band constructor to create an instance of the Band class. 
'''
    


@app.get('/bands/{band_id}')
async def band(band_id:int) -> Band:
    band = next((Band(**b) for b in BANDS if b['id'] == band_id),None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

@app.get('/bands/genre/{genre}')
async def genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value()
    ]