import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(path)

from py_scripts.SQL import atualizar

atualizar()