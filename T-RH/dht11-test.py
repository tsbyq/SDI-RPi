# _____ _____ _____ __ __ _____ _____
# |     |   __|     |  |  |     |     |
# |  |  |__   |  |  |_   _|  |  |  |  |
# |_____|_____|_____| |_| |_____|_____|
#
# Use Raspberry Pi to get temperature/humidity from DHT11 sensor
#
import time
import dht11
import RPi.GPIO as GPIO

import pandas as pd
from datetime import datetime


# define GPIO 14 as DHT11 data pin
Temp_sensor = 14


def main():
    # Main program block
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    # Initialise display
    # lcd_init()
    instance = dht11.DHT11(pin=Temp_sensor)

    v_time = []
    v_T = []
    v_RH = []
    count = 0
    batch = 0
    while True:
        # get DHT11 sensor value
        result = instance.read()
        if result.temperature != 0 and result.humidity != 0:
            if count == 0:
                now = datetime.now()
                start = now.strftime("%Y-%m-%d_%H-%M")
            count += 1
            # Get current time
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            v_time.append(dt_string)
            v_T.append(result.temperature)
            v_RH.append(result.humidity)
            print"Timestamp =", dt_string, ", Temperature = ", result.temperature, "C", " Humidity = ", result.humidity, "%"
            time.sleep(10)

        # Save to file every 360 entry
        if count == 360:
            print 'Save one batch...'
            now = datetime.now()
            end = now.strftime("%Y-%M-%d_%H-%M")
            batch += 1
            df = pd.DataFrame({
                'Time': v_time,
                'Temperature': v_T,
                'Humidity': v_RH
            })
            df.to_csv('Batch_'+str(batch)+'_'+start + ' to ' + end + '.csv', index=False)
            count = 0


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
#  finally:
#    lcd_byte(0x01, LCD_CMD)
