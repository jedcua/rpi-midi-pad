#!/usr/bin/env python3

import sys

from mido import open_input, set_backend
from mido.sockets import connect


class Client(object):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        print('Connecting to server {} : {}'.format(host, port))
        self._server = connect(host, port)

    def run(self):
        print('Start')
        with open_input('Mido Port', virtual=True) as inport:
            for msg in inport:
                if msg.type == 'note_on' and msg.bytes()[2] > 0:
                    self._server.send(msg)


if __name__ == '__main__':
    set_backend('mido.backend.rtmidi')
    client = Client(sys.argv[1], int(sys.argv[2]))
    client.run()
