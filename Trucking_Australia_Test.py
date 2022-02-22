from email.headerregistry import Address
from lib2to3.pgen2 import driver


class Driver():
    maxDemeritPoints = 12
    def __init__(self,licenceNo, firstName, lastName, mobile,address, licenseState, demeritPoints) :
        self.licenceNo = licenceNo
        self.firstName = firstName
        self.lastName = lastName
        self.mobile = mobile
        self.address = address
        self.licenseState = licenseState
        self.demeritPoints = demeritPoints
        #self.addDemeritPoints(newValue=demeritPoints)
    
    
    def displayDriverDetails(self):
        print("The driver", self.firstName, self.lastName, ", has a driver licence number : ", self.licenceNo)
        print("Contact phone number is :", self.mobile)
        print("Driver address is :")
        for x in self.address:
            print(x, ":", self.address[x])
        print("licensed to drive in the following states : ")
        for i in range(len(self.licenseState)):
            print(self.licenseState[i], ":", end=" ")


    def displayDemeritPoints(self):
            print("The driver", self.firstName, self.lastName ,"has", self.demeritPoints, "x Demerit Points remaining.")

    def addDemeritPoints(self,newValue):
        if newValue> Driver.maxDemeritPoints:
            print("Invalid Entry")
        else:
            self.demeritPoints += newValue

    def deleteDemeritPoints(self, delValue):
        self.demeritPoints -= delValue
        if self.demeritPoints <= 3:
            print("WARNING MESSAGE: \n License Suspension is imminenet \n",self.demeritPoints, "x Demerit Points remaining"  )


class Vehical():
    def __init__(self, registrationNo, make, model, kmDriven, driverDetails) :
        self.registrationNo = registrationNo
        self.make = make
        self.model = model
        self.kmDriven = kmDriven
        self.obj_driver = driverDetails
    
    def displayVehicleData(self):
        pass

    def updateKM(self):
        pass



class Car(Vehical):
    def __init__(self, registrationNo, make, model, kmDriven, driverDetails, bodyType, colour, uphostery, NoOfDoors):
        super().__init__(registrationNo, make, model, kmDriven, driverDetails)
        self.bodyType = bodyType
        self.colour = colour
        self.uphostery = uphostery
        self.NoOfDoors = NoOfDoors

    def updateKM(self, newDrivenKm):
        self.kmDriven += newDrivenKm
    
    def updateColour(self, newColour):
        self.colour = newColour

    def displayVehicleData(self):
        print("Vehicle registration number ",self.registrationNo, "is a ", self.make, ". Model is ", self.model, ". Odometer ", self.kmDriven)
        print("The driver of the vehicle is ", self.obj_driver.firstName, self.obj_driver.lastName)
        print("Additional details:")
        print("The car details are: body type ", self.bodyType, ", colour ", self.colour,"," ,self.uphostery,",", self.NoOfDoors, "doors.")
   

class Truck(Vehical):
    def __init__(self, registrationNo, make, model, kmDriven, driverDetails, maxLoad, NoOfAxles, NoOfWheels):
        super().__init__(registrationNo, make, model, kmDriven, driverDetails)
        self.maxLoad = maxLoad
        self.NoOfAxles = NoOfAxles
        self.NoOfWheels = NoOfWheels

    def updateKM(self, newDrivenKm):
        self.kmDriven += newDrivenKm

    def displayVehicleData(self):
        print("Vehicle registration number ",self.registrationNo, "is a ", self.make, ". Model is ", self.model, ". Odometer ", self.kmDriven)
        print("The driver of the vehicle is ", self.obj_driver.firstName, self.obj_driver.lastName)
        print("Additional details:")
        print("The truck details are: maximum load ", self.maxLoad, "No of Axles ", self.NoOfAxles, ",", self.NoOfWheels, "wheels ,")


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

#test driver1 and driver2 demerit points

driver1.displayDemeritPoints()
driver1.deleteDemeritPoints(30)
driver1.addDemeritPoints(2)
driver1.displayDemeritPoints()

# driver2.displayDemeritPoints()
# driver2.deleteDemeritPoints(4)
# driver2.addDemeritPoints(4)
# driver2.displayDemeritPoints()

# car1.displayVehicleData()
# print("\n")
# car1.updateColour('White')
# car1.updateKM(12000)
# car1.displayVehicleData()

# truck1.displayVehicleData()
# print("\n")
# truck1.updateKM(12000)
# truck1.displayVehicleData()


