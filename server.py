#!/usr/bin/env python3
"""
Max     RPi
============
Vcc -> Pin 2
Gnd -> Pin 6
Din -> Pin 19
Cs  -> Pin 24
Clk -> Pin 23
"""
import time
import sys
import random
import traceback
import rx
import rx.operators as ops
import socket_fix

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from blist import blist
from rx.scheduler import NewThreadScheduler
from mido.sockets import PortServer

from gfx import UpLine, LeftLine, RightLine, DownLine, Point, Up, Down, Left, Right
from mapping import standard_mapping, randomize, randomize_persist


class Server(object):
    def __init__(self, host, port, note_mapper):
        serial = spi(port=0, device=0, gpio=noop(), cs_high=True)
        device = max7219(serial)
        self._virtual = viewport(device, width=8, height=8)
        self._entities = blist([])
        self._server = PortServer(host, port)
        self._mapper = note_mapper


    def run(self):
        print('Starting server {}'.format(self._server))

        self._subscription = rx.create(self._receive).pipe(
            ops.subscribe_on(NewThreadScheduler()),
            ops.map(lambda msg: self._mapper(msg)),
            ops.filter(lambda gfx: gfx is not None),
        ).subscribe(lambda gfx: self._entities.append(gfx))


        print('Start')
        while True:
            with canvas(self._virtual) as draw:
                for entity in self._entities:
                    entity.render(draw)
                    entity.update()

            self._entities[:] = [ent for ent in self._entities if not ent.can_destroy()]
            time.sleep(0.010)


    def _receive(self, observable, scheduler):
        while True:
            try:
                client = self._server.accept()
                print('Connected from {}'.format(client))
                for msg in client:
                    observable.on_next(msg)
            except Exception as exp:
                traceback.print_exc()
                print('Connection Closed')


    def _append(self, note):
        self._entities.append(note)


if __name__ == '__main__':
    server = Server(sys.argv[1], int(sys.argv[2]), standard_mapping)
    server.run()
