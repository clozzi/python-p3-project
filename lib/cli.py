# lib/cli.py

from helpers import (
    exit_program,
    list_planets,
    list_robots
)

def planet_menu():
    while True:
        list_planets()

        print("Type planet # to see details")
        print("Type A to add a planet")
        print("Type B to go back to the previous menu")
        print("Type E to exit")

        planet_choice = input("> ")

        if planet_choice == "A":
            print("Add planet function")
        elif planet_choice == "B":
            main()
        elif planet_choice == "E":
            exit_program()
        elif planet_choice == "1":
            print("Earth details here")
        elif planet_choice == "2":
            print("Mars details here")
        else:
            print("Invalid choice.")

def robot_menu():
    while True:
        list_robots()

        print("Type robot # to see details")
        print("Type A to add a robot")
        print("Type B to go back to the previous menu")
        print("Type E to exit")

        robot_choice = input("> ")

        if robot_choice == "A":
            print("Add robot function")
        elif robot_choice == "B":
            main()
        elif robot_choice == "E":
            exit_program()
        elif robot_choice == "1":
            print("Walle details here")
        elif robot_choice == "2":
            print("Johnny details here")
        elif robot_choice == "3":
            exit_program()
        elif robot_choice == "4":
            print("Walle details here")
        elif robot_choice == "5":
            print("Johnny details here")
        else:
            print("Invalid choice.")

def main():
    while True:
        print("Please select an option:")
        print("E to Exit the program")
        print("1. Explore all Planets")
        print("2. Explore all Robots")

        choice = input("> ")

        if choice == "E":
            exit_program()
        elif choice == "1":
            planet_menu()
        elif choice == "2":
            robot_menu()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
