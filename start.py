import os

try:
    import requests
except:
    print(
        "\nIt looks like you don't have requests installed, to install it: \n\n",
        "pip install requests \n\n",
        "and run this file again.\n",
    )
    exit()

make_module_file_structure = False
module_commands = []

project_name = input("what do you want to call this project?\n:")
print("what shall we call the virtual environment for this project?")
venv_name = f"{project_name[:3]}-env"
venv_check = input(f"Are you are ok with {venv_name}? (Y/n)").upper()
if venv_check == "" or "Y" in venv_check:
    print("very cool venv name")
else:
    venv_name = input("venv name: ")

requirements = "\n".join(
    [
        "black",
        "git+https://github.com/notionparallax/pytestgen.git",
        "mypy",
        "pytest",
        "wheel",
        "bvn_values",
        "",
    ]
)


is_data = input("is this a data project? (adds pandas and that kind of thing) (Y,n): ")
if "Y" in is_data.upper() or is_data == "":
    requirements += "\n".join(
        [
            "pandas",
            "ipykernel",
            "matplotlib",
            "numpy",
            "pandas-stubs",
            "openpyxl",
        ]
    )

is_module = input(
    "is this project going to be a module on pypi?\n"
    "(sets up a folder structure and adds a few more requirements) (y,N): "
)
if "Y" in is_module.upper():
    requirements += "\n".join(["build", "twine", "flit"])
    make_module_file_structure = True

want_example = input("Do you want an example project? (Y,n): ")
if "Y" in want_example.upper():
    print("this is coming soon!   👀")
    # pseudocode:
    # make a tests folder
    # copy starter_project\starter_test.py to it
    # copy starter_project\starter_file.py to the project root
    # print some instructions on how to use it
    #   go to the tests tab on the left, set it up to use pytest, and the tests
    #   folder, use the tests in the bottom half of the panel, run the test, be
    #   happy, see ✔✔✔

try:
    os.mkdir(os.path.normpath(f"..\\{project_name}"))
except FileExistsError:
    pass  # all good, probably offer to overwrite one day?
if make_module_file_structure:
    # os.mkdir() src
    # os.mkdir() src/f"{project_name}""
    f"""
    {project_name}/
    │
    ├── src/
    │   └── {project_name}/
    │       ├── __init__.py
    │       ├── __main__.py
    │       ├── exampleA.py
    │       └── exampleB.py
    │
    ├── tests/
    │   ├── test_feed.py   TODO: eventually
    │   └── test_viewer.py TODO: eventually
    │
    ├── LICENSE
    ├── README.md
    └── pyproject.toml
    """
    # etc. by making an example set of files in this repo, and then copying them across
    init_py_contents = (
        # Write a docstring and a version number (0.1.0) to the __init__.py file
        '''"""This is the description of your project that will show up on pypi."""'''
        '\n__version=__version__ = "0.1.1"'
        "\n# importing these here makes them avaliable to the dir command"
        "\nfrom .exampleA import a"
        "\nfrom .exampleB import b"
    )
    readme_contents = f"# {project_name}\n\nTell us things about this project!"
    # Add instruction for flit init to module_commands
    #

with open(
    os.path.normpath(f"..\\{project_name}\\requirements.in"), "w", encoding="utf-8"
) as req_f:
    req_f.write(requirements)

py_gitignore = requests.get(
    "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
).text
py_gitignore += "\n\n# OUR OWN STUFF"
py_gitignore += f"\n{venv_name}"
with open(
    os.path.normpath(f"..\\{project_name}\\.gitignore"), "w", encoding="utf-8"
) as req_f:
    req_f.write(py_gitignore)

# TODO: implement these in code
message = f"""
Your next jobs are:
    Copy the following lines into your terminal:

cd ..\\{project_name}
code .

    Then stop and paste this lot:
    ⚠ VS Code notices that a new venv is created, and does some admin.
    ⚠ It really helps to have that, so do this once the window has settled fully.

"""
commands = "\n".join(
    [
        # Make a new virtual environment. This uses --copies because the BVN
        # environment seems to break whenever there's a new image made. This is
        # trying to prevent that by reducing the use of symlinks.
        f"python -m venv --copies {venv_name}",
        # Activate that environment
        f"{venv_name}\\Scripts\\activate.bat",
        'echo "🚪"',
        # Upgrade pip, it's usually a few versions behind at this point
        "python -m pip install --upgrade pip",
        # Install pip-tools https://github.com/jazzband/pip-tools
        # This is what allows us to do pip-compile
        "python -m pip install pip-tools",
        # Compile the requirements.in into a well anotated requirements.txt
        # NOTE: pip-compile won't work if you're not in a venv
        "pip-compile requirements.in",
        'echo "🚀"',
        # install all the base requirements
        "pip install -r requirements.txt",
        # Initialise this folder as a git repo
        "git init",
        'echo "🍟🍟🍟"',
        # An empty line to make sure that the last line gets excecuted
        "#",
    ]
) + "\n".join(module_commands)


print(message + commands)
