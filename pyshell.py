# main implementation of the shell

from commands.echo_cmd import EchoCommand
from commands.help_cmd import HelpCommand
from commands.ls_cmd import LsCommand
from commands.pwd_cmd import PwdCommand
from commands.clear_cmd import ClearCommand
from commands.history_cmd import HistoryCommand
from commands.cd_cmd import CdCommand
from utils.parser import parser_cmd
from utils.readline_util import _load_readline_history
import os


class PyShell:
    def __init__(self):
        self.commands = {
            "echo": EchoCommand(),
            "ls": LsCommand(),
            "pwd": PwdCommand(),
            "clear": ClearCommand(),
            "help": HelpCommand(self),
            "history": HistoryCommand(),
            "cd": CdCommand(),
        }
        self.history_cmd = self.commands["history"]
        _load_readline_history()

    def run(self):
        while True:
            try:
                current_dir = os.getcwd()
                user_input = input(f"pyshell [{current_dir}]> ").strip()
                if not user_input:
                    continue

                self.history_cmd.add_command(user_input)

                command_name, args = parser_cmd(user_input)

                if command_name in self.commands:
                    self.commands[command_name].execute(args)
                elif command_name == "exit":
                    break
                else:
                    print(f"\033[31mCommand not found: {command_name}\033[0m")
            except KeyboardInterrupt:
                print("Exiting PyShell...")
                break
            except EOFError:
                print("Received EOF. Exiting PyShell...")
                break
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    shell = PyShell()
    shell.run()
