#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):

    """Console line interpreter"""
    prompt = "(hbnb) "

    def default(self, line):
        """if no command matches do_*
        """
        self._precmd(line)

    def do_EOF(self, line):
        """what to do when findind EOF
        """
        print()
        return True

    def do_quit(self, line):
        """quit the coomand line interrupted
        """
        return True

    def emptyline(self):
        """what to do on empty line
        """
        pass

    def do_create(self, line):
        """Creates an instance
        """
        if not line:
            print("** class name missing **")
            return
        classes = storage.accepted_classes()
        if line not in classes:
            print("** class doesn't exist **")
            return
        b = classes[line]()
        b.save()
        print(b.id)

    def do_show(self, line):
        """Prints the string representation of an instance.
        """
        if not line:
            print("** class name missing **")
            return

        args_ = line.split(' ')
        classes = storage.accepted_classes()

        if args_[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args_) == 1:
            print("** instance id missing **")
            return


        if not re.search(r'\w+-\w+-\w+-\w+-\w+', args_[1]):
            print("** no instance found **")
            return

        objects = storage.all()
        key_search = args_[0] + '.' + args_[1]
        if key_search not in objects:
            print("** no instance found **")
            return
        try:
            with open("file.json", 'r') as f:
                print(objects[key_search])
        except:
            pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        if not line:
            print("** class name missing **")
            return

        args_ = line.split(' ')
        classes = storage.accepted_classes()

        if args_[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args_) == 1:
            print("** instance id missing **")
            return

        if not re.search(r'\w+-\w+-\w+-\w+-\w+', args_[1]):
            print("** no instance found **")
            return

        objects = storage.all()
        key_search = args_[0] + '.' + args_[1]
        if key_search not in objects:
            print("** no instance found **")
            return

        del objects[key_search]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        args_ = line.split(' ')
        if not line:
            out_ = [v.__str__() for k,v in storage.all().items()]

        elif args_[0] in storage.accepted_classes():
            out_ = [ v.__str__() for k,v in storage.all().items() if args_[0] == type(v).__name__]

        else:
            print("** class doesn't exist **")
            return
        print(out_)

    def do_update(self, line):
        """update the instances of a class.
        """
        if not line:
            print("** class name is missing **")
            return

        class_ = storage.accepted_classes()
        args_ = line.split(' ')

        if args_[0] not in class_:
            print("** class doesn't exist *'*")
            return

        if len(args_) == 1:
            print("** instance id missing **")
            return

        if not re.search(r'\w+-\w+-\w+-\w+-\w+', args_[1]):
            print("** no instance found **")
            return

        key_search = args_[0] + '.' + args_[1]

        if key_search not in storage.all():
            print("** no instance found **")
            return

        if len(args_) == 2:
            print("** attribute name missing **")
            return

        if len(args_) == 3:
            print("** value missing **")
            return
        object_ = storage.all()[key_search]
        object_.__dict__[args_[2]] = args_[3].strip('"')
        object_.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
