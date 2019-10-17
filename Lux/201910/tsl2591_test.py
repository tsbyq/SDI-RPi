from python_tsl2591 import tsl2591
import time


def main():
    tsl = tsl2591()  # initialize

    v_time = []
    v_lux = []
    v_full = []
    v_ir = []

    count = 0
    batch = 0
    while True:
        result = tsl.get_current()\
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
        tiem.sleep(3)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass