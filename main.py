import subprocess
import os
import sys
from pathlib import Path
import config_operate
# load
config_operate.main
my_file = Path('C:\htzqzyb2\hexin.exe')
if my_file.exists():
    child = subprocess.Popen('C:\htzqzyb2\hexin.exe',shell=True)
    child.wait()
    child = subprocess.Popen('cd C:\htzqzyb2',shell=True)
    child.wait()
    child = subprocess.Popen('git add .',shell=True)
    child.wait()
    child = subprocess.Popen('git commit -m update',shell=True)
    child.wait()
    child = subprocess.Popen('git push origin',shell=True)
else:
    child = subprocess.Popen('cd C:\ ')
    child.wait()
