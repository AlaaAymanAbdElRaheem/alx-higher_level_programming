#!/usr/bin/python3
"""script that changes the name of a State object from the database"""

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
    session.query(State).filter(State.id == 2).update(
        {State.name: "New Mexico"}, synchronize_session=False)
    session.commit()
    session.close()
