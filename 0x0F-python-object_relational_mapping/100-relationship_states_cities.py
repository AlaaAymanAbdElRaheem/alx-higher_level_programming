#!/usr/bin/python3
"""script that creates the State “California” 
with the City “San Francisco” from the database hbtn_0e_100_usa """

import sys
from urllib.parse import quote_plus
import sqlalchemy
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    passwd = quote_plus(sys.argv[2])
    engine = sqlalchemy.create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(sys.argv[1],
                                              passwd, sys.argv[3]),
                                      pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(engine)
    session = session()
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
    session.close()
    