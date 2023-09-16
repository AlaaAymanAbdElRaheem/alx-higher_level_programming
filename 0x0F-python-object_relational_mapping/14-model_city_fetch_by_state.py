#!/usr/bin/python3
""" script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa"""

import sys
from urllib.parse import quote_plus
import sqlalchemy
from model_state import Base, State
from model_city import City
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
    results = session.query(State, City).select_from(
        State).join(City, State.id == City.state_id).order_by(City.id)

    for result in results:
        print("{}: ({}) {}".format(result.State.name, result.City.id,
                                   result.City.name))
    session.close()
