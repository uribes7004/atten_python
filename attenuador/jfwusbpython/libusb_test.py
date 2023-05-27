import usb.backend.libusb1

backend = usb.backend.libusb1.get_backend(find_library=lambda x: "libusb-1.0.dll")
dev = usb.core.find(backend=backend, find_all=True)

for d in dev:
   if (d.idVendor == 0x04d8):
       print(str(d._get_full_descriptor_str()) + "\n")
       print(str(d.get_active_configuration()) + "\n")

   