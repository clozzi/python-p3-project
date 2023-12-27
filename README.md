# Python CLI+ORM: Planetary Drones

Interact with the space database to explore planets and the robots that inhabit them.
- This project is for demonstrative purposes only and does not include actual data on drones/robots which inhabit planets in our solar system.

This application utilizes Python and in-line SQL statements to seed a database with planets and the drones/robots that inhabit them. Once the database is filled, the command line interface allows the user to manipulate the contents of the database in a variety of ways. Create, update, delete, and explore data related to each of the planets and drones.

## Directory Structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── planet.py
        └── robot.py
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── seed.py
```

---


## Generating The Environment

Run the commands:

```console
pipenv install
pipenv shell
python lib/seed.py
python lib/cli.py
```

---


## File Descriptions

`lib/models/planet.py`




## Utilizing the CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

---

## Conclusion

Overall, completing this project has given me a lot of insight into the basics of CLIs and ORMs. Hopefully, someone else can use it to help them out too!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Geeks for Geeks](https://www.geeksforgeeks.org/)
- [w3 Schools](https://www.w3schools.com/python/default.asp)