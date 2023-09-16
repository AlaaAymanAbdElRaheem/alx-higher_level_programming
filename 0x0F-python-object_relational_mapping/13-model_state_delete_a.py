#!/usr/bin/python3
"""script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa"""

import sys
from urllib.parse import quote_plus
import sqlalchemy
from model_state import Base, State
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
    session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
    session.close()
