from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from .models import noteBook
from .assemble import get_database_url


class noteBookManager:
    model = noteBook

    def __int__(self):
        self.engine = create_engine(get_database_url(), echo=False)
        self.session = sessionmaker(bind=self.engine)()

        if not inspect(self.engine).has_table(self.model.__tablename__):
            self.model.metadata.create_all(bind=self.engine)

    def list(self):
        return self.session.query(self.model).order_by(
            self.model.note_datetime.desc()
        ).limit(10).all()

    def find(self, description_contains):
        return self.session.query(self.model).filter(
            self.model.description.contains(description_contains)
        ).order_by(
            self.model.note_datetime.desc()
        ).all()

    def get(self, id):
        return self.session.query(self.model).get(id)

    def create(self, description, log_datetime, note_datetime=None):
        note_entry = self.model(
            description=description,
            note_datetime=note_datetime
        )
        try:
            self.session.add(note_entry)
            self.session.commit()
            return True, 'Note created😊😊'
        except Exception as e:
            self.session.rollback()
            return False, f'An error occurred while creating a note file.{e}'

    def update(self, id, description=None, note_datetime=None):
        if not description and not note_datetime:
            return False, 'oops you must provide "--description" and/or "--date and time--"'

        note_entry = self.session.query(self.model).get(id)

        if note_entry:
            if description:
                note_entry.description = description

            if note_datetime:
                note_entry.note_datetime = note_datetime

            try:
                self.session.commit()
                return True, 'Note successfully updated'
            except Exception as e:
                self.session.rollback()
                return False, f'Oops an error occurred while updating note.{e}'
            else:
                return False, f'Oops no note found with id={id} '

    def delete(self,id):
        delete_count = self.session.query(self.model).filter_by(id=id).delete()

        if delete_count > 0 :
            try :
                self.session.commit()
                return True,'Note successfully Deleted '
            except Exception as e :
                self.session.rollback()
                return False, f'Oops an error ocurred while deleting a note.{e}'
            else:
                return False , f'Oops no bote found with id={id}'
