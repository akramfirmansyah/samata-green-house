// Import Library
#include <OneWire.h>
#include <DallasTemperature.h>
#include <EEPROM.h>
#include "GravityTDS.h"
#include "DHT.h"

// Define Constant
#define TDSPIN A1
#define PHPIN A2
#define ONE_WIRE_BUS 5
#define DHTPIN 6
#define DHTTYPE DHT22
#define LIQUIDDETECTORPIN 8

// Define variable
int waterTemperature;
int humidity;
int heatIndex;
int liquidDetector;
float tds;
float ph;
float airTemperature;
String dataSensor;

// Initialization library
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
GravityTDS gravityTds;
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);

  sensors.begin();

  gravityTds.setPin(TDSPIN);
  gravityTds.setAref(5.0);
  gravityTds.setAdcRange(1024);
  gravityTds.begin();

  dht.begin();
}

void loop() {
  ph = getPh();
  waterTemperature = getWaterTemperature();
  tds = getTDS(waterTemperature);
  airTemperature = dht.readTemperature(); // https://github.com/adafruit/DHT-sensor-library/blob/master/examples/DHTtester/DHTtester.ino
  humidity = dht.readHumidity();
  heatIndex = dht.computeHeatIndex(airTemperature, humidity, false);
  liquidDetector = getLiquidDetector(LIQUIDDETECTORPIN);
  
  dataSensor = String(ph)+"@"+String(tds)+"@"+String(waterTemperature)+"@"+String(airTemperature)+"@"+String(humidity)+"@"+String(heatIndex)+"@"+String(liquidDetector);

  Serial.println(dataSensor);

  delay(1000);
}

float getPh() {
  int sensorValue = analogRead(PHPIN);
  float phValue = sensorValue * 1;
  return phValue;
}

// https://randomnerdtutorials.com/guide-for-ds18b20-temperature-sensor-with-arduino/
int getWaterTemperature() {
  sensors.requestTemperatures();

  // int sensorValue = sensors.getTempCByIndex(0);
  int sensorValue = 25; // Set default value to 25 because sensor having trouble
  return sensorValue;
}

// https://github.com/DFRobot/GravityTDS/blob/master/GravityTDSExample/GravityTDSExample.ino
float getTDS(float waterTemperature) {
  gravityTds.setTemperature(waterTemperature);
  gravityTds.update();

  float tdsValue = gravityTds.getTdsValue();

  return tdsValue;
}

int getLiquidDetector(int pin) {
  int analogValue = digitalRead(pin);

  return analogValue;
}