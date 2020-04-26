from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def pixelate(filename):
    x_max = 25.5
    y_max = 25.5

    picture = Image.open(filename)
    # width, height = picture.size
    # print(width, height)
    picture_small = picture.resize((26, 26), resample=Image.NEAREST)

    grid_x_ticks = np.arange(-0.5, x_max, 1)
    grid_y_ticks = np.arange(-0.5, y_max, 1)

    f1 = plt.figure(1)
    plt.xlim([-0.5, x_max])
    plt.ylim([y_max, -0.5])
    ax = f1.add_subplot(1, 1, 1)
    ax.set_xticks(grid_x_ticks, minor=True)
    ax.set_yticks(grid_y_ticks, minor=True)
    ax.grid(which='minor', alpha=1, linestyle='-', color='black')
    plt.imshow(picture_small)

    plt.figure(2)
    plt.imshow(picture)
    plt.show()


pixelate('1200px-Python-logo-notext.svg.png')
