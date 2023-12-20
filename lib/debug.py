#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.planet import Planet
from models.robot import Robot

import ipdb;

def reset_db():
    Robot.drop_table()
    Robot.create_table()
    Planet.drop_table()
    Planet.create_table()

reset_db()

ipdb.set_trace()
