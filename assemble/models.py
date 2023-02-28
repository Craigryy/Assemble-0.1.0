from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class Folder(Base):
    """Table to store users folder entries"""
    __tablename__ = "folders"

    id = Column(Integer(), primary_key=True)
    name = Column(String(20), nullable=False,unique=True)
    notes = Column(String(100), nullable=False)
    files = relationship(
        "File",
        cascade="all, delete-orphan",
        back_populates="author",
        lazy="selectin",
    )
    def __init__(self,name,notes):
        self.name=name
        self.notes=notes


    @property
    def num_files(self):
        return len(self.files)

    def add_child(self,file):
        if self.num_files >=10:
            raise ValueError ('A folder can have at most 10 files.')
        self.files.append(file)


class File(Base):
    """Table to store users file entries"""
    __tablename__ = "files"

    id = Column(Integer(), primary_key=True, index=True)
    title = Column(String(100), nullable=False,unique=True)
    notes = Column(String(100), nullable=False)
    label = Column(String(100),nullable=True)
    folder_id = Column(Integer(), ForeignKey("folders.id"))
    author = relationship(
        "Folder",
        back_populates="files"
    )

