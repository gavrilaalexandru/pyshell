from commands.ibase_cmd import BaseCommand
import os


class HistoryCommand(BaseCommand):
    def __init__(self):
        self.history = []
        self._load_history()

    def execute(self, args):
        self.display_history()

    def add_command(self, command):
        if command.strip():
            self.history.append(command)
            self._save_history()

    def display_history(self):
        for i, command in enumerate(self.history, start=1):
            print(f"{i}: {command}")

    def _load_history(self):
        histfile = ".pyshell_hist"
        if os.path.exists(histfile):
            with open(histfile, "r") as f:
                self.history = [line.strip() for line in f.readlines()]

    def _save_history(self):
        histfile = ".pyshell_hist"
        with open(histfile, "w") as f:
            f.write("\n".join(self.history))

    def help(self):
        return "history --> Displays the list of previously executed commands"
