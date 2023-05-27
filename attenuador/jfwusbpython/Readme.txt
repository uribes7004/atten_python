Requires PyUSB: https://github.com/pyusb/pyusb
Requires libusb: https://libusb.info/
   Python x64: Copy libusb-1.x.x/VS2019/MS64/dll/libusb-1.0.dll to Windows\System32
   Python x86: Copy libusb-1.x.x/VS2019/MS32/dll/libusb-1.0.dll to Windows\SysWOW64
   
Example scripts are meant to show the use of the API, and are not intended to be executed unmodified.

libusb_test.py: Dumps USB descriptor information from JFW USB devices. (Troubleshooting libusb)
