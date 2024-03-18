import numpy as np
import matplotlib.pyplot as plt

def square_wave(N):
    '''This function will return the square wave.'''
    n = np.arange(N)
    y = np.ones(N)
    y[N//2:] = -1
    return y

def sawtooth_wave(N):
    '''This function will return the sawtooth wave'''
    n = np.arange(N)
    y = n % N
    return y

def modulated_sine_wave(N):
    '''This function will return the modulated sine wave.'''
    n = np.arange(N)
    y = np.sin(np.pi * n / N) * np.sin(20 * np.pi * n / N)
    return y

def discrete_fourier_transform(signal):
    '''This function will return the discrete fourier transform.'''
    N = len(signal)
    k = np.arange(N)
    n = k.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    coefficients = np.sum(signal * e, axis=1) / N
    return np.abs(coefficients)

def plot_amplitude_spectrum(signal, title, axis):
    '''This function will return the plot amplitude spectrum.'''
    N = len(signal)
    frequencies = np.fft.fftfreq(N, 1/N)
    coefficients = discrete_fourier_transform(signal)

    axis.stem(frequencies, coefficients, use_line_collection=True)
    axis.set_title(title)
    axis.set_xlabel('Frequency')
    axis.set_ylabel('Amplitude')

# Define N
N = 1000

fig,axes = plt.subplots(1,3, figsize = (15,3))

# Calculate and plot the Fourier transforms
square_wave_signal = square_wave(N)
plot_amplitude_spectrum(square_wave_signal, 'Square Wave', axes[0])

sawtooth_wave_signal = sawtooth_wave(N)
plot_amplitude_spectrum(sawtooth_wave_signal, 'Sawtooth Wave', axes[1])

modulated_sine_wave_signal = modulated_sine_wave(N)
plot_amplitude_spectrum(modulated_sine_wave_signal, 'Modulated Sine Wave', axes[2])

plt.show()

