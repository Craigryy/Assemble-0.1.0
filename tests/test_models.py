# import unittest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from assemble.models import Folder, File
# from assemble.utilis import get_database_url

# class TestParentChildCRUD(unittest.TestCase):
#     def setUp(self):
#         engine = create_engine(get_database_url())
#         Session = sessionmaker(bind=engine)
#         self.session = Session()

#     def tearDown(self):
#         self.session.rollback()
#         self.session.close()

#     def test_create(self):
#         self.parent = Folder(name='Parent 1',notes='hello')
#         self.session.add(self.parent)
#         self.session.commit()
#         expected=[self.parent]
#         result=self.session.query(Folder).all()
#         self.child = File(title='Child 1',notes='hello',label='hiyyyy', author=self.parent)
#         self.session.add(self.child)
#         self.session.commit()
#         expected_child=[self.child]
#         result2=self.session.query(File).all()
#         self.assertEqual(result,expected)
#         self.assertEqual(result2,expected_child)

#     # def test_read(self):
#     #     self.parent = Folder(name='Parent 2',notes='mum')
#     #     self.child = File(title='Child 2',notes='mum',label='hiyyy', author=self.parent)
#     #     self.session.add(self.child)
#     #     self.session.commit()

#     #     result = self.session.query(File).filter(self.child.title=='Child 2').first()
#     #     self.assertIsNotNone(result)
#     #     self.assertEqual(result, 'Parent 2')

#     # def test_update(self):
#     #     parent = Parent(name='Parent 3')
#     #     child = Child(name='Child 3', parent=parent)
#     #     self.session.add(child)
#     #     self.session.commit()

#     #     child.name = 'Child 3 Updated'
#     #     self.session.commit()

#     #     result = self.session.query(Child).filter_by(name='Child 3 Updated').first()
#     #     self.assertIsNotNone(result)
#     #     self.assertEqual(result.parent.name, 'Parent 3')

#     # def test_delete(self):
#     #     parent = Parent(name='Parent 4')
#     #     child = Child(name='Child 4', parent=parent)
#     #     self.session.add(child)
#     #     self.session.commit()

#     #     self.session.delete(child)
#     #     self.session.commit()

#     #     result = self.session.query(Child).filter_by(name='Child 4').first()
#     #     self.assertIsNone(result)
