import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)


    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()


    def set_number(self, number):
        if (0 <= number <= 255):
            binary = [int(el) for el in bin(number)[2:].zfill(8)]
            GPIO.output(self.gpio_pin, binary)
        else:
            GPIO.output(self.gpio_pin, 0)


    def 


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
       
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()