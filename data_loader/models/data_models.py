from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Circuit(Base):
    __tablename__ = 'circuits'
    __table_args__ = {'schema': 'project'}

    circuitid = Column(Integer, primary_key=True)
    circuitref = Column(Text)
    name = Column(Text)
    location = Column(Text)
    country = Column(Text)
    lat = Column(Float)
    lng = Column(Float)
    alt = Column(Integer)
    url = Column(Text)


class Constructor(Base):
    __tablename__ = 'constructors'
    __table_args__ = {'schema': 'project'}

    constructorid = Column(Integer, primary_key=True)
    constructorref = Column(Text)
    name = Column(Text)
    nationality = Column(Text)
    url = Column(Text)


class Driver(Base):
    __tablename__ = 'drivers'
    __table_args__ = {'schema': 'project'}

    driverid = Column(Integer, primary_key=True)
    driverref = Column(Text)
    number = Column(Text)
    code = Column(Text)
    forename = Column(Text)
    surname = Column(Text)
    dob = Column(Date)
    nationality = Column(Text)
    url = Column(Text)


class Race(Base):
    __tablename__ = 'races'
    __table_args__ = {'schema': 'project'}

    raceid = Column(Integer, primary_key=True)
    year = Column(Integer)
    round = Column(Integer)
    circuitid = Column(Integer, ForeignKey('project.circuits.circuitid'))
    name = Column(Text)
    date = Column(Date)
    time = Column(Text)
    url = Column(Text)
    fp1_date = Column(Text)
    fp1_time = Column(Text)
    fp2_date = Column(Text)
    fp2_time = Column(Text)
    fp3_date = Column(Text)
    fp3_time = Column(Text)
    quali_date = Column(Text)
    quali_time = Column(Text)
    sprint_date = Column(Text)
    sprint_time = Column(Text)


class ConstructorResult(Base):
    __tablename__ = 'constructor_results'
    __table_args__ = {'schema': 'project'}

    constructorresultsid = Column(Integer, primary_key=True)
    raceid = Column(Integer, ForeignKey('project.races.raceid'))
    constructorid = Column(Integer, ForeignKey('project.constructors.constructorid'))
    points = Column(Float)
    status = Column(Text)


class ConstructorStanding(Base):
    __tablename__ = 'constructor_standings'
    __table_args__ = {'schema': 'project'}

    constructorstandingsid = Column(Integer, primary_key=True)
    raceid = Column(Integer, ForeignKey('project.races.raceid'))
    constructorid = Column(Integer, ForeignKey('project.constructors.constructorid'))
    points = Column(Float)
    position = Column(Integer)
    positiontext = Column(Text)
    wins = Column(Integer)


class DriverStanding(Base):
    __tablename__ = 'driver_standings'
    __table_args__ = {'schema': 'project'}

    driverstandingsid = Column(Integer, primary_key=True)
    raceid = Column(Integer, ForeignKey('project.races.raceid'))
    driverid = Column(Integer, ForeignKey('project.drivers.driverid'))
    points = Column(Float)
    position = Column(Integer)
    positiontext = Column(Text)
    wins = Column(Integer)


class LapTime(Base):
    __tablename__ = 'lap_times'
    __table_args__ = {'schema': 'project'}

    lap_time_id = Column(Integer, primary_key=True)
    raceid = Column(Integer, ForeignKey('project.races.raceid'))
    driverid = Column(Integer, ForeignKey('project.drivers.driverid'))
    lap = Column(Integer)
    position = Column(Integer)
    time = Column(Text)
    milliseconds = Column(Integer)


class PitStop(Base):
    __tablename__ = 'pit_stops'
    __table_args__ = {'schema': 'project'}

    pitstop_id = Column(Integer, primary_key=True)
    raceid = Column(Integer, ForeignKey('project.races.raceid'))
    driverid = Column(Integer, ForeignKey('project.drivers.driverid'))
    stop = Column(Integer)
    lap = Column(Integer)
    time = Column(Text)
    duration = Column(Text)
    milliseconds = Column(Integer)


class Qualifying(Base):
    __tablename__ = 'qualifying'
    __table_args__ = {'schema': 'project'}

    qualifyid = Column(Integer, primary_key=True)
    raceid = Column(Integer, ForeignKey('project.races.raceid'))
    driverid = Column(Integer, ForeignKey('project.drivers.driverid'))
    constructorid = Column(Integer, ForeignKey('project.constructors.constructorid'))
    number = Column(Integer)
    position = Column(Integer)
    q1 = Column(Text)
    q2 = Column(Text)
    q3 = Column(Text)


class Result(Base):
    __tablename__ = 'results'
    __table_args__ = {'schema': 'project'}

    resultid = Column(Integer, primary_key=True)
    raceid = Column(Integer, ForeignKey('project.races.raceid'))
    driverid = Column(Integer, ForeignKey('project.drivers.driverid'))
    constructorid = Column(Integer, ForeignKey('project.constructors.constructorid'))
    number = Column(Text)
    grid = Column(Integer)
    position = Column(Text)
    positiontext = Column(Text)
    positionorder = Column(Integer)
    points = Column(Float)
    laps = Column(Integer)
    time = Column(Text)
    milliseconds = Column(Text)
    fastestlap = Column(Text)
    rank = Column(Text)
    fastestlaptime = Column(Text)
    fastestlapspeed = Column(Text)
    statusid = Column(Integer, ForeignKey('project.status.statusid'))


class Season(Base):
    __tablename__ = 'seasons'
    __table_args__ = {'schema': 'project'}

    season_id = Column(Integer, primary_key=True)
    year = Column(Integer)
    url = Column(Text)


class SprintResult(Base):
    __tablename__ = 'sprint_results'
    __table_args__ = {'schema': 'project'}

    resultid = Column(Integer, primary_key=True)
    raceid = Column(Integer, ForeignKey('project.races.raceid'))
    driverid = Column(Integer, ForeignKey('project.drivers.driverid'))
    constructorid = Column(Integer, ForeignKey('project.constructors.constructorid'))
    number = Column(Integer)
    grid = Column(Integer)
    position = Column(Text)
    positiontext = Column(Text)
    positionorder = Column(Integer)
    points = Column(Integer)
    laps = Column(Integer)
    time = Column(Text)
    milliseconds = Column(Text)
    fastestlap = Column(Text)
    fastestlaptime = Column(Text)
    statusid = Column(Integer, ForeignKey('project.status.statusid'))


class Status(Base):
    __tablename__ = 'status'
    __table_args__ = {'schema': 'project'}

    statusid = Column(Integer, primary_key=True)
    status = Column(Text)

from collections import OrderedDict

file_orm_mapping = OrderedDict([("circuits.csv",Circuit),
                ("races.csv" , Race),
                ("drivers.csv" , Driver),
                ("constructors.csv" , Constructor),
                ("status.csv" , Status),
                ("seasons.csv" , Season),
                ("constructor_results.csv",ConstructorResult),
                ("constructor_standings.csv" , ConstructorStanding),
                ("driver_standings.csv" , DriverStanding),
                ("lap_times.csv" , LapTime),
                ("pit_stops.csv" , PitStop),
                ("qualifying.csv" , Qualifying),
                ("results.csv" , Result),
                ("sprint_results.csv" , SprintResult)
                    ])