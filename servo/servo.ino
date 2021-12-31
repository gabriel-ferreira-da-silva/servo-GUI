                                                                                                                                                                    #include <Servo.h>


/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards
 
int pos=1;    // variable to store the servo position
int newpos=1;
int delaytime=15;

void swrite(int pos){
    char c[4]={'0','0','0','\n',};
    int j=2;
    while(pos){
      int i = pos%10;
      pos-=i;
      pos/=10;
      i+=48;
      c[j]=i;
      j-=1;
   }
   Serial.write(c);
}

void setup() {
  //pinMode(8,OUTPUT);
  myservo.attach(8);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
  //while (!Serial);
  Serial.setTimeout(3);
}

int i=1;
void loop() {

while(i){
    if(Serial.available()){
	byte o=Serial.read();
	if(char(o)=='o'){
             i=0;
	     Serial.write("comecei");
        }
    }
}

if(Serial.available()){
    
    newpos=Serial.parseInt();
    if(newpos==0)newpos=pos;
   
    if(pos < newpos){
      for (; pos <= newpos; pos++) { // goes from 0 degrees to 180 degrees
        myservo.write(pos);              // tell servo to go to position in variable 'pos'
        swrite(pos);
        delay(delaytime);
      }
      delay(10);
      newpos=pos;
    }
  
    if(pos > newpos){
      for (; pos >= newpos; pos--) { // goes from 180 degrees to 0 degrees
        myservo.write(pos);
        swrite(pos);
        delay(delaytime);
      }  
      delay(10);
      newpos=pos;
    }
  }  
}
