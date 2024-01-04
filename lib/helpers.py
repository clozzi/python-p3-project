# lib/helpers.py

from models.planet import Planet
from models.robot import Robot

def exit_program():
    print("Goodbye!")
    exit()
    
def find_robot(id):
    robot = Robot.find_by_id(id)
    print(f"Robot {robot.id}: {robot.name}, {robot.terrain}") if robot else print(
        f"Robot {id} not found in database"
    )

def find_planet(id):
    planet = Planet.find_by_id(id)
    print(f"Planet {planet.id}: {planet.name}, {planet.system}") if planet else print(
        f"Planet {id} not found in database"
    )

def list_planets():
    planets = Planet.get_all()
    for planet in planets:
        print(f"Planet {planet.id}: {planet.name}, {planet.system}")

def list_robots():
    robots = Robot.get_all()
    for robot in robots:
        print(f"Robot {robot.id}: {robot.name}, {robot.terrain}")

def find_planet_by_name():
    name = input("Enter the planet's name: ")
    planet = Planet.find_by_name(name)
    print(f"Planet {planet.id}: {planet.name}, {planet.system}") if planet else print(
        f"Planet {name} not found in database"
    )

def find_robot_by_name():
    name = input("Enter the robot's name: ")
    robot = Robot.find_by_name(name)
    print(f"Robot {robot.id}: {robot.name}, {robot.terrain}") if robot else print(
        f"Robot {name} not found in database"
    )

def find_planet_by_id():
    id_ = input("Enter the planet's id: ")
    planet = Planet.find_by_id(id_)
    print(f"Planet {planet.id}: {planet.name}, {planet.system}") if planet else print(
        f"Planet {id_} not found in database"
    )

def find_robot_by_id():
    id_ = input("Enter the robot's id: ")
    robot = Robot.find_by_id(id_)
    print(f"Robot {robot.id}: {robot.name}, {robot.terrain}") if robot else print(
        f"Robot {id_} not found in database"
    )

def create_planet():
    name = input("Enter the planet's name: ")
    system = input("Enter the planet's system: ")
    try:
        planet = Planet.create(name, system)
        print(f"Successfully created planet: {planet.name} in {planet.system}")
    except Exception as exc:
        print("Error creating planet: ", exc)

def create_robot():
    name = input("Enter the robot's name: ")
    terrain = input("Enter the robot's explorable terrain: ")
    planet_id = input("Enter the robot's planet id: ")
    try:
        robot = Robot.create(name, terrain, planet_id)
        print(f"Successfully created robot: {robot.name} exploring {robot.terrain} features")
    except Exception as exc:
        print("Error creating robot: ", exc)

def update_planet(planet_index):
    if planet := Planet.find_by_id(planet_index):
        try:
            name = input("Enter the planet's new name: ")
            planet.name = name
            system = input("Enter the planet's new location: ")
            planet.system = system

            planet.update()
            print(f'Successfully updated planet: {planet.name} in {planet.system}')
        except Exception as exc:
            print("Error updating planet: ", exc)
    else:
        print(f'Planet {planet} not found in database')

def update_robot(robot_index):
    if robot := Robot.find_by_id(robot_index):
        try:
            name = input("Enter the robot's new name: ")
            robot.name = name
            terrain = input("Enter the robot's new terrain: ")
            robot.terrain = terrain
            planet_id = input("Enter the robot's new planet id: ")
            robot.planet_id = int(planet_id)
            robot.update()
            print(f"Robot updated successfully: {robot}")
        except Exception as exc:
            print(f"Error updating robot: ", exc)
    else:
        print(f"Robot {robot} not found in database")

def delete_planet():
    name_ = input("Enter the planet's name: ")
    if planet := Planet.find_by_name(name_):
        planet.delete()
        print(f"Planet {planet.name} deleted")
    else:
        print(f"Planet {name_} not found in database")

def delete_robot():
    name_ = input("Enter the robot's name: ")
    if robot := Robot.find_by_name(name_):
        robot.delete()
        print(f"Robot {robot.name} terminated")
    else:
        print(f"Robot {name_} not found in database")