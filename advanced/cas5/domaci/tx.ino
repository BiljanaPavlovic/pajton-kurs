int tx1 = 2;
int tx2 = 4;

void setup() {
  pinMode(tx1,OUTPUT);
  pinMode(tx2,OUTPUT);
  delay(1000);
}

void loop() {
   digitalWrite(tx1,HIGH);
   delay(500);
   digitalWrite(tx2,HIGH);
   delay(500);
   digitalWrite(tx1,LOW);
   delay(250);
   digitalWrite(tx2,LOW);
   delay(500);
   
}
