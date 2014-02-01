__author__ = 'thor'

import os


def project_root():
    root = __file__
    if os.path.islink (root):
        root = os.path.realpath(root)
    return os.path.dirname(os.path.abspath(root))

