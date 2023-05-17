#!/usr/bin/env python

import os
import ivport
import time

def raspistill_capture():
    # raspistill capture
    def capture(camera):
        "This system command for raspistill capture"
        cmd = "raspistill -t 10 -o still_CAM%d.jpg" % camera
        os.system(cmd)

    iv = ivport.IVPort(ivport.TYPE_DUAL2)
    iv.camera_change(1)
    capture(1)
    iv.camera_change(2)
    capture(2)
    iv.close()

def libcamera_still_capture():
    # raspistill capture
    def capture(camera):
        "This system command for raspistill capture"
        cmd = "libcamera_still -t 10 -o still_CAM%d.jpg" % camera
        os.system(cmd)

    iv = ivport.IVPort(ivport.TYPE_DUAL2)
    iv.camera_change(1)
    capture(1)
    iv.camera_change(2)
    capture(2)
    iv.close()

# main capture examples
# all of them are functional
def main():
    #raspistill_capture()       # legacy camera
    libcamera_still_capture()   # after Raspberry OS Bullseye
    #picam_capture()
    #picam_sequence()

if __name__ == "__main__":
    main()
