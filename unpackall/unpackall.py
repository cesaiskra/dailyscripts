#!/usr/bin/evn python

# 'unpackall' looks for archives in given path and extracts them.
# Copyright (C) 2010, Tomas Varaneckas

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import sys
import os.path

class HandlerFactory(object):
    """Formats should be handled in a way which would easilly allow 
adding new archive types. This class tries to solve it."""

    def __init__(self):
        self.handlers = {
            'unrar' : 'unrar x %s',
            'unzip' : 'unzip %s'
        }
        self.handler_map = {
            'rar' : 'unrar',
            'zip' : 'unzip'
        }

    @classmethod
    def get_handler(cls, file_name):
        pass

class UnpackAll(object):
    
    def main(self, argv):
        self.argv = argv
        print self.argv

if __name__ == '__main__':
    program = UnpackAll()
    program.main(sys.argv)
