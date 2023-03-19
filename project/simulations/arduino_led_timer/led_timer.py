'''
====== Legal notices

Copyright (C) 2013 - 2021 GEATEC engineering

This program is free software.
You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicense.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY, without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the QQuickLicense for details.

The QQuickLicense can be accessed at: http://www.qquick.org/license.html

__________________________________________________________________________


 THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!

__________________________________________________________________________

It is meant for training purposes only.

Removing this header ends your license.
'''

import simpylc as sp

class LedTimer (sp.Module):
    def __init__ (self):
        sp.Module.__init__ (self)
        
        self.rampTimer = sp.Timer ()
        self.pulse = sp.Oneshot ()
        self.direction = sp.Marker ()
        self.blinkTime = sp.Register ()
        self.blinkTimer = sp.Timer ()
        self.led = sp.Marker ()
        self.runner = sp.Runner ()
            
    def sweep (self):
        self.rampTimer.reset (self.rampTimer > 9)
        self.pulse.trigger (self.rampTimer <  0.1)
        self.direction.mark (not self.direction, self.pulse)
        self.blinkTime.set (3 - self.rampTimer / 3, self.direction, self.rampTimer / 3)
        self.blinkTimer.reset (self.blinkTimer > self.blinkTime)
        self.led.mark (self.blinkTimer < 0.05)
