#!/usr/bin/env python

import os
import ivport
import time

def picam_sequence():
    FRAMES = 90
    CAM = 0
    def sequence_outputs(iv):
        frame = 0
        while frame < FRAMES:
            camera = (frame%2)+1
            time.sleep(0.07)   # SD Card Bandwidth Correction Delay
            iv.camera_change(camera)
            time.sleep(0.07)   # SD Card Bandwidth Correction Delay
            yield 'sequence_%02d.jpg' % frame
            frame += 1

    iv = ivport.IVPort(ivport.TYPE_DUAL2)
    iv.camera_open(camera_v2=True)
    iv.picam.resolution = (640, 480)
    iv.picam.framerate = 30
    #time.sleep(1)
    iv.camera_sequence(outputs=sequence_outputs(iv), use_video_port=True)
    iv.close()

def picam_capture():
    iv = ivport.IVPort(ivport.TYPE_DUAL2)
    iv.camera_open()
    iv.camera_change(1)
    iv.camera_capture("picam", use_video_port=False)
    iv.camera_change(2)
    iv.camera_capture("picam", use_video_port=False)
    iv.close()

def still_capture():
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

# main capture examples
# all of them are functional
def main():
    still_capture()
    picam_capture()
    #picam_sequence()

if __name__ == "__main__":
    main()
