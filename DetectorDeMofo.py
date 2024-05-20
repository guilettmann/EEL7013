#importa os módulos do microphyton

from machine import Pin
from time import sleep
import dht

#declara os pinos
sensorPin = Pin(23, Pin.IN, Pin.PULL_UP)
sensor = dht.DHT11(sensorPin)
led = Pin(2, Pin.OUT)

#loop de aquisição de dados

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        print('A temperatura lida é ', temp, '°C')
        umid = sensor.humidity()
        print('Umidade lida é ', umid, '%')
        
#definição de valores que proliferam mofo para aviso
        
        if temp >= 15 and temp <= 30 and umid > 65:
            led.value(1)
        else:
            led.value(0)
            
#valor de delay entre os loops
            
        sleep(1)

#se der algum erro reporta a mensagem sem parar o código
        
    except OSError as erro:
        print('Deu merda')
        
