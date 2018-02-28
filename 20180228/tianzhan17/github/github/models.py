from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlougithub')
Base = declarative_base()

class Repository(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    update_time = Column(DateTime)
    commits = Column(Integer)
    branches = Column(Integer)
    releases = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
