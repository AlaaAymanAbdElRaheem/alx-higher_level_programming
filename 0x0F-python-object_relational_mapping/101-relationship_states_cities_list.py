#!/usr/bin/python3
"""script that lists all State objects, and corresponding City objects,"""

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
    results = session.query(State).order_by(State.id).all()

    num = 1
    for result in results:
        print("{}: {}".format(num, State.name))
        for city in result.cities:
            print("    {}: {}".format(city.id, city.name))
        num += 1
    session.close()
