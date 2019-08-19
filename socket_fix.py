import select
from mido.sockets import SocketPort

"""
This is a patch that fixes the delay
when receiving notes from socket
"""
def _is_readable(socket):
    """Return True if there is data to be read on the socket."""

    timeout = 0
    (rlist, wlist, elist) = select.select(
        [socket.fileno()], [], [], timeout)

    return bool(rlist)

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

SocketPort._receive = _receive_patch
