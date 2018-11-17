void setup() {
  /* Pines de escritura (eleccion de sensor) */
  pinMode(48, OUTPUT); // LSB
  pinMode(50, OUTPUT);
  pinMode(52, OUTPUT); // MSB

  /* Pines de entrada */
  pinMode(22, INPUT); // LSB
  pinMode(24, INPUT);
  pinMode(26, INPUT);
  pinMode(28, INPUT);
  pinMode(30, INPUT);
  pinMode(32, INPUT);
  pinMode(34, INPUT);
  pinMode(36, INPUT); // MSB

  Serial.begin(9600); // Inicio del Bluetooth
}

void loop() {
  int valor1, valor2;
  /* Sensor #1 */
  seleccionSensor(LOW, LOW, LOW); // Seleccion del sensor
  delay(500); // Se espera tiempo
  valor1 = lecturaBits(8); // Lectura del puerto
  

  /* Sensor #2 */  
  seleccionSensor(HIGH, LOW, LOW); // Seleccion del sensor
  delay(500); // Se espera tiempo
  valor2 = lecturaBits(8); // Lectura del puerto  
  
  /* Envio BT */
  //String valores = valor1 + "&" + valor2;
  //Serial.println(valores); // Se envía dato
  Serial.print(valor1);
  Serial.print("&");
  Serial.println(valor2);
  Serial.flush(); // Se espera a que se envíe todo para poder continuar
}

int lecturaBits(int numBits) {
  int i = 0;
  int base;
  int valor = 0;
  for (i = 0, base = 22; i < numBits; i++, base += 2) {
    if (digitalRead(base) == HIGH) {         
      valor +=  (1 << i);
    }
  }

  return valor;
}

void seleccionSensor(int a, int b, int c) {  
  digitalWrite(48, a);
  digitalWrite(50, b);
  digitalWrite(52, c);
}
