#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb)"
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review}

    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """

        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            my_model = dct[line]()
            print(my_model.id)
            my_model.save()

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id
        """

        if not line or line == "":
            print("** class name missing **")
        args = line.split()
        if len(args) == 2:
            if args[0] in self.classes:
                key = args[0] + '.' + args[1]
                rec_of_instances = storage.all()
                if key not in rec_of_instances:
                    print("** no instance found **")
                    return
                else:
                    print(rec_of_instances[key])
                    return
            else:
                print("** class doesn't exist **")
                return
        elif len(args) == 1:
            print("** instance id missing **")
            return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """

        if not line or line == "":
            print("** class name missing **")
        args = line.split()
        if len(args) == 2:
            key = args[0] + '.' + args[1]
            if key not in rec_of_instances:
                print("** no instance found **")
            else:
                del rec_of_instance[key]
                storage.save()
        elif len(args) == 1:
            print("** instance id missing **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """
        key_list = []
        instances = storage.all()
        if len(line) == 0:
            for v in instances.values():
                key_list.append(v.__str__())
            print(key_list)
            return
        line_list = line.split()
        if line_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        for v in instances.values():
            if line_list[0] == v.__class__.__name__:
                key_list.append(v.__str__())
        print(key_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).
        Args:
            line - user input
        """

        rec_of_instances = storage.all()
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        elif len(args) == 2:
            print('** attribute name missing **')
            return
        elif len(args) == 3:
            print('** value missing **')
            return
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            key = args[0] + '.' + args[1]
            if key not in rec_of_instances:
                print('** no instance found **')
            else:
                a3 = args[3].strip('\"')
                if hasattr(key, args[2]) is True:
                    attr_type = type(getattr(key, args[2]))
                    if attr_type == int:
                        setattr(rec_of_instances[key], args[2], int(a3))
                        storage.save()
                    elif attr_type == float:
                        setattr(rec_of_instances[key], args[2], float(a3))
                        storage.save()
                else:
                    setattr(rec_of_instances[key], args[2], a3)
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
