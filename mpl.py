import matplotlib
import matplotlib.pyplot as plt
from cycler import cycler

plt.rcParams['axes.grid']=True
plt.rcParams['image.cmap']='inferno'
plt.rcParams['axes.prop_cycle']=cycler(color=['k','r','b','g','orange','purple','yellow'])
plt.rcParams['lines.linewidth']=1
plt.rcParams['lines.markersize']=1
plt.rcParams['hist.bins']=100


class MyFigure(matplotlib.figure.Figure):
    def add_subplot(self,*args,**kwargs):
        ax=super().add_subplot(*args,**kwargs)
        ax.__class__=MyAxis
        return ax

class MyAxis(matplotlib.axes.Axes):
    def log(self):
        self.set_xscale('log')
        self.set_yscale('log')

    def lin(self):
        self.set_xscale('linear')
        self.set_yscale('linear')

    def logx(self):
        self.set_xscale('log')

    def logy(self):
        self.set_yscale('log')

    def linx(self):
        self.set_xscale('linear')

    def liny(self):
        self.set_yscale('linear')

    def labels(self,x='',y='',title=''):
        self.set_xlabel(x)
        self.set_ylabel(y)
        self.set_title(title)

    def limits(self,x=None,y=None):
        if not x is None: self.set_xlim(x)
        if not y is None: self.set_ylim(y)


def figure(*args,**kwargs):
    fig=plt.figure(*args,**kwargs)
    fig.__class__=MyFigure
    return fig
