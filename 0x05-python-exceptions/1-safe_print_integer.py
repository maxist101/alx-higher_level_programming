#!/usr/bin/python3
def safe_print_integer(value):
    """Print an int with {:d}.format()"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
