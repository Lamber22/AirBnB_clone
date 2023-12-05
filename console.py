#!/usr/bin/python3
#console.py

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        print("")
        return True

    def do_EOF(self, arg):
        """CRTL+D/EOF signal to exit the program."""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
