"""
Database Setup for SQLAlchemy ORM.
"""

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


#########Put class definitions of tables and database mapper code within them here############


engine = create_engine('sqlite:///restaurantmenu.db') # can be any database system here

Base.metadata.create_all(engine)
