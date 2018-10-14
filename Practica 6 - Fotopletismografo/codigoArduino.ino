unsigned long primer_lectura = 0;


void setup() {
  Serial.begin(9600); // Inicio del Bluetooth
  attachInterrupt(0, interrupcion, RISING); // Se notifica la interrupción
}

void loop() {
  /* No es necesario código dentro del loop */
}
  

void interrupcion() {
  unsigned long segunda_lectura = millis(); // Segundo pulso detectado
  unsigned long diferencia = segunda_lectura - primer_lectura; // Diferencia para sacar el periodo de la señal
  
  float freq = 1.0 / ((float)diferencia / 1000.0); // Cálculo de la frecuencia
  float bpm = freq * 60; // Cálculo de 'beats per minute'

  Serial.println((int)bpm); // Se envía dato
  Serial.flush(); // Se espera a que se envíe todo para poder continuar
  
  primer_lectura = segunda_lectura; // La segunda lectura pasa a ser la primera
}
