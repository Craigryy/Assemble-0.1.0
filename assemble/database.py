import os
from tabulate import tabulate


def get_file_table(file_entries):
    """Create a dummy table for file/note Entries using tabulate"""
    table_data = [
        [
            entry.id,
            entry.title[0:30],
            entry.notes[0:30],
            entry.label[0:30],
            entry.folder_id
        ]
        for entry in file_entries
    ]

    table_headers = [
        "# ID",
        "Title",
        "notes",
        "label",
        "folder_id"
    ]

    return tabulate(
        table_data,
        headers=table_headers,
        tablefmt="pretty"
    )
def get_folder_table(folder_entries):
    """Create  dummy table for folder Entries using tabulate"""
    table_data = [
        [
            entry.id,
            entry.name[0:30],
            entry.notes[0:30]
        ]
        for entry in folder_entries
    ]

    table_headers = [
        "# ID",
        "NAME",
        "NOTES"
    ]

    return tabulate(
        table_data,
        headers=table_headers,
        tablefmt="pretty"
    )



def get_database_url():
    BASE_DIR= os.path.dirname(os.path.realpath(__file__))
    conn='sqlite:///'+os.path.join(BASE_DIR,'assemble.db')
    return conn
