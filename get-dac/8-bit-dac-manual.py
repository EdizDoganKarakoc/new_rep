import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setup(dac_bits, GPIO.OUT)




dynamic_range = 3.144

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Voltage is out of range DAC (0.00 - {dynamic_range:.f} V")
        print("setting to 0.00 V")
        return 0

    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    bins = [int(bit) for bit in bin(number)[2:].zfill(8)]
    GPIO.output(dac_bits, bins)







try:
    while True:
        try:
            voltage = float(input("Enter Voltage in V: "))
            number_to_dac(voltage_to_number(voltage))


        except ValueError:
            print("You've written a non number value. Please try again\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()
