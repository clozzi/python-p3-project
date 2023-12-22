# lib/cli.py

from helpers import (
    exit_program,
    list_planets,
    list_robots,
    find_planet_by_name,
    find_robot_by_name,
    find_planet_by_id,
    find_robot_by_id,
    create_planet,
    create_robot,
    delete_planet,
    delete_robot,
    update_planet,
    update_robot,
    find_robot,
    find_planet
)

def main():
    while True:
        print("")
        print("Please select an option:")
        print("1. Exit the program")
        print("2. List all Planets")
        print("3. List all Robots")
        print("4. Find Planet by name")
        print("5. Find Robot by name")

        print("********************")
        choice = input("Type your selection> ")
        print("********************")

        if choice == "1":
            exit_program()
        elif choice == "2":
            planet_menu()
        elif choice == "3":
            robot_menu()
        elif choice == "4":
            find_planet_by_name()
        elif choice == "5":
            find_robot_by_name()
        else:
            print("Invalid choice")

def planet_menu():
    while True:
        list_planets()
        print("")

        print("#: type planet # to see details")
        print("A: add a planet")
        print("D: delete a planet")
        print("B: back to the previous menu")
        print("E: exit the program")
        print("")

        print("********************")
        planet_choice = input("Type your selection> ")
        print("********************")

        if planet_choice == "A" or planet_choice == "a":
            create_planet()
        elif planet_choice == "D" or planet_choice == "d":
            delete_planet()
        elif planet_choice == "B" or planet_choice == "b":
            main()
        elif planet_choice == "E" or planet_choice == "e":
            exit_program()
        elif planet_choice == "1" or planet_choice == "2":
            find_planet(planet_choice)
            spec_planet_menu()
        else:
            print("Invalid choice.")

def robot_menu():
    while True:
        list_robots()
        print("")

        print("#: type robot # to see details")
        print("A: add a robot")
        print("D: delete a robot")
        print("B: back to the previous menu")
        print("E: exit the program")
        print("")

        print("********************")
        robot_choice = input("Type your selection> ")
        print("********************")

        if robot_choice == "A" or robot_choice == "a":
            create_robot()
        elif robot_choice == "D" or robot_choice == "d":
            delete_robot()
        elif robot_choice == "B" or robot_choice == "b":
            main()
        elif robot_choice == "E" or robot_choice == "e":
            exit_program()
        elif robot_choice == "1" or robot_choice == "2" or robot_choice == "3" or robot_choice == "4" or robot_choice == "5":
            while True:
                find_robot(robot_choice)
                print("")

                print("U: update robot details")
                print("B: back to previous menu")
                print("E: exit the program")

                print("********************")
                selected_robot = input("Type your selection> ")
                print("********************")

                if selected_robot == "U" or selected_robot == "u":
                    update_robot()
                elif selected_robot == "B" or selected_robot == "b":
                    robot_menu()
                elif selected_robot == "E" or selected_robot == "e":
                    exit_program()
                else:
                    print("Invalid selection")
        else:
            print("Invalid selection.")

def spec_planet_menu():
    while True:
        print("")

        print("U: update this planet")
        print("B: back to previous menu")
        print("E: exit the program")
        print("")

        print("********************")
        planet_choice = input("Type your selection> ")
        print("********************")

        if planet_choice == "U" or planet_choice == "u":
            update_planet()
        elif planet_choice == "B" or planet_choice == "b":
            planet_menu()
        elif planet_choice == "E" or planet_choice == "e":
            exit_program()
        else:
            print("Invalid choice")

def spec_robot_menu():
    while True:
        print("")

        print("U: update this robot")
        print("B: back to previous menu")
        print("E: exit the program")
        print("")

        print("********************")
        robot_choice = input("Type your selection> ")
        print("********************")

        if robot_choice == "U" or robot_choice == "u":
            update_robot()
        elif robot_choice == "B" or robot_choice == "b":
            robot_menu()
        elif robot_choice == "E" or robot_choice == "e":
            exit_program()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
