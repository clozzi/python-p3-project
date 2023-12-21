# lib/cli.py

from helpers import (
    exit_program,
    list_planets,
    list_robots
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "E":
            exit_program()
        elif choice == "1":
            list_planets()
        elif choice == "2":
            list_robots()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("E to Exit the program")
    print("1. Explore all Planets")
    print("2. Explore all Robots")


if __name__ == "__main__":
    main()
