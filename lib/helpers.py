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