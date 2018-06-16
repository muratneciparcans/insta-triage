#!/usr/bin/env python

import threading
import time

from functools import partial

from src.server import Server
from src.script_parser import start_script

def main():
    server = Server()

    server_thread = threading.Thread(target = server.start)
    server_thread.daemon = True
    server_thread.start()

    time.sleep(8)

    script_function = partial(start_script, server)

    # # @TODO: Do I Have to sleep?
    script_thread = threading.Thread(target = script_function)
    script_thread.daemon = True
    script_thread.start()

    # Don't stop until ctrl+c
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()