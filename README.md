
![209692029-de0aad6d-b3e7-4df1-a728-5da726c35752](https://user-images.githubusercontent.com/116971272/224728373-63da0233-adc6-4429-9c10-b3d98fe6cb13.jpg)
# assemble
a command line tool to assemble your files into your folders 

# Configuration
assemble-cli stores the SQLite database in -/.notebook/directory by default.
example:
export NOTE_BOOK_DATABASE_URL=sqlite:///]

# Options:
*--install--completion: Install completion for the current shell.
--show-completion: Show completion for the current shell, to copy it or customize the installation.
--help: Show this message and exit.

## Installation
 Download the zip file and extract all the files in the folder after which go into your console `:

from your command prompt or git bash 
1. cd to downloads or directory the folder is located
2. Write on console


![Screenshot (13)](https://github.com/Craigryy/Assemble-0.1.0/assets/116971272/54cbde2c-faa3-4a35-aed7-cdcaae001cf7)



``` console
 'poetry run python -m assemble --help'
```

## How to use `assemble-0.1.0`
**Usage**
```console
$ __main__.py [OPTIONS] COMMAND [ARGS]...
```

**Options**:
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.


**Commands**:
* `Docs`
* `File`
* `Folder`

*** Docs Commands***:
* `Docs used to generate a markdown documentation`

**Usage**:
Usage: __main__.py Docs [OPTIONS] COMMAND [ARGS]...

  Generate a markdown documentation

**Option**:
  --help  Show this message and exit.

**Commands**:
  -docs  Generate Markdown documentation for CRUD operation of a folder and...

**console:
>poetry run python -m assemble Docs docs
Usage: __main__.py Docs docs [OPTIONS] FOLDER FILE
Try '__main__.py Docs docs --help' for help.

Error: Missing argument 'FOLDER'.

**Arguments**:

* `Folder`: name of the folder  [required]
* `File`: name of the file  [required]


***Folder***

*** Folder Commands ***:
### `Folder add`

add a folder .
**Usage**:

```console
$poetry run python -m assemble Folder add [OPTIONS] name notes
```

**Arguments**:

* `name`: name of the folder  [required]
* `notes`: note of the folder  [required]

**Options**:
* `--help`: Show this message and exit.

**Example:**

```console
$ poetry run python -m assemble Folder add  "random" "This is a good day"


```


### `Folder delete`
```console
$ python -m asssemble Folder delete [OPTIONS] NAME
```

**Arguments**:

* `NAME`: NAME of Folder entry  [required]

**Options**:

* `--help`: Show this message and exit.

**Example:**

```console
$ python -m assemble Folder delete name
```

### `Folder listfolders`

List all folder entries .

**Usage**:


```console
$ python -m asssemble Folder listfolders 
```

**Options**:

* `--help`: Show this message and exit.

**Example:**

```console
$ python -m assemble Folder listfolders
```


### `File add`

Add a file entry to a folder.

**Usage**:

```console
$ python -m assemble File add [OPTIONS] ctitle  cnotes clabel
```

**Arguments**:

* `ctitle`: title of the file entry  [required]
* `cnotes`: notes of the file entry  [required]
* `clabel`: label of the file entry  [required]

**Options**:
* `--help`: Show this message and exit.

**Example:**

```console
$ python -m assemble File add  "First leg"  "The 2023 Marathon route runs through all 4 areas of the field" "random"
```


### `File edit-files`

Edit a file entry to a folder.

**Usage**:
 
 Usage:
```console
$ python -m assemble File edit-file [OPTIONS] title  notes label
```

### `File list-files`

List all files-entries attached to a folder with a pre_existing csv file inserted into the database.

**Usage**:


```console
$ python -m asssemble File list-files 
```

**Options**:

* `--help`: Show this message and exit.


### `File delete`

Delete all files-entries in the database.

**Usage**:


```console
$ python -m asssemble File delete name 
```

**Options**:

* `--help`: Show this message and exit.
