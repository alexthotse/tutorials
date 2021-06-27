#!/usr/bin/env python3


import shutil
import sys


def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True


# Check for at least 2GB and 10% free
if not check_disk_usage("/", 0.1, 10):
    # Orginally a 2
    # already calling the same gigabytes functions on line 14
    #so change it
    print("ERROR: Not enough disk space")
    sys.exit(1)

print("Everything ok")
sys.exit(0)
