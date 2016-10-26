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

First of all please enable I2C from raspi-config, [guide this link](http://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi)

And enable Camera Module from raspi-config,

### Cloning a Repository

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

First of all it is important that **init_ivport.py** should be run at every boot before starting to access camera.

```shell
cd ivport-v2
python init_ivport.py
```

And check whether ivport and camera are detected by raspberry pi or no with **vcgencmd get_camera**.

```shell
root@ivport:~/ivport-v2 $ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: 10 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- 64 -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --
```
You should get both **0x70** and **0x64** as addresses of respectively **ivport v2** and **camera module v2**.

```shell
root@ivport:~/ivport-v2 $ vcgencmd get_camera
supported=1 detected=1
```
**supported** and **detected** should be **1** before **test_ivport.py** script.

There is **test_ivport.py** script for **IVPORT DUAL V2**.

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
**TYPE** and **JUMPER** settings are configured while initialize ivport.
```python
ivport.IVPort(IVPORT_TYPE, IVPORT_JUMPER)
```
**RESOLUTION**, **FRAMERATE** and other settings can be configured.
```python
iv = ivport.IVPort(ivport.TYPE_DUAL2)
iv.camera_open(camera_v2=True, resolution=(640, 480), framerate=60)
```
Also **init_ivport.py** should be run at every boot before starting to access camera.

```shell
cd ivport-v2
python init_ivport.py
```

Tests
------

There is **test_ivport.py** script which is for testing. 
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
