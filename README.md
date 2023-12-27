# Python CLI+ORM: Planetary Drones

Interact with the space database to explore planets and the robots that inhabit them.
- *This project is for demonstrative purposes only and does not include actual data on drones/robots which inhabit planets in our solar system.*

This application utilizes Python and in-line SQL statements to seed a database with planets and the drones/robots that inhabit them. Once the database is populated, the command line interface allows the user to manipulate the contents of the database in a variety of ways. Create, update, delete, and explore data related to each of the planets and drones.

---

## Sample Usage

INSERT GIF HERE

---

## Directory Structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── planet.py
        └── robot.py
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── seed.py
```

---


## Generating The Environment

Run the following commands:

```console
pipenv install
pipenv shell
python lib/seed.py
python lib/cli.py
```

---

## CLI Interaction

#### *Main Menu*

1. Exit the program
2. List all Planets
3. List all Robots
4. Find Planet by name
5. Find Robot by name

#### Sub Menus 2 & 3

List all Planets || List all Robots

Both ALL submenus (selected with choices 2 or 3 at the main menu) provide lists of their namesakes found in the database, with options to see specific details, add elements to the database, delete elements from the database, or further navigate the cli.

#### Sub Menus 4 & 5

Find Planet by name || Find Robot by name

Search functions for when the name of the planet or robot is known. If the element is found in the database, the CLI will display the appropriate element details.

---

## File Descriptions

#### *Models*

`lib/models/planet.py`

- Defines a reusable class Planet with name and system attributes. The planet class has methods for creating and dropping an SQL table and for saving, updating, and deleting a planet. Included in the planet class are also methods for retrieving specific instances of planets or all of the planets.

`lib/models/robot.py`

- Defines a reusable class Robot with name, terrain, and planet_id attributes. The robot class has methods for creating and dropping an SQL table and for saving, updating, and deleting a robot. Included in the robot class are also methods for retrieving specific instances of robots or all of the robots. The robot class is assocaited with the planet class via the planet_id attribute, and the property setter for this attribute checks that the provided planet_id exists in the planets table by utilizing a method imported from the Planet class.

#### *Database Manipulation*

`lib/cli.py`

- INSERT EXPLANATION HERE

`lib/debug.py`

- INSERT EXPLANATION HERE

`lib/helpers.py`

- INSERT EXPLANATION HERE

`lib/seed.py`

- INSERT EXPLANATION HERE

---

## Conclusion

Overall, completing this project has given me a lot of insight into the basics of CLIs and ORMs. Hopefully, someone else can use it to help them out too!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Geeks for Geeks](https://www.geeksforgeeks.org/)
- [w3 Schools](https://www.w3schools.com/python/default.asp)