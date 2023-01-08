"""
    A process is basically an running instance of a program
    Subprocess is used to spawn child processes
"""

import subprocess

completed = subprocess.run(["python", "other_script.py"],
                           capture_output=True,
                           text=True,
                           check=True)

print(completed.returncode)
if completed.returncode != 0:
    print(completed.stderr)
else:
    print(completed.stdout)
