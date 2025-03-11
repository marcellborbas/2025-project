from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, ForeignKey, Text, Date

class Base(DeclarativeBase):
    pass

class Circuit(Base):
    __tablename__ = 'circuits'
    __table_args__ = {'schema': 'project'}

    circuitid: Mapped[int] = mapped_column(Integer, primary_key=True)
    circuitref: Mapped[str] = mapped_column(Text)
    name: Mapped[str] = mapped_column(Text)
    location: Mapped[str] = mapped_column(Text)
    country: Mapped[str] = mapped_column(Text)
    lat: Mapped[float] = mapped_column(Float)
    lng: Mapped[float] = mapped_column(Float)
    alt: Mapped[int] = mapped_column(Integer)
    url: Mapped[str] = mapped_column(Text)


class Constructor(Base):
    __tablename__ = 'constructors'
    __table_args__ = {'schema': 'project'}

    constructorid: Mapped[int] = mapped_column(Integer, primary_key=True)
    constructorref: Mapped[str] = mapped_column(Text)
    name: Mapped[str] = mapped_column(Text)
    nationality: Mapped[str] = mapped_column(Text)
    url: Mapped[str] = mapped_column(Text)


class Driver(Base):
    __tablename__ = 'drivers'
    __table_args__ = {'schema': 'project'}

    driverid: Mapped[int] = mapped_column(Integer, primary_key=True)
    driverref: Mapped[str] = mapped_column(Text)
    number: Mapped[str] = mapped_column(Text)
    code: Mapped[str] = mapped_column(Text)
    forename: Mapped[str] = mapped_column(Text)
    surname: Mapped[str] = mapped_column(Text)
    dob: Mapped[Date] = mapped_column(Date)
    nationality: Mapped[str] = mapped_column(Text)
    url: Mapped[str] = mapped_column(Text)


class Race(Base):
    __tablename__ = 'races'
    __table_args__ = {'schema': 'project'}

    raceid: Mapped[int] = mapped_column(Integer, primary_key=True)
    year: Mapped[int] = mapped_column(Integer)
    round: Mapped[int] = mapped_column(Integer)
    circuitid: Mapped[int] = mapped_column(Integer, ForeignKey('project.circuits.circuitid'))
    name: Mapped[str] = mapped_column(Text)
    date: Mapped[Date] = mapped_column(Date)
    time: Mapped[str] = mapped_column(Text)
    url: Mapped[str] = mapped_column(Text)
    fp1_date: Mapped[str] = mapped_column(Text)
    fp1_time: Mapped[str] = mapped_column(Text)
    fp2_date: Mapped[str] = mapped_column(Text)
    fp2_time: Mapped[str] = mapped_column(Text)
    fp3_date: Mapped[str] = mapped_column(Text)
    fp3_time: Mapped[str] = mapped_column(Text)
    quali_date: Mapped[str] = mapped_column(Text)
    quali_time: Mapped[str] = mapped_column(Text)
    sprint_date: Mapped[str] = mapped_column(Text)
    sprint_time: Mapped[str] = mapped_column(Text)


class Status(Base):
    __tablename__ = 'status'
    __table_args__ = {'schema': 'project'}

    statusid: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[str] = mapped_column(Text)
