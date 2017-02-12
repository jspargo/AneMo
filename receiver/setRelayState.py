#!/usr/bin/python

import pifacedigitalio
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='S', type=int,
                    help='The state for the relay/thermostat - 1 or 0')

arg = parser.parse_args().integers

def change_relay_state(arg):
    pfd = pifacedigitalio.PiFaceDigital()
    pfd.relays[0].value = arg
    pfd.deinit_board()
    print arg

if arg == 0:
    #Set State to off
    change_relay_state(arg)
    print "Off"
elif arg == 1:
    #Set State to off
    change_relay_state(arg)
    print "On"
else:
    #Error
    print "Error"
