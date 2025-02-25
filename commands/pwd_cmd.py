import os
from commands.ibase_cmd import BaseCommand


class PwdCommand(BaseCommand):
    def execute(self, args):
        print(os.getcwd())

    def help(self):
        return "pwd --> Prints the current working directory"
