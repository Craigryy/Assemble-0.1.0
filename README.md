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

## Installation

You can install `assemble-0.1.0  by downloading the zip file and saving the folder unto your desktop `:


```from your command prompt console
cd desktop(step 1)
cd assemble-0.1.0(step 2)
python -m assemble --help (step 3)
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

* `File`
* `Folder`


*** Folder Commands ***:
### `Folder add`

add a folder .
**Usage**:

```console
$ python -m assemble Folder add [OPTIONS] name notes
```

**Arguments**:

* `name`: name of the folder  [required]
* `notes`: note of the folder  [required]

**Options**:
* `--help`: Show this message and exit.

**Example:**

```console
$ python -m assemble Folder add  "random" "This is a good day"


### `Folder delete`

Delete a folder using it's ID.

**Usage**:


```console
$ python -m asssemble Folder delete [OPTIONS] ID
```

**Arguments**:

* `ID`: ID of Folder entry  [required]

**Options**:

* `--help`: Show this message and exit.

**Example:**

```console
$ python -m assemble Folder delete 1
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

```console
 __main__.py File edit-file [OPTIONS] TITLE NOTES LABEL
 
 
 Usage:
$ python -m assemble File edit-file [OPTIONS] title  notes label
```

### `File list-files`

List all files-entries with attached to a folder with a pre_existing csv file inserted into the database.

**Usage**:


```console
$ python -m asssemble File list-files 
```

**Options**:

* `--help`: Show this message and exit.



## Screenshot 

![mywork](https://user-images.githubusercontent.com/116971272/213660795-0044f390-b20b-436e-806f-c4936f758110.png)
