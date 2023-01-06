from pathlib import Path
from time import ctime
import shutil

path = Path("standard-library", "log.txt")

# Get metadata of the file, ex: size, created date time etc.
print(path.stat())
# using ctime convert epoch time to human readable format
print(ctime(path.stat().st_ctime))

# Read the contents of the file as text
print(path.read_text())

# Write data to text file
path.write_text("Adding details")
print("***",path.read_text())

# Copy file
source_path = Path("standard-library", "log.txt")
dest_path = Path("packages", "logv2.log")
shutil.copy(path, dest_path)