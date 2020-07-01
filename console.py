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
        if not line:
            return

        if self.count_instances(line):
            return

        if not self.class_method_(line):
            return

        matches = re.search(r'(User|BaseModel|Place|City|Amenity|Review|State).(all|show|destroy|create|all|update)\(([^,]*),?\s?([^,]*),?\s?([^,]*)\)', line)
        if matches:
            classes = matches.group(1)
            command = matches.group(2)
            id_ = matches.group(3)
            att_ = matches.group(4)
            att_value = matches.group(5)
            self.onecmd(command + " " + classes + " " +  id_ + " " + att_ + " " + att_value)
            return

    def count_instances(self, line):
        """count instances
        """
        matches = re.search(
            r'(User|BaseModel|Place|City|Amenity|Review|State).(count)\(\)', line)
        if matches:
            count = 0
            classes = matches.group(1)
            for k, v in FileStorage._FileStorage__objects.items():
                if classes in k:
                    count = count + 1
            print(count)
            return 0
        return 1

    def class_method_(self, line):
        """ <class>.<method>
        """
        matches = re.search(r'(User|BaseModel|Place|City|Amenity|Review|State).(update)\(([^,]*),?\s?({.+})\)', line)
        if matches:
            classes = matches.group(1)
            command = matches.group(2)
            id_ = matches.group(3).strip("\"")
            args_ = matches.group(4)
            args_ = args_.replace("\'", "\"")
            dict_ = json.loads(args_)
            for k, v in dict_.items():
                self.onecmd(command + " " + classes + " " + id_ + " " + str(k) + " " + str(v))
            return 0
        return 1


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
    def do_shell(self, line):
        """ run a shell command
        """
        output = os.popen(line).read()
        self.last_output = output

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
