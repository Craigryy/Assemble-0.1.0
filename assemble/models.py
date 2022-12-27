import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DATETIME,
)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class noteBook(Base):
    """
    Table to store users log entries
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
