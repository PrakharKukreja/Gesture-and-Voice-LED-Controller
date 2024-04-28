import pyfirmata

comport='COM7'

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:7:o')
led_2=board.get_pin('d:6:o')
led_3=board.get_pin('d:5:o')

def led(val):
    if val==1:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
    elif val==0:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)

