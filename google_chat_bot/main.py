#!/usr/bin/env python

from __future__ import division

from src.script_parser import start_script
from src.server import server

def main():
    server.start()
    start_script(server)

if __name__ == '__main__':
    main()