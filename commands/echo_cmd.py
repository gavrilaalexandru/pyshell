# echo command implementation goes here

from commands.ibase_cmd import BaseCommand


class EchoCommand(BaseCommand):
    def execute(self, args):
        text = " ".join(args)
        print(text.encode().decode("unicode_escape"))

    def help(self):
        return "echo [text] --> Prints the given text"
