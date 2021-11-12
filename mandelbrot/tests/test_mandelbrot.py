from mandelbrot.src.mandelbrot import mandelbrot_zoom, plot_sub


def test_mandelbrot_zoom():

    ylim = [-2, 2]
    xlim = [-2.5, 1.5]

    N = 512
    NN = 100

    img = mandelbrot_zoom(xlim=xlim, ylim=ylim, N=N, NN=NN)
