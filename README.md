![WhatsApp Image 2022-12-27 at 17 01 20](https://user-images.githubusercontent.com/116971272/209692029-de0aad6d-b3e7-4df1-a728-5da726c35752.jpg)
# assemble
a command line tool for a folder application

# Configuration
assemble-cli stores the sqlite database in -/.notebook/directionary by default.
exaample:
export NOTE_BOOK_DATABASE_URL=sqlite:///]

# Options:
*--install--completion: Install completion for the current shell.
--show-completion: Show completion for the current shell, to copy it or customize the installation .
--help: Show this message and exit .

# Commands:
*add : Adds a note entry  to the notebook.
delete: Delete a note entry using it's ID
edit: Update a note entry using it's ID
find:list all note entries that match the argument
list: List all note entries in a table , limits upto...
view : View a single entry using it's ID.
