import os
from commands.ibase_cmd import BaseCommand


class PwdCommand(BaseCommand):
    def execute(self, args):
        if not self.validate_args(args, expected_args=0):
            return
        print(os.getcwd())

    def help(self):
        return "pwd --> Prints the current working directory"
