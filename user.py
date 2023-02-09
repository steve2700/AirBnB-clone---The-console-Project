#usr/bin/python3
# models/user.py
from models.base_model import BaseModel

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
# models/engine/file_storage.py
# ...
def all(self, cls=None):
    """Return a dictionary of all objects in storage"""
    new_dict = {}
    for key, value in self.__objects.items():
        if cls is None or type(value) is cls:
            new_dict[key] = value
    return new_dict

def new(self, obj):
    """Set in storage the obj with key <obj class name>.id"""
    key = "{}.{}".format(type(obj).__name__, obj.id)
    self.__objects[key] = obj

def save(self):
    """Serialize the storage to JSON file"""
    objects = {}
    for key, value in self.__objects.items():
        objects[key] = value.to_dict()

    with open(self.__file_path, 'w') as f:
        json.dump(objects, f)

def reload(self):
    """Deserialize the JSON file to objects"""
    try:
        with open(self.__file_path, 'r') as f:
            objects = json.load(f)
    except FileNotFoundError:
        return

    for key, value in objects.items():
        self.__objects[key] = classes[value['__class__']](**value)
# console.py
# ...
def do_create(self, line):
    """Create a new instance of the specified class"""
    if not line:
        print("** class name missing **")
        return
    class_name = line.split()[0]
    if class_name not in classes:
        print("** class doesn't exist **")
        return
    obj = classes[class_name]()
    obj.save()
    print(obj.id)

def do_show(self, line):
    """Show the string representation of an instance based on its class name and id"""
    if not line:
        print("** class name missing **")
        return
    class_name, obj_id = self.split_class_id(line)
    if class_name not in classes:
        print("** class doesn't exist **")
        return
    if not obj_id:
        print("** instance id missing **")
        return
    key = "{}.{}".format(class_name, obj_id)
    if key not in storage.all():
        print("** no instance found **")
        return
    obj = storage.all()[key]
`




