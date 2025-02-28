# help command implementation

from commands.ibase_cmd import BaseCommand


class HelpCommand(BaseCommand):
    def __init__(self, shell):
        self.shell = shell

    def execute(self, args):
        if args:
            command_name = args[0]
            if command_name in self.shell.commands:
                print(self.shell.commands[command_name].help())
            else:
                print(f"No help available for command: {command_name}")
        else:
            print("Available commands:")
            for command_name in self.shell.commands:
                print(f" - {command_name}")

    def help(self):
        return "help [command] --> Displays information about available commands"
