# lib/helpers.py

from models.planet import Planet
from models.robot import Robot

def exit_program():
    print("Goodbye!")
    exit()

def list_planets():
    planets = Planet.get_all()
    for planet in planets:
        print(planet)

def list_robots():
    robots = Robot.get_all()
    for robot in robots:
        print(robot)

def find_planet_by_name():
    name = input("Enter the planet's name: ")
    planet = Planet.find_by_name(name)
    print(planet) if planet else print(
        f"Planet {name} not found"
    )

def find_robot_by_name():
    name = input("Enter the robot's name: ")
    robot = Robot.find_by_name(name)
    print(robot) if robot else print(
        f"Robot {name} not found"
    )

def find_planet_by_id():
    id_ = input("Enter the planet's id: ")
    planet = Planet.find_by_id(id_)
    print(planet) if planet else print(
        f"Planet {id_} not found"
    )

def find_robot_by_id():
    id_ = input("Enter the robot's id: ")
    robot = Robot.find_by_id(id_)
    print(robot) if robot else print(
        f"Robot {id_} not found"
    )

def create_planet():
    name = input("Enter the planet's name: ")
    system = input("Enter the planet's system: ")
    try:
        planet = Planet.create(name, system)
        print(f"Successfully created planet: {planet}")
    except Exception as exc:
        print("Error creating planet: ", exc)

def create_robot():
    name = input("Enter the robot's name: ")
    terrain = input("Enter the robot's explorable terrain: ")
    planet_id = input("Enter the robot's planet id: ")
    try:
        robot = Robot.create(name, terrain, planet_id)
        print(f"Success created robot: {robot}")
    except Exception as exc:
        print("Error creating robot: ", exc)

def update_planet():
    id_ = input("Enter the planet's id: ")
    if planet := Planet.find_by_id(id_):
        try:
            name = input("Enter the planet's new name: ")
            planet.name = name
            location = input("Enter the planet's new location: ")
            planet.location = location

            planet.update()
            print(f'Successfully updated planet: {planet}')
        except Exception as exc:
            print("Error updating planet: ", exc)
    else:
        print(f'Planet {id_} not found')

def update_robot():
    id_ = input("Enter the robot's id: ")
    if robot := Robot.find_by_id(id_):
        try:
            name = input("Enter the robot's new name: ")
            robot.name = name
            terrain = input("Enter the robot's new terrain: ")
            robot.terrain = terrain
            planet_id = input("Enter the robot's new planet id: ")
            robot.planet_id = planet_id
            robot.update()
            print(f"Robot updated successfully: {robot}")
        except Exception as exc:
            print(f"Error updating robot: ", exc)
    else:
        print(f"Robot {id_} not found")

def delete_planet():
    id_ = input("Enter the planet's id: ")
    if planet := Planet.find_by_id(id_):
        planet.delete()
        print(f"Planet {id_} deleted")
    else:
        print(f"Planet {id_} not found")

def delete_robot():
    id_ = input("Enter the robot's id: ")
    if robot := Robot.find_by_id(id_):
        robot.delete()
        print(f"Robot {id_} deleted")
    else:
        print(f"Robot {id_} not found")