# here goes the base class for all the shell commands
class MetaCommand(type):
    def __new__(cls, name, bases, dct):
        # Creăm clasa
        new_class = super().__new__(cls, name, bases, dct)

        if "help" in dct:
            original_help = dct["help"]

            def coloured_help(self):
                help_message = original_help(self)
                return f"\033[34m{help_message}\033[0m"  # Verde

            setattr(new_class, "help", coloured_help)

        return new_class


class BaseCommand(metaclass=MetaCommand):
    def execute(self, args):
        raise NotImplementedError("Subclasses must implement this method")

    def validate_args(self, args, expected_args=0):
        if len(args) != expected_args:
            cmd_name = self.__class__.__name__.replace("Command", "").lower()
            print(
                f"{cmd_name}: too many arguments"
                if len(args) > expected_args
                else f"{cmd_name}: missing arguments"
            )
            return False
        return True

    def help(self) -> str:
        return "No help available for this command"
