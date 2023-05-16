import os
import json
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from config import MindBridge
import requests
from convertFileFormat import ConvertFileFormat
from eeg_positions import get_elec_coords
from util import *
class JsBridge(QtCore.QObject):
    responseSignal = pyqtSignal(str)
    getFromServer = pyqtSignal(str)

    def __init__(self, parent=None):
        super(JsBridge, self).__init__(parent)
        self.responseSignal.connect(self.responseCall)
        self.getFromServer.connect(self.postFromServer)
        self.mainwindow = parent
        self.dir_path = ''

    @QtCore.pyqtSlot(str, result=str)
    def requestFromClient(self, message):
        message = json.loads(message)
        data = None

        if message["action"] == 'trigger':
            data = self.trigger(message)

        if message["action"] == "start-session":
            self.startSession(message)
            data = 'ok'

        if message['action'] == 'stop-session':
            data = self.stopSession(message)

        if message['action'] == 'start-stream':
            data = self.startStream(message)

        if message['action'] == 'stop-stream':
            data = self.stopStream(message)

        if message['action'] == 'choose-file':
            data = self.choosefile(message)

        if message['action'] == 'choose-dir':
            data = self.chooseDir(message)

        if message['action'] == 'impendence-data':
            data = self.impendenceData(message)

        if message['action'] == 'update-bad-channel':
            data = self.updateBadChannel(message)

        if message['action'] == 'start-impendence-test':
            data = self.startImpendenceTest(message)

        if message['action'] == 'end-impendence-test':
            data = self.endImpendenceTest(message)

        if message['action'] == 'get-config':
            data = self.postConfigToPage(message)

        if message['action'] == 'get-bad-channel':
            data = self.getBadChannel(message)

        if message['action'] == 'get-battery-proportion':
            data = self.getBatterVertage(message)

        if message['action'] == 'get-applications':
            data = self.getApplication(message)

        if message['action'] == 'open-html':
            data = self.openHtml(message)

        if message['action'] == 'go-to-home-page':
            data = self.goToHomePage(message)

        if message['action'] == 'open-time-serise-window':
            data = self.openTimeSeriseWindow(message)

        if message['action'] == 'close-time-serise-window':
            data = self.closeTimeSeriseWindow(message)

        if message['action'] == 'open-psd-window':
            data = self.openPSDWindow(message)

        if message['action'] == 'close-psd-window':
            data = self.closePSDWindow(message)

        if message['action'] == 'open-head-plot-window':
            data = self.openHeadPlotWindow(message)

        if message['action'] == 'close-head-plot-window':
            data = self.closeHeadPlotindow(message)

        if message['action'] == 'open-fft-window':
            data = self.openfftWindow(message)

        if message['action'] == 'close-fft-window':
            data = self.closefftWindow(message)

        if message['action'] == 'open-real-time-fft':
            data = self.openRealTimeFFTWindow(message)

        if message['action'] == 'post-time-serise-channel-show':
            data = self.postTimeSeriseChannelShow(message)
        
        if message['action']  == 'get-time-serise-channel-show':
            data = self.getTimeSeriseChannelShow(message)

        if message['action'] == 'init-board':
            data = self.initTestBoard(message)

        if message['action'] == 'full-screen':
            data = self.fullScreen(message)

        if message['action'] == 'exit-full-screen':
            data = self.exitFullScreen(message)

        if message['action'] == 'init-dev-tools':
            data = self.initDevTools(message)

        if message['action'] == 'get-p300-dectation':
            data = self.getP300Dectation(message)

        if message['action'] == 'get-current-board-data':
            data = self.getCurrentBoardData(message)

        if message['action'] == 'open-file-dialog':
            data = self.openFileDialog(message)

        if message['action'] == 'open-dir-dialog':
            data = self.openDirectory(message)

        if message['action'] == 'create-mechain-learn-p300':
            data = self.createMechainLearnP300(message)

        if message['action'] == 'filter-board-dta':
            data = self.filterBoardData(message)

        if message['action'] == 'convert-file-format':
            data = self.convertFileFormat(message)

        if message['action'] == 'get-eeg-electron-position':
            data = self.getEEGElectronPosition(message)

        if message['action'] == 'start-custom-paradigm':
            data = self.startCustomParadigm(message)

        if message['action'] == 'stop-custom-paradigm':
            data = self.endCustomParadigm(message)

        message['data'] = data
        return self.responseSignal.emit(json.dumps(message))

    @QtCore.pyqtSlot(str, result=str)
    def context(self, message):
        self.handleMessage(message)

    def responseCall(self, message):
        return message

    def postFromServer(self, message):
        return message

    def handleMessage(self, message):
        print(message)

    def startSession(self, message):
        data = self.mainwindow.startSession(message)
        return data

    def startStream(self, message):
        self.mainwindow.startStream(message)

    def stopStream(self, message):
        self.mainwindow.stopStream(message)
        return 'ok'

    def stopSession(self, message):
        self.mainwindow.stopSession(message)
        return 'ok'


    def choosefile(self, message):
        print('message')

    def chooseDir(self, message):
        print("message")


    def trigger(self, message):
        self.mainwindow.trigger(message['data'])
        return 'ok'

    def startImpendenceTest(self, message):
        data = self.mainwindow.startImpendenceTest(message)
        return data

    def endImpendenceTest(self, message):
        data = self.mainwindow.endImpendenceTest(message)
        return data

    def impendenceData(self, message):
        data = self.mainwindow.getImpendenceData(message)
        return data

    def postConfigToPage(self, message):
        mindBridge = MindBridge()
        return json.dumps(dict({"channels": mindBridge.channelImpedences, "products": mindBridge.products}))


    def getApplication(self, message):
        data = os.listdir('./web-app')
        return data

    def openHtml(self, message):
        self.mainwindow.openHtml(message['data'])
        return 'ok'

    def goToHomePage(self, message):
        self.mainwindow.homePage()
        return 'ok'

    def openTimeSeriseWindow(self, message):
        return self.mainwindow.openTimeSeriseWindow(message)

    def openRealTimeFFTWindow(self, message):
        return self.mainwindow.openRealTimeFFTWindow(message)

    def postTimeSeriseChannelShow(self, message):
        data = self.mainwindow.postTimeSeriseChannelShow(message)
        return data

    def closeTimeSeriseWindow(self, message):
        data = self.mainwindow.closeTimeSeriseWindow(message)
        return data

    def openfftWindow(self, message):
        data = self.mainwindow.openfftWindow(message)
        return data

    def closefftWindow(self, message):
        data = self.mainwindow.closefftWindow(message)
        return data

    def openPSDWindow(self, message):
        data = self.mainwindow.openPSDWindow(message)
        return data

    def closePSDWindow(self, message):
        data = self.mainwindow.closePSDWindow(message)
        return data

    def openHeadPlotWindow(self, message):
        data = self.mainwindow.openHeadPlotWindow(message)
        return data

    def closeHeadPlotindow(self, message):
        data = self.mainwindow.closeHeadPlotindow(message)
        return data

    def fullScreen(self, message):
        self.mainwindow.fullScreen(message)

    def exitFullScreen(self, message):
        self.mainwindow.exitFullScreen(message)

    def initDevTools(self, message):
        self.mainwindow.initDevTools()

    def getP300Dectation(self, message):
        self.mainwindow.getRelTimeDectation(message)

    def getCurrentBoardData(self, message):
        return self.mainwindow.getCurrentBoardData(message)

    def getBatterVertage(self, message):
        try:
            result = requests.get(
                'http://'+message['data']['ip'] + ':80/BatteryVoltage', timeout=1, headers={'Connection': 'close'})
            res = json.loads(result.text)
            Battery = res['BatteryProportion']
            return int(Battery / 10)
        except Exception as e:
            print(e)
            return 0

    def initTestBoard(self, message):
        try:
            result = requests.get(
                'http://'+message['data']['ip'] + ':80/all', timeout=3, headers={'Connection': 'close'})
            res = json.loads(result.text)
            result.close()
            if result.status_code != 200:
                return "fail"
            else:
                if message['data']['productId'] == '5' and res['num_channels'] == 8:
                    return 'ok'
                if message['data']['productId'] == '516' and res['num_channels'] == 16:
                    return 'ok'
                if message['data']['productId'] == '532' and res['num_channels'] == 32:
                    return 'ok'
                if message['data']['productId'] == '564' and res['num_channels'] == 64:
                    return 'ok'
                if message['data']['productId'] == '520' and res['CHIP_CHANNEL_NUM'] == 6:
                    return 'ok'

                return 'fail'
        except Exception as e:
            print(e)
            return 'false'
        return 'ok'

    def openFileDialog(self, message):
        fileName = self.mainwindow.openFileDialog(message)
        return fileName

    def openFilesDialog(self, message):
        fileNames = self.mainwindow.openFilesDialog(message)
        return fileNames

    def openDirectory(self, message):
        dir = self.mainwindow.openDirectory(message)
        return dir

    # 实时数据进行滤波处理
    def filterBoardData(self, message):
        data = self.mainwindow.filterBoardData(message)
        return data

    def getBadChannel(self, message):
        if self.mainwindow.badChannel == None:
            return []
        return self.mainwindow.badChannel

    def updateBadChannel(self, message):
        return self.mainwindow.updateBadChannel(message['data'])

    def getEEGElectronPosition(self, message):
        coords = get_elec_coords(system='1010', as_mne_montage=False)
        data = [coords['label'].tolist(), coords['x'].tolist(),
                coords['y'].tolist()]
        return data

    def getTimeSeriseChannelShow(self, message):
        figure = self.mainwindow.figure
        if figure != None:
            channels = figure.getShowChannels()
            print('channels', channels)
            return channels
        return []

    def convertFileFormat(self, message):
        savePath = message['data']['savePath']
        files = message['data']['fileList']
        fileFormat = ConvertFileFormat()
        for file in files:
            if message['data']['type'] == 'edf':
                fileFormat.toEDF(file, message['data'], savePath)
            elif message['data']['type'] == 'openbci':
                fileFormat.toTXT(file, savePath)
            elif message['data']['type'] == 'mne':
                fileFormat.toMNE(file, savePath)
        return 'ok'
    # 生成p300 检测模型

    def startCustomParadigm(self, message):
        self.mainwindow.startCustomParadigm(message)

    def endCustomParadigm(self, message):
        self.mainwindow.endCustomParadigm(message)
    
    def createMechainLearnP300(self, message):
        try:
            trainModel = P300Model()
            self.dir_path = os.getcwd()
            self.dir_path = self.dir_path.replace("\\", "/", 5)
            fileLists = message['data']['fileList']
            if len(fileLists) == '0':
                return 'no file'
            trainModel.createModels(fileLists, message['data'])
        except Exception as e:
            print(e)
            return 'fail create p300 model'
        return 'ok'

    def flush(self):
        pass
