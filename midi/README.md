# installing

```
pip3 install rtmidi-python
sudo apt install fluidsynth
```

# running
Start the software synthesizer:
```
fluidsynth -a alsa -v -s /usr/share/sounds/sf2/FluidR3_GM.sf2
```

# send test data
```
ros2 topic pub alarm std_msgs/Int32 "data: 1"  4
```
