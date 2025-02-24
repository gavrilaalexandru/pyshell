# main implementation of the shell

from commands.echo_cmd import EchoCommand
from commands.help_cmd import HelpCommand
from utils.parser import parser_cmd


class PyShell:
    def __init__(self):
        self.commands = {
            "echo": EchoCommand(),
            "help": HelpCommand(self),
        }

    def run(self):
        while True:
            try:
                user_input = input("pyshell> ").strip()
                if not user_input:
                    continue

                command_name, args = parser_cmd(user_input)

                if command_name in self.commands:
                    self.commands[command_name].execute(args)
                else:
                    print(f"Command not found: {command_name}")
            except KeyboardInterrupt:
                print("\nExiting PyShell...")
                break
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    shell = PyShell()
    shell.run()
