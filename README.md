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

Run the commands:

```console
pipenv install
pipenv shell
python lib/seed.py
python lib/cli.py
```

---

## CLI Interaction

BREAKDOWN OF CLI SCRIPT

---

## File Descriptions

#### *Models*

- `lib/models/planet.py`

INSERT EXPLANATION HERE

- `lib/models/robot.py`

INSERT EXPLANATION HERE

    #### *Database Manipulation*

- `lib/cli.py`

INSERT EXPLANATION HERE

- `lib/debug.py`

INSERT EXPLANATION HERE

- `lib/helpers.py`

INSERT EXPLANATION HERE

- `lib/seed.py`

INSERT EXPLANATION HERE

---

## Conclusion

Overall, completing this project has given me a lot of insight into the basics of CLIs and ORMs. Hopefully, someone else can use it to help them out too!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Geeks for Geeks](https://www.geeksforgeeks.org/)
- [w3 Schools](https://www.w3schools.com/python/default.asp)