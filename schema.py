from enum import Enum
from pydantic import BaseModel, field_validator
from datetime import date


class GenreURLChoices(Enum):
    ROCK = 'rock'
    POP = 'pop'
    METAL = 'metal'

class GenreURLChoices(Enum):
    ROCK = 'Rock'
    POP = 'Pop'
    METAL = 'Metal'
    
class Album(BaseModel):
    title: str
    release_date: date

 
class BandBase(BaseModel):
    '''
    {'id':1,'name':'Linkin Park','genre':'Rock'}
    '''
    id : int 
    name: str
    genre: GenreURLChoices
    albums: list[Album] = []  ## default value
    
class BandCreate(BandBase):
    @field_validator('genre')
    def validate_genre(cls, value):
        if value not in GenreURLChoices:
            raise ValueError(f"Invalid genre: {value}. Must be one of {[choice.value for choice in GenreURLChoices]}")
        return value

class BandWithID(BandBase):
    id: int