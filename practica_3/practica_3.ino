
/**
 * @example TCPClientSingle.ino
 * @brief The TCPClientSingle demo of library WeeESP8266. 
 * @author Wu Pengfei<pengfei.wu@itead.cc> 
 * @date 2015.02
 * 
 * @par Copyright:
 * Copyright (c) 2015 ITEAD Intelligent Systems Co., Ltd. \n\n
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of
 * the License, or (at your option) any later version. \n\n
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
#include "ESP8266.h"
#include <SoftwareSerial.h>
#include <dht.h>

dht DHT;

#define DHT11_PIN 7
#define SSID        "AP_C201"
#define PASSWORD    ""
#define HOST_NAME   "things.ubidots.com"
#define HOST_PORT   (80)

SoftwareSerial mySerial(3,2);
ESP8266 wifi(mySerial);

void setup(void)
{
    Serial.begin(9600);
    Serial.print("setup begin\r\n");
    
    Serial.print("FW Version:");
    Serial.println(wifi.getVersion().c_str());
      
    if (wifi.setOprToStationSoftAP()) {
        Serial.print("to station + softap ok\r\n");
    } else {
        Serial.print("to station + softap err\r\n");
    }
 
    if (wifi.joinAP(SSID, PASSWORD)) {
        Serial.print("Join AP success\r\n");
        Serial.print("IP:");
        Serial.println( wifi.getLocalIP().c_str());       
    } else {
        Serial.print("Join AP failure\r\n");
    }
    
    if (wifi.disableMUX()) {
        Serial.print("single ok\r\n");
    } else {
        Serial.print("single err\r\n");
    }
    
    Serial.print("setup end\r\n");
}
 
void loop(void)
{
    uint8_t buffer[128] = {0};

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
    delay(2000);

    
    if (wifi.createTCP(HOST_NAME, HOST_PORT)) {
        Serial.print("create tcp ok\r\n");
    } else {
        Serial.print("create tcp err\r\n");
    }    

    //UNA VARIABLE   
    /*char* str = (char *)malloc(300);
    strcpy(str,"POST /api/v1.6/variables/5740b5aa762542562f8b6735/values HTTP/1.1\r\nX-Auth-Token: WvqtRGXVBKHD90SffwFLoNxt2EdO5bZjSTtcynwRgV9vnAdtKoVFCSxtx2sY\r\nHost: things.ubidots.com\r\nConnection: close\r\nContent-Type: application/json\r\nContent-Length: 12\r\n\r\n{\"value\":");
    strcat(str,tmp);
    strcat(str,"}");*/
    //VARIAS VARIABLES
    char *str = (char *)malloc(300);
    sprintf(str,"POST /api/v1.6/collections/values/?token=kKWPshWijlTpR1BzDbVK9YALXi48Uf HTTP/1.1\r\nHost: things.ubidots.com\r\nContent-Type: application/json\r\nContent-Length: ");
    strcat(str,"103");
    strcat(str,"\r\n\r\n[{\"variable\":\"59581dff7625423eb19351e9\",\"value\":");
    strcat(str,tmp);
    strcat(str,"},{\"variable\":\"59581df87625423eb2e5514d\",\"value\":");
    strcat(str,hum);
    strcat(str,"}]");

    //Serial.print(str);
    

    wifi.send((const uint8_t*)str, strlen(str));
    
    uint32_t len = wifi.recv(buffer, sizeof(buffer), 10000);
    if (len > 0) {
        Serial.print("Received:[");
        for(uint32_t i = 0; i < len; i++) {
            Serial.print((char)buffer[i]);
        }
        Serial.print("]\r\n");
    }
    
    if (wifi.releaseTCP()) {
        Serial.print("release tcp ok\r\n");
    } else {
        Serial.print("release tcp err\r\n");
    }
    free(str);
    //free(buffer);
    delay(10000);
}
