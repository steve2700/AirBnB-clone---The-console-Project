#Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

#Now it’s time to re-create an instance with this dictionary representation.

#<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
#Update models/base_model.py:

#__init__(self, *args, **kwargs):
#you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
#*args won’t be used
#if kwargs is not empty:
#each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
#each value of this dictionary is the value of this attribute name
#Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
#otherwise:
#create id and created_at as you did previously (new instance)
import uuid
import datetime from datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.item():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT:%M:%S.%f")
            self.update_at = datetime.strptime(self.updated_at,  "%Y-%m-%dT:%M:%S.%f")
        else:
            self.id =str(uuid.uuid4())
            self.created_at = datetime.now
            self.updated_at = created_at












