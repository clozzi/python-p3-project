# lib/cli.py

from helpers import (
    exit_program,
    list_planets,
    list_robots,
    find_planet_by_name,
    find_robot_by_name,
    earth_details,
    mars_details,
    create_planet,
    create_robot,
    delete_planet,
    delete_robot
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
        elif planet_choice == "1":
            earth_menu()
        elif planet_choice == "2":
            mars_menu()
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
        elif robot_choice == "1":
            while True:
                print("Walle details here")
                print("")

                print("U: update robot details")
                print("D: delete robot")
                print("B: back to previous menu")
                print("E: exit the program")

                print("********************")
                selected_robot = input("Type your selection> ")
                print("********************")

                if selected_robot == "1":
                    print("update robot")
                elif selected_robot == "2":
                    print("delete robot")
                elif selected_robot == "3":
                    robot_menu()
                elif selected_robot == "4":
                    exit_program()
                else:
                    print("Invalid selection")
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

def earth_menu():
    while True:
        earth_details()
        print("")

        print("U: update this planet")
        print("B: back to previous menu")
        print("E: exit the program")
        print("")

        print("********************")
        earth_choice = input("Type your selection> ")
        print("********************")

        if earth_choice == "U" or earth_choice == "u":
            print("Update Earth")
        elif earth_choice == "B" or earth_choice == "b":
            planet_menu()
        elif earth_choice == "E" or earth_choice == "e":
            exit_program()
        else:
            print("Invalid choice")

def mars_menu():
    while True:
        mars_details()
        print("")

        print("U: update this planet")
        print("B: back to previous menu")
        print("E: exit the program")
        print("")

        print("********************")
        mars_choice = input("Type your selection> ")
        print("********************")

        if mars_choice == "U" or mars_choice == "u":
            print("Update Mars")
        elif mars_choice == "B" or mars_choice == "b":
            planet_menu()
        elif mars_choice == "E" or mars_choice == "e":
            exit_program()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
