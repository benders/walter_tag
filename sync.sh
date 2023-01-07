#!/bin/sh

set -ex

rsync --exclude=.\* --exclude=.\*/ --delete --delete-excluded -avC $(pwd)/ pi@ted-e.local:/media/CIRCUITPY/
