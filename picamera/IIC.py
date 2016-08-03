#!/usr/bin/env python
#
# This file is part of Ivport.
# Copyright (C) 2015 Ivmech Mechatronics Ltd. <bilgi@ivmech.com>
#
# Ivport is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ivport is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#title           :IIC.py
#description     :IIC module for ivport v2 camera multiplexer
#author          :Caner Durmusoglu
#date            :20160514
#version         :0.1
#usage           :
#notes           :
#python_version  :2.7
#==============================================================================

from datetime import datetime

import smbus

iic_address = (0x70)
iic_register = (0x00)

iic_bus0 = (0x01)
iic_bus1 = (0x02)
iic_bus2 = (0x04)
iic_bus3 = (0x08)

class IIC():
    def __init__(self, twi=1, addr=iic_address, bus_enable=iic_bus0):
        self._bus = smbus.SMBus(twi)
        self._addr = addr
        config = bus_enable
        self._write(iic_register, config)

    def _write(self, register, data):
        self._bus.write_byte_data(self._addr, register, data)

    def _read(self):
        return self._bus.read_byte(self._addr)

    def read_control_register(self):
        value = self._read()
        return value

    def write_control_register(self, config):
        self._write(iic_register, config)
