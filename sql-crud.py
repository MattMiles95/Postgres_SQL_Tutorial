from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Porgrammer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database dircetly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Micrsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

# add each instance of our progrmmers to our session
session.add(ada_lovelace)
session.add(alan_turing)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_berners_lee)

# commit our session to the database
session.commit()

# Query to find Ada Lovelace
# ada_query = session.query(Programmer).filter_by(first_name="Ada", last_name="Lovelace")
# ada = ada_query.first()
# alan_query = session.query(Programmer).filter_by(first_name="Alan", last_name="Turing")
# alan = alan_query.first()

# Delete Additional Records
# if ada:
#     session.delete(ada)
#     session.commit()
#     print("\nAda Lovelace deleted successfully.")
# elif alan:
#     session.delete(alan)
#     session.commit()
#     print("\Alan Turing deleted successfully.")
# else:
#     print("\nNeither Ada Lovelace nor Alan Turing found.")

# query the database to find all prgrammers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )