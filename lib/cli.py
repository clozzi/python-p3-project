# lib/cli.py

from helpers import (
    exit_program,
    list_planets,
    list_robots
)

def e_exit():
    exit_program()

def planet_menu():
    list_planets()

    print("Type planet # to see details")
    print("Type A to add a planet")
    print("Type B to go back to the previous menu")
    print("Type E to exit")

def robot_menu():
    list_robots()

def main():
    print("Please select an option:")
    print("E to Exit the program")
    print("1. Explore all Planets")
    print("2. Explore all Robots")

    choice = input("> ")

    if choice == "E":
        e_exit()
    elif choice == "1":
        planet_menu()
    elif choice == "2":
        robot_menu()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
