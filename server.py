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
import rx
import rx.operators as ops

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from blist import blist
from rx.scheduler import NewThreadScheduler
from mido.sockets import PortServer

from gfx import Point, Up, Down, Left, Right


def port_server(host, port):
    print('Creating server {} : {}'.format(host, port))
    server = PortServer(host, port)

    def receive(observable, scheduler):
        while True:
            try:
                client = server.accept()
                print('Connected from {}'.format(client))
                for msg in client:
                    observable.on_next(msg.note)
            except Exception as exp:
                print('Connection Closed')
    return receive


def randomize(_):
    dir = random.choice(['up', 'down', 'left', 'right'])
    rand_pos = random.randint(0,7)
    if dir == 'up':
        return Up(Point(rand_pos, 7))
    elif dir == 'down':
        return Down(Point(rand_pos, 0))
    elif dir == 'left':
        return Left(Point(7, rand_pos))
    elif dir == 'right':
        return Right(Point(0, rand_pos))
    elif dir == 'downline':
        x_pos = random.randint(0,5)
        return DownLine(x_pos, x_pos + 2, 0)
    elif dir == 'upline':
        x_pos = random.randint(0,5)
        return UpLine(x_pos, x_pos + 2, 7)


class Server(object):
    def __init__(self, host, port):
        serial = spi(port=0, device=0, gpio=noop())
        device = max7219(serial)
        self._virtual = viewport(device, width=8, height=8)
        self._entities = blist([])
        self._host = host
        self._port = port


    def run(self):
        self._subscription = rx.create(port_server(self._host, self._port)).pipe(
            ops.subscribe_on(NewThreadScheduler()),
            ops.filter(lambda note: note is not None),
            ops.map(lambda note: randomize(None))
        ).subscribe(lambda note: self._entities.append(note))


        # Main loop
        print('Start')
        while True:
            with canvas(self._virtual) as draw:
                for entity in self._entities:
                    entity.render(draw)
                    entity.update()

            self._entities[:] = [ent for ent in self._entities if not ent.can_destroy()]
            time.sleep(0.010)


    def _append(self, note):
        self._entities.append(note)


if __name__ == '__main__':
    server = Server(sys.argv[1], int(sys.argv[2]))
    server.run()
