
from models.__init__ import CONN, CURSOR
from models.planet import Planet
from models.robot import Robot

def seed_db():
    Robot.drop_table()
    Planet.drop_table()
    Planet.create_table()
    Robot.create_table()

    earth = Planet.create("Earth", "solar")
    mars = Planet.create("Mars", "solar")
    Robot.create("Walle", "terrestrial", earth.id)
    Robot.create("Johnny", "terrestrial", earth.id)
    Robot.create("Skynet", "aerial", earth.id)
    Robot.create("Ingenuity", "aerial", mars.id)

seed_db()
print("DB seeded")