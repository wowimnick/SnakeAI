import matplotlib.pyplot as plt
from IPython import display
from scipy.interpolate import make_interp_spline
import numpy as np

plt.style.use('ggplot')


def start():
    plt.ion()
    fig = plt.figure()
    return fig

def plot(scores, mean_scores, fig):
    display.clear_output(wait=False)
    fig.canvas.toolbar.pack_forget()
    display.display(plt.gcf())
    plt.clf()
    plt.box(False)
    plt.title('Training...')
    plt.xlabel('Episodes')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores, 'go-')
    plt.ylim(ymin=0)
    plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)
