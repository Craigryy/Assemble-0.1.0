from datetime import datetime

import typer

from .managers import noteBookManager
from .assemble import get_table

app = typer.Typer(help="Command line tool to keep notes.")


@app.command(name='list')
def list_log_entries():
    """
    List all log entries in a table, limits up to 10 log entries.
    """
    manager = noteBookManager()
    note_entries = manager.list()

    if note_entries:
        typer.echo(get_table(note_entries))
    else:
        typer.echo(
            typer.style(
                f'You do not have any entries in your note book.',
                fg=typer.colors.MAGENTA,
                bold=True
            )
        )


@app.command()
def find(
        title: str = typer.Argument(
            ...,
            help="String that may match title entry description"
        ),
        notes: str = typer.Argument(
            ...,
            help="string that may match notes entry description"

        ),
        label: str = typer.Argument(
            ...,
            help="String that may match label entry description"
        )
):
    """
    List all log entries that match the argument.
    """
    manager = noteBookManager()
    note_entries = manager.find(title, notes, label)

    if note_entries:
        typer.echo(get_table(note_entries))
    else:
        typer.echo(
            typer.style(
                f'You do not have any entries matching '
                f'"{title, notes, label}" in your log book.',
                fg=typer.colors.RED,
                bold=True
            )
        )


@app.command()
def view(
        id: int = typer.Argument(
            ...,
            help="ID of the Note entry"
        )
):
    """
    View a single note entry using it's ID.
    """
    manager = noteBookManager()
    note_entry = manager.get(id)

    if note_entry:
        note_entry_id = (
                typer.style("Note Entry ID: ", fg=typer.colors.BRIGHT_BLUE, bold=True) +
                str(note_entry.id)
        )
        typer.echo(note_entry_id)

        note_datetime = (
                typer.style("Note Date & Time: ", fg=typer.colors.BRIGHT_BLUE, bold=True) +
                note_entry.log_datetime.strftime("%Y-%m-%d %I:%M %p")
        )
        typer.echo(note_datetime)

        typer.echo(
            typer.style("\nTitle:\n", fg=typer.colors.BRIGHT_BLUE, bold=True)
        )
        typer.echo(note_entry.title + '\n')

        created_at = (
                typer.style("Created at: ", fg=typer.colors.BRIGHT_BLUE, bold=True) +
                note_entry.created_at.strftime("%Y-%m-%d %I:%M %p")
        )
        typer.echo(created_at)

        updated_at = (
                typer.style("Updated at: ", fg=typer.colors.BRIGHT_BLUE, bold=True) +
                note_entry.updated_at.strftime("%Y-%m-%d %I:%M %p")
        )
        typer.echo(updated_at)
    else:
        typer.echo(
            typer.style(
                f'No Note Entry Found with id={id}',
                fg=typer.colors.RED,
                bold=True
            )
        )


@app.command()
def add(
        title: str = typer.Argument(
            ...,
            help="Description of the log entry"
        ),
        notes: str = typer.Argument(
            ...,
            help="Description of the note entry"
        ),
        label: str = typer.Argument(
            ...,
            help="Label of the note entry"
        ),
        date: datetime = typer.Option(
            datetime.now().strftime("%Y-%m-%d"), '--date', '-d',
            help="Date of the log entry"
        ),
        time: datetime = typer.Option(
            datetime.now().strftime("%I:%M %p"), '--time', '-t',
            formats=["%H:%M:%S", "%I:%M %p"],
            help="Time of the log entry"
        )
):
    """
    Add a log entry to the logbook.
    """
    note_entry_time = time.time()
    note_datetime = datetime.combine(date, note_entry_time)

    manager = noteBookManager()
    created, message = manager.create(title, notes, label, note_datetime)

    if created:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )


@app.command()
def edit(
        id: int = typer.Argument(
            ...,
            help="ID of the log entry"
        ),
        title: str = typer.Option(
            "", '--description',
            help="New Description for the log entry"
        ),
        notes: str = typer.Option(
            "", '--description',
            help="New Description for the log entry"
        ),
        label: str = typer.Option(
            "", '--description',
            help="New Description for the log entry"
        ),
        date: datetime = typer.Option(
            None, '--date', '-d',
            help="New Date for the log entry"
        ),
        time: datetime = typer.Option(
            None, '--time', '-t',
            formats=["%H:%M:%S", "%I:%M %p"],
            help="New Time for the log entry"
        )
):
    """
    Update a log entry using it's ID.
    """
    note_datetime = None

    if date and time:
        note_entry_time = time.time()
        note_datetime = datetime.combine(date, note_entry_time)

    manager = noteBookManager()
    updated, message = manager.update(
        id,
        title=title,
        notes=notes,
        label=label,
        note_datetime=note_datetime
    )

    if updated:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )


@app.command()
def delete(
        id: int = typer.Argument(
            ...,
            help="ID of the log entry"
        )
):
    """
    Delete a log entry using it's ID.
    """
    manager = noteBookManager()
    deleted, message = manager.delete(id)

    if deleted:
        typer.echo(
            typer.style(message, fg=typer.colors.GREEN, bold=True)
        )
    else:
        typer.echo(
            typer.style(message, fg=typer.colors.RED, bold=True)
        )

