from ast import NodeTransformer


class user:
    def __init__(self):
        self.name = None
        self.email = None
        self.username = None
        self.password = None
        self.ID = None
        self.tickets =[]
    
    def __init__(self,a,b,c,d,id):
        self.name = a
        self.email = b
        self.username = c
        self.password = d
        self.ID = id
        self.tickets =[]
    def addTicket(self,trainID):
        if trainID not in self.tickets:
            self.tickets.append(trainID)
            self.tickets.sort()
        
    

class train:
    def __init__(self):
        self.ID = None
        self.source = None
        self.dest = None
        self.price = None
        self.passengersID = []
    def __init__(self,a,b,c,d):
        self.ID = a
        self.source = b
        self.dest = c
        self.price = d
        self.passengersID = []

    def setID(self,id):
        self.ID = id+100
    def setTrip(self,src , d):
        self.source = src
        self.dest = d
    def setPrice(self,prc):
        self.price = prc
    def addPassenger(self , pas):
        self.passengersID.append(pas)
    