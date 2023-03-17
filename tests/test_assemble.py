from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from unittest import TestCase

from assemble.models import Folder, File, Base
from assemble.utilis import get_database_url


class ParentChildModelTest(TestCase):
    engine = create_engine(get_database_url(), echo=True)

    def setUp(self):
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # Create a Parent object
        self.folder = Folder('John', 'hello how are you')
        self.session.add(self.folder)
        self.session.commit()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_query_folder(self):
        expected = [self.folder]
        result = self.session.query(Folder).all()
        self.assertEqual(result, expected)

    def test_query_update(self):
        expected = [self.folder]
        self.folder.name = 'am updated'
        self.session.commit()

        result = self.session.query(Folder).all()
        self.assertEqual(result, expected)

    def test_delete_query(self):
        self.folder = Folder('Parent 4', 'hello')
        self.session.add(self.folder)
        self.session.commit()

        expected = self.session.delete(self.folder)

        result = self.session.query(Folder).all()
        self.assertNotEqual(result, expected)

    def test_create_file(self):
        # Create a Child object linked to the parent object created in setUp()
        self.file = File(title='Alice', notes='hello', label='jesus' , author=self.folder)
        self.session.add(self.file)
        self.session.commit()

        # Verify that the child was created and linked to the parent
        retrieved_file = self.session.query(File).all()
        expected = [self.file]

        self.assertEqual(expected, retrieved_file)

    # def test_query_update(self):
    #     expected=[self.file.title=='koko']
    #     self.session.commit()

    #     result = self.session.query(File).all()
    #     self.assertEqual(result,expected)

    def test_delete_file(self):
        # create a file object
        self.file = File(title='Al', notes='hello', label='jesus' , author=self.folder)
        self.session.add(self.file)
        self.session.commit()

        expected = self.session.delete(self.file)
        # Query the database for a child by name
        result = self.session.query(File).all()

        # Delete the child from the databases
        self.assertNotEqual(result, expected)
