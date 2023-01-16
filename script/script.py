import bk8500
import serial
import contextlib
import io

address = 0
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM16'
ser.parity = 'N'
ser.timeout = 2
print(ser)
ser.open()

def mode_change(value):
    global address
    mode = 0
    io_string = io.StringIO()
    if (value == 1):
        mode = "CC"
    elif (value == 2):
        mode = "CV"
    elif (value == 3):
        mode = "CW"
    elif (value == 4):
        mode = "CR"
    with contextlib.redirect_stdout(io_string):
        bk8500.set_mode(ser, address, mode)

#set remote
bk8500.set_remote(ser,address,True)

#enable input
# bk8500.enable_input(ser,address,True)

# # bk8500.set_current(ser,address,10)

# bk8500.set_resistance(ser,address,200)

# bk8500.set_current(ser,address,10)

# bk8500.set_voltage(ser,address,10)

# bk8500.get_resistance(ser,address)

# bk8500.get_current(ser,address)

#set control to local (panel) instead of remote

# bk8500.set_remote(ser,address,False)

# bk8500.get_product_info(ser,address)
# bk8500.get_instrument_readings(ser,address)

# mode 1 = "CC"
# mode 2 = "CV"
# mode 3 = "CW"
# mode 4 = "CR"

mode = 1

mode_change(mode)
bk8500.set_current(ser,address,10)

bk8500.enable_input(ser,address,True)
bk8500.set_remote(ser,address,False)