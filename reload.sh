#!/bin/bash

killall ./start.sh
cd ~/Desktop/workplace/scholar/PROGRAMACAO/arduino/servo_GUI/servo
echo '37489101' | sudo -S make upload
cd ~/Desktop/workplace/scholar/PROGRAMACAO/arduino/servo_GUI
./start.sh
