# mollisfelis/easings.py

import numpy as np

def linear(t):
    return t

def ease_in_quad(t):
    return t ** 2

def ease_out_quad(t):
    return t * (2 - t)

def ease_in_out_quad(t):
    return 2 * t ** 2 if t < 0.5 else -1 + (4 - 2 * t) * t

def ease_in_cubic(t):
    return t ** 3

def ease_out_cubic(t):
    return (t - 1) ** 3 + 1

def ease_in_out_cubic(t):
    return 4 * t ** 3 if t < 0.5 else (t - 1) * (2 * t - 2) * (2 * t - 2) + 1

def ease_in_quart(t):
    return t ** 4

def ease_out_quart(t):
    return 1 - (1 - t) ** 4

def ease_in_out_quart(t):
    return 8 * t ** 4 if t < 0.5 else 1 - 8 * (1 - t) ** 4

def ease_in_quint(t):
    return t ** 5

def ease_out_quint(t):
    return 1 - (1 - t) ** 5

def ease_in_out_quint(t):
    return 16 * t ** 5 if t < 0.5 else 1 - 16 * (1 - t) ** 5

def ease_in_sine(t):
    return -np.cos(t * np.pi / 2) + 1

def ease_out_sine(t):
    return np.sin(t * np.pi / 2)

def ease_in_out_sine(t):
    return -(np.cos(np.pi * t) - 1) / 2

def ease_in_expo(t):
    return 0 if t == 0 else 2 ** (10 * (t - 1))

def ease_out_expo(t):
    return 1 if t == 1 else 1 - 2 ** (-10 * t)

def ease_in_out_expo(t):
    if t == 0:
        return 0
    elif t == 1:
        return 1
    elif t < 0.5:
        return 0.5 * 2 ** (20 * t - 10)
    else:
        return 1 - 0.5 * 2 ** (-20 * t + 10)

def ease_in_circ(t):
    return -np.sqrt(1 - t ** 2) + 1

def ease_out_circ(t):
    return np.sqrt(1 - (t - 1) ** 2)

def ease_in_out_circ(t):
    return 0.5 * (1 - np.sqrt(1 - 4 * t ** 2)) if t < 0.5 else 0.5 * (np.sqrt(1 - (-2 * t + 2) ** 2) + 1)

def ease_in_back(t, s=1.70158):
    return t ** 2 * ((s + 1) * t - s)

def ease_out_back(t, s=1.70158):
    return (t - 1) ** 2 * ((s + 1) * (t - 1) + s) + 1

def ease_in_out_back(t, s=1.70158):
    s *= 1.525
    return 2 * t ** 2 * ((s + 1) * t - s) if t < 0.5 else (2 * t - 2) ** 2 * ((s + 1) * (2 * t - 2) + s) / 2 + 1

def ease_in_elastic(t, amplitude=1, period=0.3):
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        s = period / 4
        return -(amplitude * 2 ** (10 * (t - 1))) * np.sin((t - s) * (2 * np.pi) / period)

def ease_out_elastic(t, amplitude=1, period=0.3):
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        s = period / 4
        return amplitude * 2 ** (-10 * t) * np.sin((t - s) * (2 * np.pi) / period) + 1

def ease_in_out_elastic(t, amplitude=1, period=0.45):
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        s = period / 4
        return -0.5 * (amplitude * 2 ** (10 * (t - 1))) * np.sin((t - s) * (2 * np.pi) / period) if t < 0.5 else amplitude * 2 ** (-10 * (2 * t - 1)) * np.sin((2 * t - 1 - s) * (2 * np.pi) / period) * 0.5 + 1

def ease_in_bounce(t):
    return 1 - ease_out_bounce(1 - t)

def ease_out_bounce(t):
    if t < (1 / 2.75):
        return 7.5625 * t ** 2
    elif t < (2 / 2.75):
        t -= 1.5 / 2.75
        return 7.5625 * t ** 2 + 0.75
    elif t < (2.5 / 2.75):
        t -= 2.25 / 2.75
        return 7.5625 * t ** 2 + 0.9375
    else:
        t -= 2.625 / 2.75
        return 7.5625 * t ** 2 + 0.984375

def ease_in_out_bounce(t):
    return 0.5 * ease_in_bounce(2 * t) if t < 0.5 else 0.5 * ease_out_bounce(2 * t - 1) + 0.5
