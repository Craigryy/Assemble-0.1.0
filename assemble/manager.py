import csv
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from assemble.models import Folder, File
from assemble.database import get_database_url


class fileManger:
    model=Folder
    model_2=File


    def __init__(self):
        #create engine and con to the database
        self.engine = create_engine(get_database_url(), echo=False)
        #create a session and bind to engine
        self.session = sessionmaker(bind=self.engine)()
        if not inspect(self.engine).has_table(self.model_2.__tablename__):
            self.model_2.metadata.create_all(bind=self.engine)


    def save(self, obj):
        self.session.add(obj)
        self.session.commit()


    def insert(self,csv_filename):
        # Open the CSV file and insert its contents into the table
        with open(csv_filename) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip reader row
            for row in reader:
                data = File(title=row[0],
                            notes=row[1],
                            label=row[2]
                            )

        self.save(data)


    def search(self, first_letter):
        #Query the database to return a file entry
        return self.session.query(self.model_2).filter(self.model_2.title.ilike(f"{first_letter}%")).all()


    def view(self,title):
        return self.session.query(self.model_2).filter(self.model_2.title==title).all()


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


    def delete(self, name):
        """
        delete a file using its name
        """
        # Query the database and return a file entry by its name
        folder_to_delete = self.session.query(self.model_2).filter(File.name == name).first()
        #Delete the file by its name
        self.session.delete(folder_to_delete)
        try:
            self.session.commit()
            return True, 'File deleted'
        except Exception as e:
            self.session.rollback()
            return False, f'An error oc+curred while deleting a File. {e}'


    def add_file(self,ctitle: str, cnotes: str, clabel=None):
        """
        create a file entry
        """
        if clabel is None :
            # query database for a default folder
            default_folder = self.session.query(self.model).filter(self.model.name == 'default_folder').first()
            if default_folder:
                clabel = "default"
                child = File(title=ctitle, notes=cnotes, label=clabel, author=default_folder)
                self.save(child)
                return False,f"Default folder created and file added to folder name : {default_folder.name}. "

        elif clabel is not None :
            #query the database folder that matches the file
            file_folder = self.session.query(Folder).filter(Folder.name == clabel).first()
            if file_folder:
                NewFile = File(title=ctitle, notes=cnotes, label=clabel, author=file_folder)
                self.save(NewFile)
                return True,f"file added to folder name:{NewFile.label}"
            else:
                #create a new folder
                fol=Folder(name="default_file",notes="man")
                self.save(fol)
                NewFile = File(title=ctitle, notes=cnotes, label=clabel, author=file_folder)
                self.save(NewFile)
                return True, f"file added to an existng folder name:{NewFile.label}"

        else:
            #create a new folder
            folder=Folder(name="default_file",notes="have a nice day")
            self.session.add(folder)
            file=File(title=ctitle,notes=cnotes,label=clabel,author=folder)
            self.save(file)
            return True,f"new folder : {folder.name} created with file title : {file.title} added."


class folderManager:
    model=Folder
    model_2=File

    def __init__(self):
        self.engine = create_engine(get_database_url(), echo=False)
        self.session = sessionmaker(bind=self.engine)()

        if not inspect(self.engine).has_table(self.model.__tablename__):
            self.model.metadata.create_all(bind=self.engine)


    def save(self, obj):
        self.session.add(obj)
        self.session.commit()

    def get(self,name):
        # Get a folder Item
        folder_items = self.session.query(self.model).filter(Folder.name==name).first()
        return folder_items

    def list(self):
        # List all folder entries.
        return self.session.query(self.model).all()

    def addFolder(self,name, notes):
        # Add a folder entry
        new_folder = Folder(name, notes)
        # check if a folder with the same name already exists in the database
        existing_folder = self.session.query(self.model).filter(Folder.name == new_folder.name).first()
        # if a folder with the same name exists,don't add the new folder and return an error message
        if existing_folder:
            return False, f"A folder with the name '{new_folder.name}'already exists in the database.Cannot add the new Folder."
        # if a folder with the same name does not exist ,add the new folder to the database
        else:
            self.save(new_folder)
            return True, f"Added folder '{new_folder.name}'with ID '{new_folder.id}' to the database."

    def delete_all(self):
        # Query and delete all Folders
        self.session.query(self.model).delete()
        self.session.query(self.model_2).delete()
        try:
            self.session.commit()
            return True, 'All folders deleted'
        except Exception as e:
            return False, f'An error occurred while deleting all folder. {e}'

    def delete(self, name):
        # Delete a particular folder entry using its name
        Folder_to_delete = self.session.query(Folder).filter(Folder.name == name).first()
        self.session.delete(Folder_to_delete)
        try:
            self.session.commit()
            return True, 'Folder deleted'
        except Exception as e:
            self.session.rollback()
            return False, f'An error occurred while deleting a folder. {e}'

