# lib/models/employee.py
from models.__init__ import CURSOR, CONN
from models.planet import Planet

class Robot:

    all = {}

    def __init__(self, name, terrain, planet_id, id=None):
        self.id = id
        self.name = name
        self.terrain = terrain
        self.planet_id = planet_id

    def __repr__(self) -> str:
        return (
            f"Robot {self.id}: {self.name}, {self.terrain}, " +
            f"Planet ID: {self.planet_id}"
        )

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise Exception("Robot name must be a non-empty string.")

    @property
    def terrain(self):
        return self._terrain
    
    @terrain.setter
    def terrain(self, terrain):
        if isinstance(terrain, str) and len(terrain):
            self._terrain = terrain
        else:
            raise Exception("Terrain must be a non-empty string.")
        
    @property
    def planet_id(self):
        return self._planet_id
    
    @planet_id.setter
    def planet_id(self, planet_id):
        if type(planet_id) is int and Planet.find_by_id(planet_id):
            self._planet_id = planet_id
        else:
            raise ValueError("planet_id must reference a planet in the database")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS robots (
            id INTEGER PRIMARY KEY,
            name TEXT,
            terrain TEXT,
            planet_id INTEGER,
            FOREIGN KEY (planet_id) REFERENCES planets(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS robots
        """
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        sql = """
            INSERT INTO robots (name, terrain, planet_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.terrain, self.planet_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE robots
            SET name = ?, terrain = ?, planet_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.terrain,
                             self.planet_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM robots
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        
        self.id = None

    @classmethod
    def create(cls, name, terrain, planet_id):
        robot = cls(name, terrain, int(planet_id))
        robot.save()
        return robot
    
    @classmethod
    def instance_from_db(cls, row):
        robot = cls.all.get(row[0])
        if robot:
            robot.name = row[1]
            robot.terrain = row[2]
            robot.planet_id = row[3]
        else:
            robot = cls(row[1], row[2], row[3])
            robot.id = row[0]
            cls.all[robot.id] = robot
        return robot
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Robot object per row in the table"""
        sql = """
            SELECT *
            FROM robots
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM robots
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM robots
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
