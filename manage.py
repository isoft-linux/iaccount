#!/usr/bin/env python2
import os
import sys

if __name__ == "__main__":
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iaccount.settings")

    for i in ("apps", "modules"):
        path_dir = os.path.join(PROJECT_ROOT, i)
        if os.path.isdir(path_dir):
            sys.path.insert(0, path_dir)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
