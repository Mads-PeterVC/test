import numpy as np
import matplotlib.pyplot as plt

def simple_test(x):
    x = np.array(x)
    return x**2

def plot_function(x, func):
    fig, ax = plt.subplots()
    ax.plot(x, func(x))
