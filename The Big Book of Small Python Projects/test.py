import time

ee = time.localtime()

print(ee.tm_hour % 12)