# echo command implementation goes here

from commands.ibase_cmd import BaseCommand


class EchoCommand(BaseCommand):
    def execute(self, args):
        print(" ".join(args))

    def help(self):
        return "echo [text] --> Prints the given text"
