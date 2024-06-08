# test_mollisfelis.py

import time
import matplotlib.pyplot as plt
from mollisfelis.tweener import Tweener
from mollisfelis.easings import *

def plot_tween(duration, easing_func, start_val, end_val):
    tweener = Tweener(duration=duration, easing_func=easing_func)
    tweener.start()

    values = []
    times = []
    start_time = time.time()

    while True:
        current_time = time.time()
        if current_time > tweener.end_time:
            break
        value = tweener.get_value(start_val, end_val)
        values.append(value)
        times.append(current_time - start_time)
        time.sleep(0.01)

    plt.plot(times, values, label=easing_func.__name__)

def main():
    duration = 2  # duração de 2 segundos
    start_val = 0
    end_val = 10

    plt.figure()

    # Adicione aqui as funções de easing que você deseja testar
    easing_functions = [linear, ease_in_quad, ease_out_quad, ease_in_out_quad, ease_in_cubic, ease_out_cubic, ease_in_out_cubic]

    for func in easing_functions:
        plot_tween(duration, func, start_val, end_val)

    plt.xlabel('Time (s)')
    plt.ylabel('Value')
    plt.legend()
    plt.title('Easing Functions')
    plt.show()

if __name__ == "__main__":
    main()
