// PIR motion sensor using arduino
int ledPin = 13;
int pirPin = 2;
int val = 0;
float temp;
float vout;
float vout1;
void setup()
{
  pinMode(ledPin, OUTPUT);
  pinMode(pirPin, INPUT);
}
void loop()
{
  vout=analogRead(A0);
  vout=(vout/1023)*5000;
  temp=(vout1-500)/10;
  val = digitalRead(pirPin);
  Serial.print("Current Temperature:");
  Serial.print(temp);
  if(temp>60){
    digitalWrite(7,HIGH);
  }
  else{
    digitalWrite(7,LOW);
  }
  digitalWrite(ledPin, val);

if (val ==1)
  digitalWrite(ledPin, LOW);
}