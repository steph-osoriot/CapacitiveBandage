#define BL 32
#define tx_pin 10
#define rx_pin A3
float filter_val = 0;
float filter_coeff = 0.9;
void setup() {
  // put your setup code here, to run once:
  pinMode(tx_pin, OUTPUT);
  pinMode(rx_pin, INPUT);
  Serial.flush();
  Serial.begin(115200);
}

void loop() {
  int accum = 0;
  for (int i = 0; i < BL; i++) {
    digitalWrite(tx_pin, HIGH);
    // accum += analogRead(rx_pin);
    accum += analogRead(rx_pin);
    digitalWrite(tx_pin, LOW);
    accum -= analogRead(rx_pin);
  }
  Serial.println(accum);

  // filter_val = float(accum) * (filter_coeff) + filter_val * (1- filter_coeff);
  // Serial.println(filter_val);
}
