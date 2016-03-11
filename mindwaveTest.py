import mindwave, time

headset = mindwave.Headset('/dev/ttyUSB0', 'EA0D')
time.sleep(2)

headset.connect()
print("Connecting...")

while headset.status != 'connected':
    time.sleep(0.5)
    if headset.status == 'standby':
        headset.connect()
        print("Retrying connect...")
    else:
    	print("headset status: %s" % headset.status)
print("Connected.")

while True:
    print("Attention: %s, Meditation: %s" % (headset.attention, headset.meditation))
    time.sleep(0.5)
