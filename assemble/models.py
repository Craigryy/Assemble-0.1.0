from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Folder(Base):
    """ Folder account."""

    __tablename__ = "folders"

    gid = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)

    files = relationship("File", back_populate='author', lazy='noload', cascade='all,delete')

    def __init__(self, name, notes, gid):
        self.name = name
        self.notes = notes
        self.gid = gid


class File(Base):
    __tablename__ = "files"

    id = Column(Integer(), primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    notes = Column(String(200), nullable=False)
    label = Column(String(200), nullable=False)

    folder_gid = Column(String(20), ForeignKey('folders_gid'))
    author = relationship("Folder", back_populate="files")
