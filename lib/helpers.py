# lib/helpers.py

from models.planet import Planet
from models.robot import Robot

def display_planets_robots(id):
    robots = Robot.find_robots_by_planet(id)
    count = 1
    print("\nCurrent Robots:")
    for robot in robots:
        print(f"{count}: {robot.name} is exploring {robot.terrain} regions.")
        count += 1

def exit_program():
    print("Goodbye!")
    exit()
    
def find_robot(id):
    robot = Robot.find_by_id(id)
    planet = Planet.find_by_id(robot.planet_id)
    print(f"Robot {robot.id}: {robot.name}, Terrain: {robot.terrain}, Planet: {planet.name}") if robot else print(
        f"Robot {id} not found in database\n"
    )

def find_planet(id):
    planet = Planet.find_by_id(id)
    print(f"Planet {planet.id}: {planet.name}, {planet.system}") if planet else print(
        f"Planet {id} not found in database\n"
    )

def list_planets():
    planets = Planet.get_all()
    for planet in planets:
        print(f"Planet {planet.id}: {planet.name}, {planet.system}")

def list_robots():
    robots = Robot.get_all()
    for robot in robots:
        planet = Planet.find_by_id(robot.planet_id)
        print(f"Robot {robot.id}: {robot.name}, Terrain: {robot.terrain}, Planet: {planet.name}")

def find_planet_by_name():
    name = input("Enter the planet's name: ")
    planet = Planet.find_by_name(name)
    robots = Robot.find_robots_by_planet(planet.id)
    if planet:
        print(f"Planet {planet.id}: {planet.name}, {planet.system}\n")
        for robot in robots:
            print(f"{robot.name} exploring {robot.terrain}")
    else:
        print(
        f"Planet {name} not found in database\n"
    )

def find_robot_by_name():
    name = input("Enter the robot's name: ")
    robot = Robot.find_by_name(name)
    planet = Planet.find_by_id(robot.planet_id)
    print(f"Robot {robot.id}: {robot.name}, Terrain: {robot.terrain}, Planet: {planet.name}") if robot else print(
        f"Robot {name} not found in database\n"
    )

def find_planet_by_id():
    id_ = input("Enter the planet's id: ")
    planet = Planet.find_by_id(id_)
    print(f"Planet {planet.id}: {planet.name}, {planet.system}") if planet else print(
        f"Planet {id_} not found in database\n"
    )

def find_robot_by_id():
    id_ = input("Enter the robot's id: ")
    robot = Robot.find_by_id(id_)
    planet = Planet.find_by_id(robot.planet_id)
    print(f"Robot {robot.id}: {robot.name}, Terrain: {robot.terrain}, Planet: {planet.name}") if robot else print(
        f"Robot {id_} not found in database\n"
    )

def create_planet():
    while True:
        name = input("Enter the planet's name: ")
        if isinstance(name, str) and len(name) and not name.isnumeric():
            break
        else:
            print("Name must be nonempty string")
    while True:
        system = input("Enter the planet's system: ")
        if isinstance(system, str) and len(system) and not system.isnumeric():
            break
        else:
            print("System must be nonempty string")
    try:
        planet = Planet.create(name, system)
        print(f"Successfully created planet: {planet.name} in {planet.system}")
    except Exception as exc:
        print("Error creating planet: ", exc)

def create_robot():
    while True:
        name = input("Enter the robot's name: ")
        if isinstance(name, str) and len(name) and not name.isnumeric():
            break
        else:
            print("Name must be a nonempty string")
    while True:
        terrain = input("Enter the robot's explorable terrain: ")
        if terrain == "aerial" or terrain == "terrestrial":
            break
        else:
            print("Robots can only explore the land or the sky! (terrestrial or aerial)")
    while True:
        planet_name = input("Enter the robot's planet name: ")
        planet = Planet.find_by_name(planet_name)
        if planet:
            planet_id = planet.id
            break
        else:
            print("Planet is not yet registered with NASA")
    try:
        robot = Robot.create(name, terrain, planet_id)
        print(f"Successfully created robot: {robot.name} exploring {robot.terrain} features")
    except Exception as exc:
        print("Error creating robot: ", exc)

def update_planet(planet_index):
    if planet := Planet.find_by_id(planet_index):
        # try:
        while True:
            name = input("Enter the planet's new name: ")
            if isinstance(name, str) and len(name) and not name.isnumeric():
                break
            else:
                print("Planet name must be a nonempty string")
        while True:
            system = input("Enter the planet's new location: ")
            if isinstance(system, str) and len(system) and not system.isnumeric():
                break
            else:
                print("System name must be a nonempty string")
            
        planet.name = name    
        planet.system = system
        planet.update()
        print(f'Successfully updated planet: {planet.name} in {planet.system}')
    else:
        print(f"Planet {planet} not found in database\n")

def update_robot(robot_index):
    if robot := Robot.find_by_id(robot_index):
        while True:
            name = input("Enter the robot's new name: ")
            if isinstance(name, str) and len(name) and not name.isnumeric():
                break
            else:
                print("Name must be nonempty string")
        while True:
            terrain = input("Enter the robot's new terrain: ")
            if isinstance(terrain, str) and terrain == "terrestrial" or terrain == "aerial":
                break
            else:
                print("Robots can only explore the land or the sky! (terrestrial or aerial)")
        while True:
            planet_name = input("Enter the robot's planet name: ")
            planet = Planet.find_by_name(planet_name)
            if planet:
                planet_id = planet.id
                break
            else:
                print("Planet is not yet registered with NASA")

        robot.name = name
        robot.terrain = terrain
        robot.planet_id = planet_id
        robot.update()
        print(f"Robot updated successfully: {robot.name}")
    else:
        print(f"Robot {robot} not found in database\n")

def delete_planet():
    name_ = input("Enter the planet's name: ")
    if planet := Planet.find_by_name(name_):
        planet.delete()
        print(f"Planet {planet.name} deleted")
    else:
        print(f"Planet {name_} not found in database\n")

def delete_robot():
    name_ = input("Enter the robot's name: ")
    if robot := Robot.find_by_name(name_):
        robot.delete()
        print(f"Robot {robot.name} terminated")
    else:
        print(f"Robot {name_} not found in database\n")