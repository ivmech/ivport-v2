IVPORT V2
--------------

IVPORT V2 is compatible with Raspberry Pi Camera Module V2 with 8MP SONY IMX219 Sensor

IVPORT and IVPORT V2 which are the first Raspberry Pi (also Raspberry Pi A,A+,B+ and Raspberry Pi 2,3 fully compatible) Camera Module multiplexer is designed to make possible connecting more than one camera module to single CSI camera port on Raspberry Pi. Multiplexing can be controlled by 3 pins for 4 camera modules, 5 pins for 8 camera modules and 9 pins for **maximum up to 16 camera modules** with using GPIO.

IVPort has already been preferred by  ESA, MIT Lab, Spacetrex Lab, well known company research centers and numerous different universities.

Getting Started
-----------------------------------

###Order

IVPORT V2 is available at [HERE](http://www.ivmech.com/magaza/ivport-v2-p-107).

### Installation

```shell
	git clone https://github.com/ivmech/ivport-v2.git
```

### Dependency Installation

```shell
	sudo apt-get install python-smbus
```
picamera module was forked from https://github.com/waveform80/picamera and small edits for camera v2 and ivport support. It may be needed to uninstall preinstalled picamera module on device.

```shell
	sudo apt-get remove python-picamera
	sudo pip uninstall picamera
```

###Usage

There is test_ivport.py script.
```python
import ivport
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
```
TYPE and JUMPER settings are configured while init ivport.
```python
iv = ivport.IVPort(IVPORT_TYPE, IVPORT_JUMPER)
```

There is test_ivport.py script.
```shell
cd ivport-v2
python test_ivport.py
```

Wiki
------

#### See wiki pages from  [here](https://github.com/ivmech/ivport/wiki).

Video
-------

IVPort can be used for stereo vision with stereo camera.

### [Youtube video](https://www.youtube.com/watch?v=w4JZN7Y0d2o) of stereo recording with 2 camera modules
[![IVPort Stereo Recording](https://raw.githubusercontent.com/ivmech/ivport/master/images/ivport_stereo_01.jpg)](https://www.youtube.com/watch?v=w4JZN7Y0d2o)

### IVPort was [@hackaday](http://hackaday.com/2014/12/19/multiplexing-pi-cameras/).
