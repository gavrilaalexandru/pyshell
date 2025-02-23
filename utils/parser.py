def parser_cmd(user_input):
    if not user_input:
        return None, []

    parts = user_input.strip().split()
    command_name = parts[0]
    args = parts[1:]

    return command_name, args
