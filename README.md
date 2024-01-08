# Python CLI+ORM: Planetary Drones

Interact with the space database to explore planets and the robots that inhabit them.
- *This project is for demonstrative purposes only and does not include actual data on drones/robots which inhabit planets in our solar system.*

This application utilizes Python and in-line SQL statements to seed a database with planets and the drones/robots that inhabit them. Once the database is populated, the command line interface allows the user to manipulate the contents of the database in a variety of ways. Create, update, delete, and explore data related to each of the planets and drones.

---

## Sample Usage

![Sample App Usage](/SpaceCLI.gif)

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

#### *Database Interaction and Manipulation*

`lib/cli.py`

- Creates an interactive command line interface for users utilizing three methods to define three menus separately for clarity and imported helper functions. The main method provides the user with the initial set of choices, while the planet_menu and robot_menu methods facilitate user interactions with the database (space.db) via the imported functions. The cli is looped so that users must exit the program manually.

`lib/debug.py`

- Resets the space database via dropping and creating the relevant class tables and begins an ipdb session for code analysis.

`lib/helpers.py`

- All primary functions for database operations are contained in this file. It is the bridge between the CLI and the two classes which represent database models. The methods defined in this file range in function, here is a list of their functionality:
    - `exit_program`
        Says goodbye and exits the program
    - `find_robot` && `find_planet`
        Takes in an id argument to find a specific robot or planet from the database
    - `list_planets` && `list_robots`
        Retrieves and prints information about all planets or robots in the database
    - `find_planet_by_name` && `find_robot_by_name`
        Takes a name as input and finds the corresponding planet or robot and prints either the relevant information or an error 
    - `find_planet_by_id` && `find_robot_by_id`
        Takes an id as input and finds the corresponding planet or robot and prints either the relevant information or an error
    - `create_planet` && `create_robot`
        Takes user input to create a new planet or robot with appropriate attributes and prints either a confirmation message or an error 
    - `update_planet` && `update_robot`
        Takes user input to update information about a planet or robot in the database and prints either a success message or an error
    - `delete_planet` and `delete_robot`
        Takes user input to delete a planet or robot and prints a success message or an error
    

`lib/seed.py`

- Resets the space database via dropping and creating tables, then repopulates the database with two planets and five robots

---

## Conclusion

Overall, completing this project has given me a lot of insight into the basics of CLIs and ORMs. Hopefully, someone else can use it to help them out too!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Geeks for Geeks](https://www.geeksforgeeks.org/)
- [w3 Schools](https://www.w3schools.com/python/default.asp)