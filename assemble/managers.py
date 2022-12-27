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

    def find(self, title_contains, note_contains, label_contains):
        return self.session.query(self.model).filter(
            self.model.title.contains(title_contains, note_contains, label_contains)
        ).order_by(
            self.model.note_datetime.desc()
        ).all()

    def get(self,identity ):
        return self.session.query(self.model).get(identity)

    def create(self, title, notes, label, note_datetime):
        note_entry = self.model(
            title=title,
            notes=notes,
            label=label,
            note_datetime=note_datetime
        )
        try:
            self.session.add(note_entry)
            self.session.commit()
            return True, 'Note created😊😊'
        except Exception as e:
            self.session.rollback()
            return False, f'An error occurred while creating a note file.{e}'

    def update(self, identity, title=None, notes=None, label=None, note_datetime=None):
        if title or notes or label or note_datetime:
            return False, 'you must provide details.'

            note_entry = self.session.query(self.model).get(identity)
            
                try:
                    self.session.commit()
                    return True, 'Note successfully updated'
                except Exception as e:
                    self.session.rollback()
                    return False, f'Oops an error occurred while updating note.{e}'
                else:
                    return False

    def delete(self, identity):
        delete_count = self.session.query(self.model).filter_by(identity=identity).delete()

        if delete_count > 0:
            try:
                self.session.commit()
                return True, 'Note successfully Deleted '
            except Exception as e:
                self.session.rollback()
                return (False, f'Oops an error ocurred while deleting a note.{e}')
