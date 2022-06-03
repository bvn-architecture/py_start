import os
import requests


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
        "black"
        "git+https://github.com/notionparallax/pytestgen.git"
        "mypy"
        "mypy"
        "pytest"
        "wheel"
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
        ]
    )


try:
    os.mkdir(os.path.normpath(f"..\\{project_name}"))
except FileExistsError:
    pass  # all good, probably offer to overwrite one day?

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
)

print(message + commands)
