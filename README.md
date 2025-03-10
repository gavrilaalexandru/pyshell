# PyShell Documentation
## Overview
PyShell is a simple, customizable shell written in Python that supports several basic commands like echo, ls, pwd, cd, and more. This shell allows for running commands, viewing history, and getting help for each command.
## Features
- Command History: Maintains a history of executed commands.
- Basic Shell Commands: Implements common shell commands such as echo, pwd, ls, cd, and more.
- Custom Command Structure: Easy to extend with new commands by subclassing BaseCommand.
## Installation
Ensure you have Python installed. Clone this repository and run the **pyshell.py** script.
```
git clone https://github.com/gavrilaalexandru/pyshell.git
cd pyshell
python pyshell.py
```
## Usage
### Available Commands:
1. echo [text]: Prints the provided text.
2. pwd: Prints the current working directory.
3. ls [path]: Lists the contents of the specified directory.
4. cd [path]: Changes the current working directory to the specified path.
5. clear: Clears the terminal screen.
6. history [-c]: Displays command history. Use -c to clear it.
7. help [command]: Displays information about a specific command or list of available commands.
## Extending PyShell
To add a new command:
1. Create a new class that inherits from BaseCommand.
2. Implement the execute method.
3. Optionally, add a help method to provide description.
