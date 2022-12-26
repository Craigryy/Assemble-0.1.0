import os
from pathlib import Path

from tabulate import tabulate


def get_table(note_entries):
    """Create table for Log Entries using tabulate"""
    table_data = [
        [
            entry.id,
            entry.description[0:30],
            entry.log_datetime.strftime("%Y-%m-%d %I:%M %p"),
            entry.created_at.strftime("%Y-%m-%d %I:%M %p"),
            entry.updated_at.strftime("%Y-%m-%d %I:%M %p")
        ]
        for entry in note_entries
    ]

    table_headers = [
        "# ID",
        "description",
        "Log Datetime",
        "Created At",
        "Updated At"
    ]

    return tabulate(
        table_data,
        headers=table_headers,
        tablefmt="pretty"
    )


def get_database_url():
    """Get Database URL from environment variable or "~/.notebook/" directory"""
    NOTE_BOOK_DATABASE_URL = os.environ.get('NOTE_BOOK_DATABASE_URL')

    if NOTE_BOOK_DATABASE_URL:
        return NOTE_BOOK_DATABASE_URL

    database_directory = str(Path.home() / '.notebook')

    # create "~/.logbook/" directory if it does not exist
    Path(database_directory).mkdir(parents=True, exist_ok=True)

    return 'sqlite:///' + database_directory + '/notebook.sqlite3'
