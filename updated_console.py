#usr/bin/python3


import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, args):
        """Create a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        new_model = eval(class_name + "()")
        new_model.save()
        print(new_model.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, model_id = args[0], args[1]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        model = eval(class_name + ".load(" + model_id + ")")
        if model is None:
            print("** no instance found **")
            return
        print(model)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, model_id = args[0], args[1]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        model = eval(class_name + ".load(" + model_id + ")")
        if model is None:
            print("** no instance found **")
            return
        model.delete()

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        if not args:
            instances = [str(instance) for instance in storage.all().values()]
        else:
            class_name = args.split()[0]
            if class_name not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            instances = [str(instance) for instance in storage.all().values()
                        if type(instance).__name__ == class_name]
        print("[" + ", ".join(instances) + "]")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id





