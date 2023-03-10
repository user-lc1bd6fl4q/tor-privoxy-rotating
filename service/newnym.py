#!/usr/bin/env python 

import stem
from stem import Signal
from stem.control import Controller

with Controller.from_port(port = 9051) as controller:
    controller.authenticate(password='') 
    controller.signal(Signal.NEWNYM)

