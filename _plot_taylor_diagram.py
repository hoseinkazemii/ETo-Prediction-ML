import numpy as np
import matplotlib.pyplot as plt
from matplotlib.projections import PolarAxes
import mpl_toolkits.axisartist.grid_finder as gf
import mpl_toolkits.axisartist.floating_axes as fa


class TaylorDiagram(object):
    def __init__(self, STD, fig=None, rect=111, label='_'):
        self.STD = STD
        tr = PolarAxes.PolarTransform()
        # Correlation labels
        rlocs = np.concatenate(((np.arange(11.0) / 10.0), [0.95, 0.99]))
        tlocs = np.arccos(rlocs)  # Conversion to polar angles
        gl1 = gf.FixedLocator(tlocs)  # Positions
        tf1 = gf.DictFormatter(dict(zip(tlocs, map(str, rlocs))))
        # Standard deviation axis extent
        self.smin = 0
        self.smax = 1.6 * self.STD
        gh = fa.GridHelperCurveLinear(tr, extremes=(0, (np.pi / 2), self.smin, self.smax),
                                      grid_locator1=gl1, tick_formatter1=tf1)
        if fig is None:
            fig = plt.figure()
        ax = fa.FloatingSubplot(fig, rect, grid_helper=gh)
        fig.add_subplot(ax)
        # Angle axis
        ax.axis['top'].set_axis_direction('bottom')
        ax.axis['top'].label.set_text("Correlation Coefficient")
        ax.axis["top"].label.set_fontsize(20)
        ax.axis['top'].toggle(ticklabels=True, label=True)
        ax.axis['top'].major_ticklabels.set_axis_direction('top')
        ax.axis['top'].label.set_axis_direction('top')
        ax.axis['top'].major_ticklabels.set_fontsize(14)

        # X axis
        ax.axis['left'].set_axis_direction('bottom')
        ax.axis['left'].label.set_text("Standard Deviation")
        ax.axis["left"].label.set_fontsize(20)
        ax.axis['left'].toggle(ticklabels=True, label=True)
        ax.axis['left'].major_ticklabels.set_axis_direction('bottom')
        ax.axis['left'].label.set_axis_direction('bottom')
        ax.axis['left'].major_ticklabels.set_fontsize(14)
        # Y axis
        ax.axis['right'].set_axis_direction('top')
        ax.axis['right'].label.set_text("Standard Deviation")
        ax.axis["right"].label.set_fontsize(20)
        ax.axis['right'].toggle(ticklabels=True, label=True)
        ax.axis['right'].major_ticklabels.set_axis_direction('left')
        ax.axis['right'].label.set_axis_direction('top')
        ax.axis['right'].major_ticklabels.set_fontsize(14)
        # Useless
        ax.axis['bottom'].set_visible(False)
        # Contours along standard deviations
        ax.grid()
        self._ax = ax  # Graphical axes
        self.ax = ax.get_aux_axes(tr)  # Polar coordinates
        # Add reference point and STD contour
        l, = self.ax.plot([0], self.STD, 'k*', ls='', ms=12, label=label)
        t = np.linspace(0, (np.pi / 2.0))
        t1 = np.linspace(0, (np.pi / 2.0))
        r = np.zeros_like(t) + self.STD
        r1 = np.zeros_like(t) + self.STD
        self.ax.plot(t, r, 'k--', label='_')
        # Collect sample points for later use (e.g., legend)
        self.samplePoints = [l]

    def add_sample(self, STD, r, *args, **kwargs):
        l, = self.ax.plot(np.arccos(r), STD, *args, **kwargs)  # (theta, radius)
        self.samplePoints.append(l)
        return l

    def add_contours(self, levels=10, **kwargs):
        rs, ts = np.meshgrid(np.linspace(self.smin, self.smax), np.linspace(0, (np.pi / 2.0)))
        RMSE = np.sqrt(np.power(self.STD, 2) + np.power(rs, 2) - (2.0 * self.STD * rs * np.cos(ts)))
        contours = self.ax.contour(ts, rs, RMSE, levels, **kwargs)
        return contours

def srl(obsSTD, s, r, l, fname):
    plt.rcParams["font.family"] = "Times New Roman"

    fig = plt.figure(figsize=(8, 8))
    dia = TaylorDiagram(obsSTD, fig=fig, rect=111, label='Ref')
    plt.clabel(dia.add_contours(colors='#808080'), inline=1, fontsize=14)
    srlc = zip(s, r, l)

    colors = ['red', 'green', 'blue', 'orange', 'purple']
    for j, i in enumerate(srlc):
        dia.add_sample(i[0], i[1], label=i[2], marker='o', mec=colors[j % len(colors)], mfc='none', mew=1.6, markersize=8)
    spl = [p.get_label() for p in dia.samplePoints]
    legend = fig.legend(dia.samplePoints, spl, numpoints=1, prop=dict(size='medium'), loc=[0.7, 0.3])
    for handle in legend.legendHandles:
        handle.set_linewidth(0)
    for text in legend.get_texts():
        text.set_fontsize(14)

    plt.savefig(fname, dpi=600, bbox_inches="tight")


obsSTD = 2.187246776

s = [1.820900759, 1.901975395, 0.832069022, 1.945085126, 3.477296634]
r = [0.908093006, 0.896167966, 0.928516826, 0.878244433, 0.805333627]

l = ['CatBoost', 'RF', 'HS', 'PT', 'R']

rmse_values = [0.9333, 0.9732, 2.6894, 1.3484, 2.1743]

fname = 'TaylorDiagram.jpg'
srl(obsSTD, s, r, l, fname)
plt.savefig("TaylorDiagram.tif", dpi=600, bbox_inches="tight")