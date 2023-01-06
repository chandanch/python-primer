from pathlib import Path

log_path = Path("log.txt")

script_path = Path("../streams/stream.py")

# print(script_path.cwd())

# parent folder name or the folder in which the file exists
# print(script_path.parent)

# Path instances also offer the with_name function that allow you to seamlessly create a new
# Path object with a different name
log_path = log_path.with_name("log2.txt")
# print(log_path.absolute())
empty_path = Path("packages", "streams")
# empty_path = empty_path.with_name("log3.txt")
print(empty_path.parent)
