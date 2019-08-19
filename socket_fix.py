import select
import socket

from mido.sockets import SocketPort, format_address, _is_readable
from mido.ports import BaseIOPort 
from mido.parser import Parser
from mido.py2 import PY2


"""
This is a patch that fixes the delay
when receiving notes from socket
"""
def _init_patch(self, host, portno, conn=None):
    BaseIOPort.__init__(self, name=format_address(host, portno))
    self.closed = False
    self._parser = Parser()
    self._messages = self._parser.messages

    if conn is None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setblocking(True)
        self._socket.connect((host, portno))
    else:
        self._socket = conn

    if PY2:
        kwargs = {'bufsize': 0}
    else:
        kwargs = {'buffering': 3}

    self._rfile = self._socket.makefile('rb', **kwargs)
    self._wfile = self._socket.makefile('wb', **kwargs)


def _receive_patch(self, block=True):
    while _is_readable(self._socket):
        try:
            byte = self._rfile.read(3)
        except socket.error as err:
            raise IOError(err.args[1])
        if byte == '':
            # The other end has disconnected.
            self.close()
            break
        else:
            self._parser.feed_byte(byte[0])
            self._parser.feed_byte(byte[1])
            self._parser.feed_byte(byte[2])

SocketPort.__init__ = _init_patch
SocketPort._receive = _receive_patch
