#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Kill Huawei modems by switching to wrong mode.
# Tested on Huawei E1550, E1750, E171, E173
# N.B. Recovery via Qualcomm tools - QPST, QXDM


__author__ = '@090h'
__license__ = 'GPL'


from sys import argv
from serial import Serial


class ModemKiller(object):

    def __init__(self, port, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=5, xonoff=False, rtscts=False, dsrdtr=False):
        self.port = Serial(port, baudrate, bytesize, parity, stopbits, timeout, xonoff, rtscts, dsrdtr)
        self._mode = 0

    def info(self):
        self.port.write('ATI\r')
        return self.port.read(4096)


    def set_mode(self, value):
        self.port.write('AT^U2DIAG=%i\r' % value)
        self._mode = value

    def get_mode(self):
        self.port.write('AT^U2DIAG?\r')
        try:
            self._mode = int(self.port.readline())
        except ValueError:
            self._mode = 0
        return self._mode

    mode = property(get_mode, set_mode)

    def kill(self, max=1000):
        print('Modem info:\n%s' % self.info())
        print('Modem mode: %i' % self.mode)

        # for i in xrange(0, max):
        #     print('Setting mode to: %i' % i)
        #     self.mode = i

if __name__ == '__main__':
    if len(argv) == 1:
        print('Usage:\n\t./killmodem.py <modem_port>')
    else:
        killer = ModemKiller(argv[1])
        killer.kill()