import r2r_dac as r2r
import signal_generator as sg

amplitude = 2.5
signal_frequency = 10
sampling_frequency = 1000

dt = 1 / sampling_frequency
t = 0.0

if __name__ == '__main__':
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.15, True)
    try:

        while True:
            norm_amp = sg.get_sin_wave_amplitude(signal_frequency, t)
            dac.set_voltage(norm_amp * amplitude)
            sg.wait_for_sampling_period(sampling_frequency)
            t += dt


    finally:
        dac.deinit()