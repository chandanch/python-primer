"""
    The ZipFile Module enables operations with the Zip file
"""

from pathlib import Path
from zipfile import ZipFile

file_path = Path("packages")

# Create a Zip File - Using with statement to create a zip file,
# using the with statement ZipFile.close() method will be called automatically 
# once the files added to zip file
# with ZipFile("files.zip", "w") as zip_file:
#     for path in file_path.rglob("*.*"):
#         zip_file.write(path)

# Read contents of zipfile and zipfile metadata
with ZipFile("files.zip") as zip_file:
    print(zip_file.namelist())

# Extract all the files from a zip file
with ZipFile("files.zip") as zip_file:
    zip_file.extractall("extractors")