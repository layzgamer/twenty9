import threading
from PyQt4 import QtNetwork,QtCore
class Client():
    def __init__(self,name,socket):
        self.Name = name
        self.Socket = socket
        self.Hand = []
        
class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.server = None
        self.sockets = []
        self.clients = []
        self.scores = [(0,0),(0,0)]
        self.trump = None
        self.deck = []
        self.pit = []
        self.temp = None
    def run(self):
        self.server = QtNetwork.QTcpServer()
        if self.server.listen():
            print self.server.serverAddress().toString()
            print int(self.server.serverPort())       
        QtCore.QObject.connect(self.server, QtCore.SIGNAL("newConnection()"),self.newConnection)
        
    def newConnection(self):
        socket = self.server.nextPendingConnection()
        self.sockets.append(socket)
        for i in self.sockets:
            QtCore.QObject.connect(i, QtCore.SIGNAL("readyRead()"),self.readyReadEmitted)
            
    def readyReadEmitted(self):
        print "baal"
        signal = str(self.temp.readAll())
        if "name:" in signal:
            self.createClient(signal.lstrip("name:"))
    
    def createClient(self,name):
        newClient = Client(name,self.temp)
        clients.append(newClient)
        print "client successfully added!!"