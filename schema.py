from enum import Enum
from pydantic import BaseModel
from datetime import date


class GenreURLChoices(Enum):
    ROCK = 'rock'
    POP = 'pop'
    METAL = 'metal'
    
class Album(BaseModel):
    title: str
    release_date: date

 
class Band(BaseModel):
    '''
    {'id':1,'name':'Linkin Park','genre':'Rock'}
    '''
    id : int 
    name: str
    genre: str
    albums: list[Album] = []  ## default value
    
