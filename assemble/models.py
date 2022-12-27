import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DATETIME,
)

from sqlalchemy.ext.declarative import declarative_base

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()


class noteBook(Base):
    """
    Table to store users note entries
    """
    __tablename__ = 'note_book'

    id = column(Integer, primary_key=True)
    title = column(string(300), nullable=False)
    note = column(string(300),nullable=False)
    label = column(string(300),nullable=False)
    note_datetime = column(DATETIME, nullable=False)

    created_at = column(
        datetime,
        default=datetime.now,
        nullable=False
    )

    updated_at = column(
        datetime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now(),
        nullable=False
    )
