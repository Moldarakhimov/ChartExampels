import matplotlib.pyplot as plt
import numpy as np

def plot_chart():
    # Данные для графика
    np.random.seed(19680801)
    fig, ax = plt.subplots()
    for color in ['tab:blue', 'tab:orange', 'tab:green']:
        n = 750
        x, y = np.random.rand(2, n)
        scale = 200.0 * np.random.rand(n)
        ax.scatter(x, y, c=color, s=scale, label=color, alpha=0.3, edgecolors='none')
    ax.legend()
    ax.grid(True)
    plt.show()
