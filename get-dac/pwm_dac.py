import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_bits, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

        self.pwm = GPIO.PWM(self.gpio_bits, self.pwm_frequency)
        self.pwm.start(0.0)


    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()


    def set_voltage(self, voltage):
        number = int(voltage / self.dynamic_range * 100)
        self.pwm.ChangeDutyCycle(number)


if __name__ == "__main__":
    dac = PWM_DAC(12, 2000, 3.15, True)
    try:


        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()