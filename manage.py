#!/usr/bin/env python
print( "hellooo" )
print( "asdfasdfasdfasdf" )
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yacatecuhtli.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
