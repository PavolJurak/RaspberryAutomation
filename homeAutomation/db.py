from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite3')
session = scoped_session(sessionmaker(bind=engine))
