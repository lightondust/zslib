import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def scatter_plot3D(arr, dims=(0,1,2)):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter3D(arr[:,dims[0]], arr[:,dims[1]], arr[:,dims[2]])


def scatter_plot3Ds(arrs, dims=(0,1,2), transvers=False):
    fig = plt.figure()
    ax = Axes3D(fig)
    for i, arr in enumerate(arrs):
        if transvers:
            arr = arr.T
        ax.scatter3D(arr[dims[0]], arr[dims[1]], arr[dims[2]])


def scatter_plot_by_group(arr, intvl_length=50):
    plt.figure()
    label_count = 0
    for pos in range(0, arr.shape[0], intvl_length):
        plt.scatter(arr[:,0][pos:pos + intvl_length], arr[:,1][pos:pos + intvl_length], label=str(label_count))
        label_count += 1
    plt.legend()


def scatter_plot(arr):
    plt.figure()
    plt.scatter(arr[:,0], arr[:,1], label='a')
    plt.legend()


def scatter_plots(arrs, ax=[0,1], labels=[], figsize=(8,7), title='', save=False, filename='',transvers=False):
    from matplotlib.markers import TICKLEFT, TICKRIGHT, TICKUP, TICKDOWN, CARETLEFT, CARETRIGHT, CARETUP, CARETDOWN
    plt.figure(figsize=figsize, dpi=200)
    markers = [
        ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_',
        TICKLEFT, TICKRIGHT, TICKUP, TICKDOWN, CARETLEFT, CARETRIGHT, CARETUP, CARETDOWN
    ]
    if len(markers) < len(arrs):
        markers = markers * (int(len(arrs) / len(markers) + 1))
    if not len(labels):
        labels = range(1, len(arrs)+1)
    for count, arr in enumerate(arrs):
        if transvers:
            arr = arr.T
        plt.scatter(arr[ax[0]], arr[ax[1]], s=10, alpha =0.4, label=labels[count], marker=markers[count])
    plt.title(title)
    plt.legend()

    if save:
        if not filename:
            filename = 'temp.png'
        plt.savefig(filename)
        plt.close()


