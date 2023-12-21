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
        print("A: add a planet")
        print("B: back to the previous menu")
        print("E: exit")

        planet_choice = input("Type your selection> ")

        if planet_choice == "A" or planet_choice == "a":
            print("Add planet function")
        elif planet_choice == "B" or planet_choice == "b":
            main()
        elif planet_choice == "E" or planet_choice == "e":
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
        print("A: add a robot")
        print("B: back to the previous menu")
        print("E: exit")

        robot_choice = input("Type your selection> ")

        if robot_choice == "A" or robot_choice == "a":
            print("Add robot function")
        elif robot_choice == "B" or robot_choice == "b":
            main()
        elif robot_choice == "E" or robot_choice == "e":
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
        print("E: exit the program")
        print("P: list all Planets")
        print("R: list all Robots")

        choice = input("Type your selection> ")

        if choice == "E" or choice == "e":
            exit_program()
        elif choice == "P" or choice == "p":
            planet_menu()
        elif choice == "R" or choice == "r":
            robot_menu()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
