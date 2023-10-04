def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Invalid input. Please try again."
    return wrapper

@input_error
def main():
    contacts = {}

    def parse_command(command):
        command_parts = command.strip().split(' ', 1)
        if len(command_parts) < 1:
            return None, None
        command_type = command_parts[0].lower()
        args = command_parts[1] if len(command_parts) > 1 else None
        return command_type, args

    def handle_hello():
        return "How can I help you?"

    def handle_add(args):
        if args:
            name, phone = args.split(' ', 1)
            contacts[name] = phone
            return "Contact added successfully."
        else:
            return "Please provide name and phone."

    def handle_change(args):
        if args:
            name, phone = args.split(' ', 1)
            if name in contacts:
                contacts[name] = phone
                return "Phone number updated for {}".format(name)
            else:
                return "Contact not found."
        else:
            return "Please provide name and phone."

    def handle_phone(args):
        if args:
            name = args.strip()
            if name in contacts:
                return "Phone number for {}: {}".format(name, contacts[name])
            else:
                return "Contact not found."
        else:
            return "Please provide a name."

    def handle_show_all():
        if contacts:
            result = "Contacts:\n"
            for name, phone in contacts.items():
                result += "{}: {}\n".format(name, phone)
            return result.strip()
        else:
            return "No contacts available."

    def handle_goodbye():
        return "Good bye!"

    while True:
        command = input("Enter a command: ")
        command_type, args = parse_command(command)
        
        if command_type == "hello":
            print(handle_hello())
        elif command_type == "add":
            print(handle_add(args))
        elif command_type == "change":
            print(handle_change(args))
        elif command_type == "phone":
            print(handle_phone(args))
        elif command_type == "show":
            print(handle_show_all())
        elif command_type in ["goodbye", "close", "exit"]:
            print(handle_goodbye())
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
