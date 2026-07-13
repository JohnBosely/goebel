"""
FFT-based feature extraction for bearing vibration signals (CWRU / IMS).

TODO:
- load_signal(path) -> raw vibration array + sampling rate
- fft_features(signal, fs) -> dominant frequency peaks, band energies
  known bearing fault frequencies to extract energy around:
    BPFO (ball pass frequency outer race)
    BPFI (ball pass frequency inner race)
    BSF  (ball spin frequency)
  formulas depend on bearing geometry (given in CWRU dataset docs)
"""
import numpy as np
from scipy.fft import fft, fftfreq


def load_signal(path: str):
    raise NotImplementedError


def fft_features(signal: np.ndarray, fs: float) -> dict:
    n = len(signal)
    yf = np.abs(fft(signal))
    xf = fftfreq(n, 1 / fs)
    # placeholder: return top-3 peak frequencies + total energy
    raise NotImplementedError
