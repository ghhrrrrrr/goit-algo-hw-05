def input_error_show(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name please."
        except KeyError:
            return "There's no such a contact"
        except IndexError:
            return "Enter the argument for the command"
    return inner

def input_error_change(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Something went wrong... Please try again"
        except IndexError:
            return "Enter the argument for the command"
    return inner

def input_error_add(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Something went wrong... Please try again"
        except IndexError:
            return "Enter the argument for the command"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error_add
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error_change
def change_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Contact updated'
    else:
        return "There's no such a contact"

@input_error_show
def show_phone(args ,contacts):
    return contacts[args[0]]


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
        elif command == 'change':
            print(change_phone(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()