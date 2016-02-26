# ThermoMechanical_Arduino
#cameraMacro.py#

This macro should be able to trigger focusing, zooming and photo taking
in the IR camera. Ideally, the listen.py macro will be waiting for a
certain value coming from the Arduino, then it will call this macro.

#mergingMacro.py#

Once all the photos have been taken they can be merged into a panorama.
This can be done offline without much trouble, but it'd be nice
to have a complete, automated process.
