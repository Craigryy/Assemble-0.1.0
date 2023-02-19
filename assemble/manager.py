import csv
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from assemble.models import Folder, File
from assemble.database import get_database_url




class fileManger:
    model_2 = File
    model = Folder

    def __init__(self):
        self.engine = create_engine(get_database_url(), echo=False)
        self.session = sessionmaker(bind=self.engine)()
        if not inspect(self.engine).has_table(self.model_2.__tablename__):
            self.model_2.metadata.create_all(bind=self.engine)



    def addFile(self, ctitle, cnotes, clabel):
        # get a folder object you want to add the file to
        existing_folder = self.session.query(Folder).filter(Folder.name == clabel).first()
        try:
            new_file = File(title=ctitle, notes=cnotes, label=clabel, author=existing_folder)
            self.session.add(new_file)
            self.session.commit()
            return True,f'successfully saved '
        except Exception as e:
            self.session.rollback()
            return False,f'an error .{e}'


    def find(self, title):
        #find a specific file entry using its title
        return self.session.query(File).filter(File.title == title).all()

    def read_csv(self):
        #read data from csv file
        with open('notes-app.csv','r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)#skip the header row
            for row in reader:
                #create an instance of the file class with the row data
                csv_data= File(title=row[0],notes=row[1],label=row[2],folder_id=row[3])
                self.session.add(csv_data)
                self.session.commit()
                self.session.close()


    def list(self):
        #return list of all file entries
        all_file = self.session.query(File).all()
        return all_file


    def update(self, title=None, notes=None, label=None):
        if not title and not notes and not label:
            return False, f'you  have  failed to provide an update'

        file_entry = self.session.query(File).filter(Folder.name == label).first()

        if file_entry:
            if title:
                file_entry.title = title

            if notes:
                file_entry.notes = notes

            if label:
                file_entry.label = label

            try:
                self.session.commit()
                return True, 'file Entry Updated'
            except Exception as e:
                self.session.rollback()
                return False, f'An error occurred while updating file Entry. {e}'
        else:
            return False, f'No file Entry found with label={label}'


class folderManager:
    model = Folder
    model_2 = File

    def __init__(self):
        self.engine = create_engine(get_database_url(), echo=False)
        self.session = sessionmaker(bind=self.engine)()

        if not inspect(self.engine).has_table(self.model.__tablename__):
            self.model.metadata.create_all(bind=self.engine)


    def get(self):
        # Get a folder Item
        folder_items = self.session.query(self.model).all()
        return folder_items

    def list(self):
        #List all folder entries.
        return self.session.query(self.model).all()

    def addFolder(self, name, notes):
        #Add a folder entry
        new_folder = Folder(name, notes)
        try:
            self.session.add(new_folder)
            self.session.commit()
            return True, f'Folder created .'
        except Exception as e:
            self.session.rollback()
            return False, f'An error occurred while creating a folder. {e}'

    def delete(self, id):
        #Delte a particular folder entry using its ID
        Folder_to_delete = self.session.query(self.model).filter(Folder.id == id).first()
        self.session.delete(Folder_to_delete)
        try:
            self.session.commit()
            return True, 'Folder deleted'
        except Exception as e:
            self.session.rollback()
            return False, f'An error occurred while deleting a folder. {e}'
