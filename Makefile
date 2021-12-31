ARDUINO_DIR = /usr/share/arduino

TARGET = servo.ino

BOARD_TAG = uno
ARDUINO_PORT= /dev/ttyACM1

#ARDUINO_LIBS = WIRE
#ARDUINO_LIBS += DS3231

ARDUINO_DIR = /usr/share/arduino
AVR_TOOLS_PATH = /usr/bin

include /usr/share/arduino/Arduino.mk
