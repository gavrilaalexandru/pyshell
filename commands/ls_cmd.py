import os
from commands.ibase_cmd import BaseCommand


class LsCommand(BaseCommand):
    def execute(self, args):
        path = args[0] if args else "."

        try:
            contents = os.listdir(path)
            print("\n".join(contents))
        except FileNotFoundError:
            print(f"Directory not found: {path}")
        except PermissionError:
            print(f"Permission denied: {path}")
        except Exception as e:
            print(f"Unknown error: {e}")

    def help(self):
        return "ls [path] --> Lists the contents of the specified directory/current directory"
