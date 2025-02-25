import os
from commands.ibase_cmd import BaseCommand


class ClearCommand(BaseCommand):
    def execute(self, args):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system("cls")
        else:
            print("\033[H\033[J", end="")

    def help(self):
        return "clear --> Clears the terminal screen"
