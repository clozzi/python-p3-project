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