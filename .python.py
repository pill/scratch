"""
saves python history between sessions
save file in: 
~/.python.py

update ~/.bash_profile:
PYTHONSTARTUP=$HOME/.python.py
export PYTHONSTARTUP

run this the first time:
readline.write_history_file(history_file)
"""

import os
import readline
import atexit

history_file = os.path.expanduser('~/.python_history')
readline.read_history_file(history_file)

atexit.register(readline.write_history_file, history_file)
