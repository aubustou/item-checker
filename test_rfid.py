import mercury
import time


time.sleep(2)
reader = mercury.Reader("tmr:///dev/ttyS0")


reader.set_region("EU3")
reader.set_read_plan([1], "GEN2")


while True:
    data = reader.read()
    if data:
        print(data)
    time.sleep(1)
