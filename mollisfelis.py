# mollisfelis.py

import math

def linear(t):
    return t

def ease_in_quad(t):
    return t ** 2

def ease_out_quad(t):
    return 1 - (1 - t) ** 2

def ease_in_out_quad(t):
    return 2 * t ** 2 if t < 0.5 else 1 - (-2 * t + 2) ** 2 / 2

def ease_in_cubic(t):
    return t ** 3

def ease_out_cubic(t):
    return 1 - (1 - t) ** 3

def ease_in_out_cubic(t):
    return 4 * t ** 3 if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2

def ease_in_quart(t):
    return t ** 4

def ease_out_quart(t):
    return 1 - (1 - t) ** 4

def ease_in_out_quart(t):
    return 8 * t ** 4 if t < 0.5 else 1 - (-2 * t + 2) ** 4 / 2

def ease_in_quint(t):
    return t ** 5

def ease_out_quint(t):
    return 1 - (1 - t) ** 5

def ease_in_out_quint(t):
    return 16 * t ** 5 if t < 0.5 else 1 - (-2 * t + 2) ** 5 / 2

def ease_in_sine(t):
    return 1 - math.cos((t * math.pi) / 2)

def ease_out_sine(t):
    return math.sin((t * math.pi) / 2)

def ease_in_out_sine(t):
    return -(math.cos(math.pi * t) - 1) / 2

def ease_in_expo(t):
    return 0 if t == 0 else 2 ** (10 * t - 10)

def ease_out_expo(t):
    return 1 if t == 1 else 1 - 2 ** (-10 * t)

def ease_in_out_expo(t):
    if t == 0:
        return 0
    if t == 1:
        return 1
    return 2 ** (20 * t - 10) / 2 if t < 0.5 else (2 - 2 ** (-20 * t + 10)) / 2

def ease_in_circ(t):
    return 1 - math.sqrt(1 - t ** 2)

def ease_out_circ(t):
    return math.sqrt(1 - (t - 1) ** 2)

def ease_in_out_circ(t):
    return (1 - math.sqrt(1 - (2 * t) ** 2)) / 2 if t < 0.5 else (math.sqrt(1 - (-2 * t + 2) ** 2) + 1) / 2

def ease_in_back(t):
    c1 = 1.70158
    c3 = c1 + 1
    return c3 * t ** 3 - c1 * t ** 2

def ease_out_back(t):
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2

def ease_in_out_back(t):
    c1 = 1.70158
    c2 = c1 * 1.525
    return (2 * t) ** 2 * ((c2 + 1) * 2 * t - c2) / 2 if t < 0.5 else ((2 * t - 2) ** 2 * ((c2 + 1) * (t * 2 - 2) + c2) + 2) / 2

def ease_in_elastic(t):
    c4 = (2 * math.pi) / 3
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        return -2 ** (10 * t - 10) * math.sin((t * 10 - 10.75) * c4)

def ease_out_elastic(t):
    c4 = (2 * math.pi) / 3
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        return 2 ** (-10 * t) * math.sin((t * 10 - 0.75) * c4) + 1

def ease_in_out_elastic(t):
    c5 = (2 * math.pi) / 4.5
    if t == 0:
        return 0
    elif t == 1:
        return 1
    elif t < 0.5:
        return -(2 ** (20 * t - 10) * math.sin((20 * t - 11.125) * c5)) / 2
    else:
        return (2 ** (-20 * t + 10) * math.sin((20 * t - 11.125) * c5)) / 2 + 1

def ease_in_bounce(t):
    return 1 - ease_out_bounce(1 - t)

def ease_out_bounce(t):
    n1 = 7.5625
    d1 = 2.75

    if t < 1 / d1:
        return n1 * t ** 2
    elif t < 2 / d1:
        t -= 1.5 / d1
        return n1 * t ** 2 + 0.75
    elif t < 2.5 / d1:
        t -= 2.25 / d1
        return n1 * t ** 2 + 0.9375
    else:
        t -= 2.625 / d1
        return n1 * t ** 2 + 0.984375

def ease_in_out_bounce(t):
    return (1 - ease_out_bounce(1 - 2 * t)) / 2 if t < 0.5 else (1 + ease_out_bounce(2 * t - 1)) / 2
