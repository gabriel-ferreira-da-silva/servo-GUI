                                                                                                                                                                    #include <Servo.h>

#include <Servo.h>

Servo myservo; 

 
int pos=1;  
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
  myservo.attach(8);  
  Serial.begin(9600);
  Serial.setTimeout(3);
}

String a;
void loop() {


if(Serial.available()){
    newpos=Serial.parseInt();
    if(newpos==0)newpos=pos;
   
    if(pos < newpos){
      for (; pos <= newpos; pos++) { 
        myservo.write(pos);          
        swrite(pos);
        delay(delaytime);
      }
      delay(10);
      newpos=pos;
    }
  
    if(pos > newpos){
      for (; pos >= newpos; pos--) {
        myservo.write(pos);
        swrite(pos);
        delay(delaytime);
      }  
      delay(10);
      newpos=pos;
    }
  }  
}
