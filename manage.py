#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlineexam.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlineTest.settings")
>>>>>>> master

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
