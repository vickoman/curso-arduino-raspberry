#include <dht.h>

dht DHT;

#define DHT11_PIN 7

void setup(void)
{
    Serial.begin(9600);
    Serial.print("setup begin\r\n");
}
 
void loop(void)
{
    int chk = DHT.read11(DHT11_PIN);
    char tmp[3],hum[3];
    int t = DHT.temperature;
    int h = DHT.humidity;
    sprintf(tmp,"%d",t);
    sprintf(hum,"%d",h);
    Serial.print("Temp:");
    Serial.println(tmp);
    Serial.print("Hum:");
    Serial.println(hum);    
    delay(10000);
}

