def input_error(func):

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter the argument for the command"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for contact '{name}' has been updated"
    else:
        return f"Contact '{name}' does not exist."

@input_error
def show_all_contacts(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

@input_error
def username_phone(name, contacts):
    if name in contacts:
        return contacts[name]
    else:
        return "You don't have the phone number of this contact"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "show":
            print(show_all_contacts(contacts))

        elif command == "phone":
            print(username_phone(args[0], contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()