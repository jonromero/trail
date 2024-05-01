#!/bin/bash

# Jot down your trail of thoughts
# Jon Vlachogiannis (darksun4@gmail.com)
# 4/30/2024

import sys
import os
from datetime import datetime

# Determine the filename based on the TRAIL_USER environment variable
filename = f".{os.getenv('TRAIL_USER', 'default')}_trails"

# Get the current date and time
now = datetime.now().strftime("%d %B %Y %T")

# Check command line arguments
if len(sys.argv) == 1:
    print(f"Usage: {sys.argv[0]} [text] [-n num_of_lines]")
    sys.exit(0)

if len(sys.argv) == 3 and sys.argv[1] == "-n":
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_of_lines = int(sys.argv[2])
            for line in lines[-num_of_lines:]:
                print(line, end='')  # end='' to avoid double new lines
        sys.exit(0)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)

# Append the date and provided text to the trails file
with open(filename, 'a') as file:
    file.write(f"{now} -> {' '.join(sys.argv[1:])}\n")
