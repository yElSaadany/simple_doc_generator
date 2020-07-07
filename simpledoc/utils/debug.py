"""Tiny helper module for quick debugging."""
import os
import inspect


def debug(msg):
    if os.environ.get("DEBUG", False):
        calling_function = inspect.getouterframes(inspect.currentframe(), 2)
        calling_function = calling_function[1].function
        print("DEBUG:%s: %s" % (calling_function, msg))
