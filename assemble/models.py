from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Folder(Base):
    """ Folder account."""

    __tablename__ = "folders"

    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    files = relationship(
        "File",
        cascade="all, delete-orphan",
        back_populates="folder",
        lazy="selectin",
    )

    def __init__(self,name):
        self.name=name

class File(Base):
    __tablename__ = "files"

    id = Column(Integer(), primary_key=True, index=True)
    Title = Column(String(200), nullable=False)
    Notes = Column(String(200), nullable=False)
    Label = Column(String(20), nullable=False)
    folder_id = Column(Integer(), ForeignKey("folders.id")
    )
    folder = relationship(
        "Folder",
        back_populates="files",
    )
