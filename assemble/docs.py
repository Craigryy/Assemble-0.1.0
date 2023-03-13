import typer


app = typer.Typer(help="Generate a markdown documentation")


@app.command()
def Docs(folder: str, file: str, one_to_many: bool = True):
    """
    Generate Markdown documentation for CRUD operation of a folder and child in one-many relationship .
    """
    title = f"{folder.title()} and {file.title()} CRUD Documentation"
    print(f"#{title}\n")

    if one_to_many:
        print(f"## {folder.title()}\n")
        print(f"### Create {folder.title()}\n")
        print("### Request\n")
        print(
            "json\n{{\n    \"id\": \"integer\",\n    \"name\": \"string\", \"notes\":\"string\"\n}}\n")
        print(f"### Get {folder.title()}\n")
        print("#### Request\n")
        print(f"http\nGET /{folder.lower()}s/{{id}}\n")
        print("#### Response\n")
        print(
            f"json\n{{\n    \"id\": \"integer\",\n    \"name\": \"string\",\n    \"{file.lower()}s\": [\n              {{\n       \"id\": \"integer\",\n            \"title\": \"string\",\n    \"notes\": \"string\",\n   \"label\": \"string\",\n       }}\n    ]\n}}\n")

        print(f"## {file.title()}\n")
        print(f"### Create {file.title()}\n")
        print("#### Request\n")
        print(f"json\n{{\n    \"title\": \"string\",\n   \"notes\": \"string\",\n   \"label\": \"string\"\n,    \"{folder.lower()}_id\": \"integer\"\n}}\n")
        print("#### Response\n")
        print(
            f"json\n{{\n    \"id\": \"integer\",\n   \"title\": \"string\",\n   \"notes\": \"string\",\n    \"label\": \"string\",\n     \"{folder.lower()}_id\": \"integer\"\n}}\n")
        print(f"### Get {file.title()}\n")
        print("#### Request\n")
        print(f"http\nGET /{file.lower()}s/{{id}}\n")
        print("#### Response\n")
        print(
            f"json\n{{\n    \"id\": \"integer\",\n    \"title\": \"string\",\n       \"notes\": \"string\",\n    \"label\": \"string\",\n      \"{folder.lower()}_id\": \"integer\",\n    \"{folder.lower()}\": {{\n        \"id\": \"integer\",\n        \"name\": \"string\"\n    }}\n}}\n")

    else:
        # Code for many-to-many relationship CRUD documentation
        pass
