
from models.__init__ import CURSOR, CONN

class Planet:

    def __init__(self, name, system, id=None):
        self.id = id
        self.name = name
        self.system = system

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Planet name cannot be changed.")
        
    @property
    def system(self):
        return self._system
    
    @system.setter
    def system(self, system):
        if isinstance(system, str):
            self._system = system
        else:
            raise Exception("System must be string.")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS planets (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS planets;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO planets (name, system)
            VALUES (?, ?)
        """
        CURSOR.execute(sql)
        CONN.commit()

        self.id = CURSOR.lastrowid

    
    
    def update(self):
        sql = """
            UPDATE planets
            SET name = ?, system = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.system, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM planets
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        self.id = None

    @classmethod
    def create(cls, name, system):
        planet = cls(name, system)
        planet.save()
        return planet

    @classmethod
    def get_all(cls):
        """Return a list containing a Planet object per row in the table"""
        sql = """
            SELECT *
            FROM planets
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        planet = cls.all.get(row[0])
        if planet:
            planet.name = row[1]
            planet.system = row[2]
        else:
            planet = cls(row[1], row[2])
            planet.id = row[0]
            cls.all[planet.id] = planet
        return planet
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM planets
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM planets
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None