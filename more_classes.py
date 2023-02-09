#Write all those classes that inherit from BaseModel:

#State (models/state.py):
#Public class attributes:
#name: string - empty string
#City (models/city.py):
#Public class attributes:
#state_id: string - empty string: it will be the State.id
#name: string - empty string
#Amenity (models/amenity.py):
#Public class attributes:
#name: string - empty string
#Place (models/place.py):
#Public class attributes:
#city_id: string - empty string: it will be the City.id
#user_id: string - empty string: it will be the User.id
#name: string - empty string
#description: string - empty string
#number_rooms: integer - 0
#number_bathrooms: integer - 0
#max_guest: integer - 0
#price_by_night: integer - 0
#latitude: float - 0.0
#longitude: float - 0.0
#amenity_ids: list of string - empty list: it will be the list of Amenity.id later
#Review (models/review.py):
#Public class attributes:
#place_id: string - empty string: it will be the Place.id
#user_id: string - empty string: it will be the User.id
#text: string - empty string

from models.base_model import Basemodel

class State(BaseModel):
    name = ""
class City(Basemodel):
    state_id = ""
    name = ""
class Amenity(Basemodel):
    name = ""
class Place:
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_batherooms = 0
    max_guest = 0
    price_by_night = 0
    latitudes = 0.0
    longitude = 0.0
    amenity_ids []
class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""


