from assemble import __version__
import unittest
from assemble.models import Folder, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class TestQuery(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = Session(self.engine)
        Base.metadata.create_all(self.engine)
        self.folder = Folder('ion torrent', 'start')
        self.session.add(self.folder)
        self.session.commit()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_query_folder(self):
        expected = [self.folder]
        result = self.session.query(Folder).all()
        self.assertEqual(result, expected)


def test_version():
    assert __version__ == '0.1.0'
