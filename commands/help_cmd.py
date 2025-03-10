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
                print(f"\033[31mNo help available for command: {command_name}\033[0m")
        else:
            print("\033[34mAvailable commands:")
            for command_name in self.shell.commands:
                print(f"\033[34m - {command_name}\033[0m")

    def help(self):
        return "help [command] --> Displays information about available commands"
