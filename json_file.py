#Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

#models/engine/file_storage.py
#Private class attributes:
#__file_path: string - path to the JSON file (ex: file.json)
#__objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
#Public instance methods:
#all(self): returns the dictionary __objects
#new(self, obj): sets in __objects the obj with key <obj class name>.id
#save(self): serializes __objects to the JSON file (path: __file_path)
#reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
#Update models/__init__.py: to create a unique FileStorage instance for your application

#import file_storage.py
#create the variable storage, an instance of FileStorage
#call reload() method on this variable
#Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage

#import the variable storage
#in the method save(self):
#call save(self) method of storage
#__init__(self, *args, **kwargs):
#if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage

import json
from datetime import datetime


class FileStorage:
    """serializes instances to Json file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary objects"""
        return FileStorage.__objects
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.name__ + "." + obj.id
        FileStorage = .__object[key] = value
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as f:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)
    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
                for key, value in FileStorage.__objects.items():
                    class_name = value["__class__"]
                    class_name = eval(class_name)
                    FileStorage.__objects[key] = class_name(**value)
        except FileNotFoundError:
            pass

 from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()








