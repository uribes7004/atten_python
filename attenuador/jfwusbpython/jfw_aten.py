import sys
from jfwusb import JfwUsb
import time
from threading import Thread

'''
Examples using the JfwUsb() class
'''
# find all JFW USB devices
try: jusb = JfwUsb()
except Exception as e:
    print(e)
    sys.exit(1)

# list devices
print("List of USB devices")
print(jusb.GetList())
#**************************************************
attenuator = ""
While attenuator != "E"
    attenuattor= input("how many dbm  or " + "hit e to exit")
    attenuattor attenuattor*100
    if attenuattor > 6500:
        print("the value must not be greater than 65")
    print("Set Attenuator (device #1) to " + attenuattor + "dB\n   (No Response Expected)")
    try: jusb.Set(1,attenuattor )  
    except Exception as e: print(e)
    time.sleep(3
    # divide read value by 100 for dB
    print("\nRead Attenuator (device #1)")
    try: print("   Atten (Device #1) = {}dB".format(jusb.Read(1)/100))
    except Exception as e: print(e)
#**************************************************
