import shlex


def parser_cmd(user_input):
    if not user_input:
        return None, []

    parts = shlex.split(user_input)
    command_name = parts[0]
    args = parts[1:]

    return command_name, args
