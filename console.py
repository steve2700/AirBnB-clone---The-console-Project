#!/usr/bin/python3
#Write a program called console.py that contains the entry point of the command interpreter:

#You must use the module cmd
#Your class definition must be: class HBNBCommand(cmd.Cmd):
#Your command interpreter should implement:
#quit and EOF to exit the program
#help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
#a custom prompt: (hbnb)
#an empty line + ENTER shouldn’t execute anything
#Your code should not be executed when imported
#Warning:

#You should end your file with:

#if __name__ == '__main__':
 #   HBNBCommand().cmdloop()
#to make your program executable except when imported. Please don’t add anything around - the Checker won’t like it otherwise

import cmd

class HBNBCommand(cmd.Cmd):
    """Class to handle the entry point of the command interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, args):
        """command to exit the program"""
        return True
    def do_EQF(self, args):
        """command to exit the program"""
        return True
    def do_help(self, args):
        """for help in the programm"""
        cmd.Cmd.do_help(self, args)
    def do_emptyline(self, args)
    """Do nothing when emptyline is executed"""
    pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()







