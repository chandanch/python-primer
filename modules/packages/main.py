"""
    Packages helps to group related modules together, it enables organization of modules
    into a folder
    In order to mark a folder as a package we must add the __init__.py file, python will consider
    the folder as a package
"""

from logger.log import write_logs, read_logs
from streams import stream

write_logs()
read_logs()

stream.create_stream()