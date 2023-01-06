from pathlib import Path

path = Path("packages")

# iterdir() returns the list of file and directories in a given path
paths = [p for p in path.iterdir()]
# print(paths)

# using path.glob() - This is used to search for files or directories by some pattern
# It is also used to list files or directories recursively in a given path
py_files = [p for p in path.rglob("*.py")]
print(py_files)