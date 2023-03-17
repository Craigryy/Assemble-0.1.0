import os
from tabulate import tabulate


def get_file_table(file_entries):
    """Create table for file Entries using tabulate."""
    table_data = []
    for file in file_entries:
        table_data.append([file.id, file.title, file.notes,
                          file.label, file.folder_id])

    # use tabulate library to format the table
    table_headers = [
        "# ID",
        "Title",
        "Notes",
        "Label",
        "Folder_id"
    ]
    return tabulate(
        table_data,
        headers=table_headers,
        tablefmt="pretty"
    )


def get_folder_table(folder_entries):
    """Create table for folder Entries using tabulate."""
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
        "Name",
        "Notes"
    ]

    return tabulate(
        table_data,
        headers=table_headers,
        tablefmt="pretty"
    )


def get_database_url():
    """Get Database URL from environment variable."""
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    conn = 'sqlite:///' + os.path.join(BASE_DIR, 'assemble.db')
    return conn
