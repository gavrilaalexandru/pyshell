# here goes the base class for all the shell commands


class BaseCommand:
    def execute(self, args):
        raise NotImplementedError("Subclasses must implement this method")

    def help(self) -> str:
        return "No help available for this command"
