#!/usr/bin/env python

from __future__ import division

from src.application import Application


def main():

    # Let's see, maybe we want this
    # conf = Configuration("./mapper.txt")

    print('Standby mode...\nPress any key to record')

    app = Application(False)
    while True:
        app.listen_key()


if __name__ == '__main__':
    main()