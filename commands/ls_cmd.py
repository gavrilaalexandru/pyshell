import os
import shutil
from commands.ibase_cmd import BaseCommand


class LsCommand(BaseCommand):
    def execute(self, args):
        path = args[0] if args else "."

        try:
            contents = os.listdir(path)
            visible_contents = [item for item in contents if not item.startswith(".")]
            self.print_multi_line(visible_contents)
        except FileNotFoundError:
            print(f"Directory not found: {path}")
        except PermissionError:
            print(f"Permission denied: {path}")
        except Exception as e:
            print(f"Unknown error: {e}")

    def help(self):
        return "ls [path] --> Lists the contents of the specified directory/current directory"

    def print_multi_line(self, contents):

        terminal_width = shutil.get_terminal_size().columns

        current_line_length = 0
        for item in contents:
            item_length = len(item) + 2

            if current_line_length + item_length > terminal_width:
                print()
                current_line_length = 0

            print(item, end=" ")
            current_line_length += item_length

        print()
