import readline
import os


def _load_readline_history():
    histfile = ".pyshell_hist"
    if os.path.exists(histfile):
        with open(histfile, "r") as f:
            for line in f.readlines():
                readline.add_history(line.strip())


def _clear_readline_history():
    readline.clear_history()
