from python_tsl2591 import tsl2591
import time
import pandas as pd
from datetime import datetime


def main():
    tsl = tsl2591()  # initialize

    sample_interval = 5 # in second
    batch_duration = 2 # in hour
    second_in_hour = 3600

    v_time = []
    v_lux = []
    v_full = []
    v_ir = []

    count = 0
    batch = 0
    while True:
        result = tsl.get_current()
        if count == 0:
            now = datetime.now()
            start = now.strftime("%Y-%m-%d_%H-%M")
        count += 1
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        v_time.append(dt_string)
        v_lux.append(result['lux'])
        v_full.append(result['full'])
        v_ir.append(result['ir'])
        print(result)
        time.sleep(sample_interval)

    if count >= batch_duration*second_in_hour//sample_interval:
        print('Save one batch...')
        now = datetime.now()
        end = now.strftime("%Y-%M-%d_%H-%M")
        batch += 1
        df = pd.DataFrame({
            'Time': v_time,
            'Lux': v_lux,
            'Full': v_full,
            'IR': v_ir
        })
        df.to_csv('Batch_'+str(batch)+'_'+start + ' to ' + end + '.csv', index=False)
        count = 0

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass