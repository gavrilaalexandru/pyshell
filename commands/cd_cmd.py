import os
from commands.ibase_cmd import BaseCommand


class CdCommand(BaseCommand):
    def execute(self, args):
        if not args:
            new_dir = os.path.expanduser("~")
        else:
            new_dir = args[0]

        try:
            os.chdir(new_dir)
            print(f"Changed directory to {new_dir}")
        except FileNotFoundError:
            print(f"Directory not found: {new_dir}")
        except PermissionError:
            print(f"Permission denied: {new_dir}")
        except Exception as e:
            print(f"Unknown error: {e}")

    def help(self):
        return "cd [path] --> Changes the current directory"
