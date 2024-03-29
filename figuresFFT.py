import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import QDir, QTimer, Qt

import matplotlib
from PyQt5 import QtCore, QtWidgets
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, WindowOperations, DetrendOperations
from signals import Signal

import random
class Ui_figuresFFTWidget(object):
    def setupUi(self, figuresFFTWidge):
        print('ui_figuresFFT widget')

class FiguresFFTWindow(QWidget, Ui_figuresFFTWidget):
    def __init__(self):
        super(FiguresFFTWindow, self).__init__()
        self.setupUi(self)
        self.set_matplotlib()
        self.signal = Signal()
        self.scale = []
        self.nowTime = []
        self.showChannels = []
        self.seletChannelIndex = []
        self.channels = []
        self.psd_size = 1024
        self.sampling_rate = 1000
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

    def setChannels(self, channels):
        self.channels = channels
     
    def chooseShowChannel(self, channels):
        selectChannelsIndex = []
        for channel in channels:
            selectChannelsIndex.append(self.channels.index(channel))
        self.seletChannelIndex = selectChannelsIndex

    def set_matplotlib(self):
        self.fig = plt.figure()
        plt.margins(0, 0)
        plt.margins(0, tight=True)
        self.fig.tight_layout(w_pad=0, h_pad=0)
        self.canvas = FigureCanvas(self.fig)
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.canvas)
        self.setLayout(self.vlayout)
        self.ax = self.fig.gca()
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        plt.subplots_adjust(left=0.05, right=1)
        
    def closeEvent(self, a0: QtGui.QCloseEvent):
        if self.signal and self.signal != None:
            self.signal._mainClose.emit('fft')
        return super().closeEvent(a0)
    
    def update(self, data):
        self.ax.clear()
        self.ax.set_ylim(0,20)
        if len(data) != 0:
            plt.xlim(0, 45)
        for i in range(len(data)):
            item = data[i] 
            self.ax.plot(item[1][0:45].tolist(),(np.log2(item[0][0:45] + 1).tolist()))
        self.fig.canvas.draw()  # 画布重绘，self.figs.canvas
        self.fig.canvas.flush_events()

