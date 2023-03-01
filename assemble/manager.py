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


    def search(self, first_letter):
        #Query the database to return a file entry
        return self.session.query(self.model_2).filter(File.title.ilike(f"{first_letter}%")).all()


    def view(self,title):
        return self.session.query(self.model_2).filter(File.title==title).all()


    def list(self):
        #Query the database to return a list of all file entries
        return self.session.query(self.model_2).all()


    def update(self, title=None, notes=None, label=None):
        if not title and not notes and not label:
            return False, f'you  have  failed to provide an update'

        file_entry = self.session.query(File).filter(Folder.name == title).first()

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


    def addFile(self, ctitle, cnotes, clabel):
        # Query the database to find a folder whose Folder name match the file tag and return the first item
        file_folder = self.session.query(Folder).filter(Folder.name == clabel).first()
        # If  a file_folder exist in the database, create a file and add .
        if file_folder is not None:
            NewFile = File(title=ctitle, notes=cnotes, label=clabel, author=file_folder)
            # create add session
            self.session.add(NewFile)
            self.session.commit()
            # close session
            self.session.close()
            return True, "File added to existing folder."
        else:
            # Create a default folder
            default_folder = self.session.query(Folder).filter(Folder.name == 'default').first()
            if default_folder is None:
                default_folder = Folder(name="default", notes='have a nice day ')
                self.session.add(default_folder)
                # Create a new file with the default Folder
                new_file = File(title=ctitle, notes=cnotes, label=clabel, author=default_folder)
                self.session.add(new_file)
                self.session.commit()
                # close session
                self.session.close()
                return False, "File added to folder name: {default_folder.name} with ID: {default_folder.id}."



    def delete(self, name):
        # Delete a particular file entry using its name
        folder_to_delete = self.session.query(self.model_2).filter(File.name == name).first()
        self.session.delete(folder_to_delete)
        try:
            self.session.commit()
            return True, 'File deleted'
        except Exception as e:
            self.session.rollback()
            return False, f'An error occurred while deleting a File. {e}'


class folderManager:
    model = Folder
    model_2 = File

    def __init__(self):
        self.engine = create_engine(get_database_url(), echo=False)
        self.session = sessionmaker(bind=self.engine)()

        if not inspect(self.engine).has_table(self.model.__tablename__):
            self.model.metadata.create_all(bind=self.engine)

    def get(self,name):
        # Get a folder Item
        folder_items = self.session.query(self.model).filter(Folder.name==name).first()
        return folder_items

    def list(self):
        # List all folder entries.
        return self.session.query(self.model).all()

    def addFolder(self, name, notes):
        # Add a folder entry
        new_folder = Folder(name, notes)
        # check if a folder with the same name already exists in the database
        existing_folder = self.session.query(self.model).filter(Folder.name == new_folder.name).first()
        # if a folder with the same name exists,don't add the new folder and return an error message
        if existing_folder:
            return False, f"A folder with the name '{new_folder.name}'already exists in the database.Cannot add the new Folder."
        # if a folder with the same name does not exist ,add the new folder to the database
        else:
            self.session.add(new_folder)
            self.session.commit()
            return True, f"Added folder '{new_folder.name}'with ID '{new_folder.id}' to the database."

    def delete_all(self):
        # Query and delete all Folders
        self.session.query(self.model).delete()
        self.session.query(self.model_2).delete()
        try:
            self.session.commit()
            return True, 'All folders deleted'
        except Exception as e:
            self.session.rollback()
            return False, f'An error occurred while deleting all folder. {e}'

    def delete(self, name):
        # Delete a particular folder entry using its name
        Folder_to_delete = self.session.query(self.model).filter(Folder.name == name).first()
        self.session.delete(Folder_to_delete)
        try:
            self.session.commit()
            return True, 'Folder deleted'
        except Exception as e:
            self.session.rollback()
            return False, f'An error occurred while deleting a folder. {e}'

