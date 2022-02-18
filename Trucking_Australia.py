class Driver():
    def __init__(self,licenceNo, firstName, lastName, mobile,address, licenseState, demeritPoints) :
        self.licenceNo = licenceNo
        self.firstName = firstName
        self.lastName = lastName
        self.mobile = mobile
        self.address = address
        self.licenseState = licenseState
        self.demeritPoints = demeritPoints
    
    #def displayDriverDetails():

    #def displayDemerits(self):

    #def addDemerits(self):
    
    #def deleteDemerits(self):

class Vehical():
    def __init__(self, registrationNo, make, model, kmDriven, driverDetails) :
        self.registrationNo = registrationNo
        self.make = make
        self.model = model
        self.kmDriven = kmDriven
        self.obj_driver = driverDetails

class Car(Vehical):
    def __init__(self, registrationNo, make, model, kmDriven, driverDetails, bodyType, colour, uphostery, NoOfDoors):
        super().__init__(registrationNo, make, model, kmDriven, driverDetails)
        self.bodyType = bodyType
        self.colour = colour
        self.uphostery = uphostery
        self.NoOfDoors = NoOfDoors

class Truck(Vehical):
    def __init__(self, registrationNo, make, model, kmDriven, driverDetails, maxLoad, NoOfAxles, NoOfWheels):
        super().__init__(registrationNo, make, model, kmDriven, driverDetails)
        self.maxLoad = maxLoad
        self.NoOfAxles = NoOfAxles
        self.NoOfWheels = NoOfWheels