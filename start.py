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

requirements = """
black
git+https://github.com/notionparallax/pytestgen.git
mypy
pytest
wheel
"""

is_data = input("is this a data project? (adds pandas and that kind of thing) (Y,n): ")
if "Y" in is_data.upper() or is_data == "":
    requirements += "\n".join(["pandas", "ipykernel", "matplotlib", "numpy"])


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
print(
    f"""
Next jobs
Copy the following lines into your terminal:

cd ..\\{project_name}
code . -r

then stop and paste this lot:

python -m venv --copies {venv_name}
{venv_name}\\Scripts\\activate.bat
echo "🚪"
python -m pip install --upgrade pip
python -m pip install pip-tools
pip-compile requirements.in
echo "🚀"
pip install -r requirements.txt
git init
echo "🍟🍟🍟"
#

"""
)
