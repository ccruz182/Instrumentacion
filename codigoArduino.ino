unsigned long primer_lectura = 0;


void setup() {
  Serial.begin(9600); // Inicio del Bluetooth
  attachInterrupt(0, interrupcion, RISING);
}

void loop() {
  /**/
}
  

void interrupcion() {
 // Serial.println("Paso algo");
  unsigned long segunda_lectura = millis();
  unsigned long diferencia = segunda_lectura - primer_lectura;
  float freq = 1.0 / ((float)diferencia / 1000.0);
  float bpm = freq * 60;  
  Serial.println((int)bpm);
  Serial.flush();
  primer_lectura = segunda_lectura;
}
