#!/usr/bin/env python
import id3reader
import os
import sip
sip.setapi('QString', 2)
import sys
from PyQt4 import QtCore, QtGui
from Const import *
from main import music
import time
import unicodedata
global user
user="user"

try:
    from PyQt4.phonon import Phonon
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "Music Player",
            "Your Qt installation does not have Phonon support.",
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
            QtGui.QMessageBox.NoButton)
    sys.exit(1)

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(QtGui.QMainWindow, self).__init__()

        self.setWindowIcon(QtGui.QIcon('icon.png'))
        
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mediaObject = Phonon.MediaObject(self)
        self.metaInformationResolver = Phonon.MediaObject(self)

        self.mediaObject.setTickInterval(1000)

        self.mediaObject.tick.connect(self.tick)
        self.mediaObject.stateChanged.connect(self.stateChanged)
        self.metaInformationResolver.stateChanged.connect(self.metaStateChanged)
        self.mediaObject.currentSourceChanged.connect(self.sourceChanged)
        self.mediaObject.aboutToFinish.connect(self.aboutToFinish)

        Phonon.createPath(self.mediaObject, self.audioOutput)

        self.setupActions()
        self.setupMenus()
        self.setupUi()
        self.timeLcd.display("00:00") 

        self.sources = []

    def sizeHint(self):
        return QtCore.QSize(1000, 350)
		
    def create(self):
        myapp.show()
        return

    def login(self):
        global user
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        if ok == True:
            user = text
            self.label.setText("Hello "+text.upper())
        else:
            user = "user"
            self.label.setText("Welcome "+user)
        with open(user+".txt","a") as c:
            pass
        with open("log.txt","w") as c:
            c.write(user)
        return

    def generate(self):
        global user
        list = music(user)
        index = len(self.sources)
        for x in list:
            try:
                self.sources.append(Phonon.MediaSource(x))                
                id3r = id3reader.Reader(str(x))
                with open(user+".txt","a") as c:
                    c.write("00"+str(id3r.getValue('title'))+"\n")
                    c.write("01"+str(id3r.getValue('performer'))+"\n")
                    c.write("02"+str(id3r.getValue('album'))+"\n")
                    c.write("03"+str(id3r.getValue('year'))+"\n")
                    c.write("04"+str(id3r.getValue('genre'))+"\n")
            except:
                pass

        if self.sources:
            self.metaInformationResolver.setCurrentSource(self.sources[index])

        QtGui.QMessageBox.information(self, "PyMusiqMix","PlayList Created")
        
    def addFiles(self):
        files = QtGui.QFileDialog.getOpenFileNames(self, "Select Music Files",
                QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.MusicLocation))
        #save seed songs
        for x in files:
            x = unicodedata.normalize('NFKD', x).encode('ascii','ignore')
            id3r = id3reader.Reader(str(x))
            with open(user+".txt","a") as c:
                c.write("00"+str(id3r.getValue('title'))+"\n")
                c.write("01"+str(id3r.getValue('performer'))+"\n")
                c.write("02"+str(id3r.getValue('album'))+"\n")
                c.write("03"+str(id3r.getValue('year'))+"\n")
                c.write("04"+str(id3r.getValue('genre'))+"\n")
        if not files:
            return
        index = len(self.sources)
        for string in files:
            self.sources.append(Phonon.MediaSource(string))
        if self.sources:
            self.metaInformationResolver.setCurrentSource(self.sources[index])

    def about(self):
        QtGui.QMessageBox.information(self, "About PyMusiqMix",
                "This Music Player is a fine example of recommendation playlist"
                "Created by Nimitha,Riya,Tom")

    def stateChanged(self, newState, oldState):
        if newState == Phonon.ErrorState:
            if self.mediaObject.errorType() == Phonon.FatalError:
                QtGui.QMessageBox.warning(self, "Fatal Error",
                        self.mediaObject.errorString())
            else:
                QtGui.QMessageBox.warning(self, "Error",
                        self.mediaObject.errorString())

        elif newState == Phonon.PlayingState:
            
            self.playAction.setEnabled(False)
            self.pauseAction.setEnabled(True)
            self.stopAction.setEnabled(True)

        elif newState == Phonon.StoppedState:
            self.stopAction.setEnabled(False)
            self.playAction.setEnabled(True)
            self.pauseAction.setEnabled(False)
            self.timeLcd.display("00:00")

        elif newState == Phonon.PausedState:
            self.pauseAction.setEnabled(False)
            self.stopAction.setEnabled(True)
            self.playAction.setEnabled(True)

    def tick(self, time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.timeLcd.display(displayTime.toString('mm:ss'))

    def tableClicked(self, row, column):
        wasPlaying = (self.mediaObject.state() == Phonon.PlayingState)

        self.mediaObject.stop()
        self.mediaObject.clearQueue()
        self.mediaObject.setCurrentSource(self.sources[row])

        #reading clicked file

        filename =  self.mediaObject.currentSource().fileName()
        id3r = id3reader.Reader(filename)
        with open(user+".txt","a") as c:
            c.write("00"+str(id3r.getValue('title'))+"\n")
            c.write("01"+str(id3r.getValue('performer'))+"\n")
            c.write("02"+str(id3r.getValue('album'))+"\n")
            c.write("03"+str(id3r.getValue('year'))+"\n")          
            c.write("04"+str(id3r.getValue('genre'))+"\n")

        if wasPlaying:
            self.mediaObject.play()
        else:
            self.mediaObject.stop()
            

    def sourceChanged(self, source):
        self.musicTable.selectRow(self.sources.index(source))        
        self.timeLcd.display('00:00')

    def metaStateChanged(self, newState, oldState):
        if newState == Phonon.ErrorState:
            QtGui.QMessageBox.warning(self, "Error opening files",self.metaInformationResolver.errorString())
            while self.sources and self.sources.pop() != self.metaInformationResolver.currentSource():
               pass
            return
        
        if newState != Phonon.StoppedState and newState != Phonon.PausedState:
            return

        if self.metaInformationResolver.currentSource().type() == Phonon.MediaSource.Invalid:
            return

        metaData = self.metaInformationResolver.metaData()
        
        title = metaData.get('TITLE', [''])[0]
        if not title:
            title = self.metaInformationResolver.currentSource().fileName()

        #metadata
        filename = self.metaInformationResolver.currentSource().fileName()
        id3r = id3reader.Reader(filename)

        titleItem = QtGui.QTableWidgetItem(title)
        titleItem.setFlags(titleItem.flags() ^ QtCore.Qt.ItemIsEditable)

        #artist = metaData.get('ARTIST', [''])[0]
        artist = str(id3r.getValue('performer'))
        artistItem = QtGui.QTableWidgetItem(artist)
        artistItem.setFlags(artistItem.flags() ^ QtCore.Qt.ItemIsEditable)

        #album = metaData.get('ALBUM', [''])[0]
        album = str(id3r.getValue('album'))
        albumItem = QtGui.QTableWidgetItem(album)
        albumItem.setFlags(albumItem.flags() ^ QtCore.Qt.ItemIsEditable)

        #year = metaData.get('DATE', [''])[0]
        year = str(id3r.getValue('year'))
        yearItem = QtGui.QTableWidgetItem(year)
        yearItem.setFlags(yearItem.flags() ^ QtCore.Qt.ItemIsEditable)

        #genre = metaData.get('GENRE', [''])[0]
        genre = str(id3r.getValue('genre'))
        genreItem = QtGui.QTableWidgetItem(genre)
        genreItem.setFlags(genreItem.flags() ^ QtCore.Qt.ItemIsEditable)

        currentRow = self.musicTable.rowCount()
        self.musicTable.insertRow(currentRow)
        self.musicTable.setItem(currentRow, 0, titleItem)
        self.musicTable.setItem(currentRow, 1, artistItem)
        self.musicTable.setItem(currentRow, 2, albumItem)
        self.musicTable.setItem(currentRow, 3, yearItem)
        self.musicTable.setItem(currentRow, 4, genreItem)

        if not self.musicTable.selectedItems():
            self.musicTable.selectRow(0)
            self.mediaObject.setCurrentSource(self.metaInformationResolver.currentSource())

        index = self.sources.index(self.metaInformationResolver.currentSource()) + 1

        if len(self.sources) > index:
            self.metaInformationResolver.setCurrentSource(self.sources[index])
        else:
            self.musicTable.resizeColumnsToContents()
            if self.musicTable.columnWidth(0) > 300:
                self.musicTable.setColumnWidth(0, 300)      

    def aboutToFinish(self):
        
        index = self.sources.index(self.mediaObject.currentSource()) + 1
        if len(self.sources) > index:
            self.mediaObject.enqueue(self.sources[index])

    def setupActions(self):
        self.playAction = QtGui.QAction(
                self.style().standardIcon(QtGui.QStyle.SP_MediaPlay), "Play",
                self, shortcut="Ctrl+P", enabled=False,
                triggered=self.mediaObject.play)

        self.pauseAction = QtGui.QAction(
                self.style().standardIcon(QtGui.QStyle.SP_MediaPause),
                "Pause", self, shortcut="Ctrl+A", enabled=False,
                triggered=self.mediaObject.pause)

        self.stopAction = QtGui.QAction(
                self.style().standardIcon(QtGui.QStyle.SP_MediaStop), "Stop",
                self, shortcut="Ctrl+S", enabled=False,
                triggered=self.mediaObject.stop)

        self.nextAction = QtGui.QAction(
                self.style().standardIcon(QtGui.QStyle.SP_MediaSkipForward),
                "Next", self, shortcut="Ctrl+N")

        self.previousAction = QtGui.QAction(
                self.style().standardIcon(QtGui.QStyle.SP_MediaSkipBackward),
                "Previous", self, shortcut="Ctrl+R")

        self.addFilesAction = QtGui.QAction("Add &Files", self,
                shortcut="Ctrl+F", triggered=self.addFiles)

        self.generateAction = QtGui.QAction("&Generate Playlist", self,
                shortcut="Ctrl+G", triggered=self.generate)
        
        self.createAction = QtGui.QAction("G&ive Constraints", self,
                shortcut="Ctrl+I", triggered=self.create)

        self.exitAction = QtGui.QAction("E&xit", self, shortcut="Ctrl+X",
                triggered=self.close)

        self.aboutAction = QtGui.QAction("A&bout", self, shortcut="Ctrl+B",
                triggered=self.about)

        self.Login = QtGui.QAction("&Login", self, shortcut="Ctrl+L",
                triggered=self.login)

        self.aboutQtAction = QtGui.QAction("About &Qt", self,
                shortcut="Ctrl+Q", triggered=QtGui.qApp.aboutQt)

    def setupMenus(self):
        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(self.Login)
        fileMenu.addAction(self.addFilesAction)
        fileMenu.addAction(self.createAction)
        fileMenu.addAction(self.generateAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)

        aboutMenu = self.menuBar().addMenu("&Help")
        aboutMenu.addAction(self.aboutAction)

    def setupUi(self):

        
        
        self.label = QtGui.QLabel()
        self.label.setGeometry(QtCore.QRect(60, 40, 71, 16))
        self.label.setObjectName("label")
        self.label.setText("Welcome "+user)
        self.lineEdit = QtGui.QLineEdit()
        self.lineEdit.setGeometry(QtCore.QRect(160, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtGui.QPushButton()
        self.pushButton.setGeometry(QtCore.QRect(150, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")

        bar = QtGui.QToolBar()
        bar.addAction(self.playAction)
        bar.addAction(self.pauseAction)
        bar.addAction(self.stopAction)

        self.seekSlider = Phonon.SeekSlider(self)
        self.seekSlider.setMediaObject(self.mediaObject)

        self.volumeSlider = Phonon.VolumeSlider(self)
        self.volumeSlider.setAudioOutput(self.audioOutput)
        self.volumeSlider.setSizePolicy(QtGui.QSizePolicy.Maximum,
                QtGui.QSizePolicy.Maximum)

        volumeLabel = QtGui.QLabel()
        volumeLabel.setPixmap(QtGui.QPixmap('images/volume.png'))

        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Light, QtCore.Qt.darkGray)

        self.timeLcd = QtGui.QLCDNumber()
        self.timeLcd.setPalette(palette)

        headers = ("Title", "Artist", "Album", "Year" ,"Genre")

        self.musicTable = QtGui.QTableWidget(0, 5)
        self.musicTable.setHorizontalHeaderLabels(headers)
        self.musicTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.musicTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.musicTable.cellPressed.connect(self.tableClicked)

        seekerLayout = QtGui.QHBoxLayout()
        seekerLayout.addWidget(self.seekSlider)
        seekerLayout.addWidget(self.timeLcd)

        playbackLayout = QtGui.QHBoxLayout()
        playbackLayout.addWidget(bar)
        playbackLayout.addStretch()
        playbackLayout.addWidget(volumeLabel)
        playbackLayout.addWidget(self.volumeSlider)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.label)#login
        mainLayout.addWidget(self.musicTable)
        mainLayout.addLayout(seekerLayout)
        mainLayout.addLayout(playbackLayout)

        widget = QtGui.QWidget()
        widget.setLayout(mainLayout)

        self.setCentralWidget(widget)
        self.setWindowTitle("PyMusiqMix")

if __name__ == '__main__':
    with open("log.txt","w") as c:
        c.write("user")
    with open("user.txt","a") as c:
        pass
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("PyMusiqMix")
    app.setQuitOnLastWindowClosed(True)
    window = MainWindow()
    myapp = MyForm()
    window.show()
    sys.exit(app.exec_())
