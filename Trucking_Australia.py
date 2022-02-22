class Driver():
    def __init__(self,licenceNo, firstName, lastName, mobile,address, licenseState, demeritPoints) :
        self.licenceNo = licenceNo
        self.firstName = firstName
        self.lastName = lastName
        self.mobile = mobile
        self.address = address
        self.licenseState = licenseState
        self.demeritPoints = demeritPoints
    
    #def displayDriverDetails(self):
       

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

#instantiation and hard-coding of objects
states1 = ['Victoria', 'New South Wales', 'Queensland', 'Northern Territory']
states2 = ['Victoria', 'New South Wales', 'Queensland', 'Tasmania','South Australia']
address1 = {'Street':'178 Bluff Road','City':'Manly','State':'NSW','PostCode':'2101'}
address2 = {'Street':'10 Downing Street','City':'Brighton','State':'VIC','PostCode':'3188'}
driver1 = Driver(3313377,'Gladys','Berejkilan','0414566999', address1, states1, 8)
driver2 = Driver(9877345, 'Boris','Johnson','0414123456', address2, states2, 2)
car1 = Car('BBJ702','Mazde','CX3',10000, driver1, 'Hatch','Blue','Leather',5)
car2 = Car('OYO400','Ford','Festive',39785, driver2, 'Sedan', 'Green','Fabric', 4)
truck1 = Truck('XJBJ882','Kenworth','BigMOther5000',150000, driver1, '40 tonnes', 5, 18 )
truck2 = Truck('ARC542','Hyundai','iLoad',76520, driver2, '2 tonnes', 2, 4)

driver1.displayDriverDetails()