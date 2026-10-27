#!/usr/bin/env python
"""Herramienta de administración del proyecto Huellas Sanas."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "huellas_sanas.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
