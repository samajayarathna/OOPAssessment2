
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
            print("\nThe driver", self.firstName, self.lastName ,"has", self.demeritPoints, "x Demerit Points remaining.\n")

    def addDemeritPoints(self,newValue):
        totalDemeritPoints = self.demeritPoints + newValue
        if totalDemeritPoints > Driver.maxDemeritPoints:
            print("Invalid Entry....")
        else:
            self.demeritPoints = totalDemeritPoints

    def deleteDemeritPoints(self, delValue):
        if delValue <= self.demeritPoints:
            self.demeritPoints -= delValue
            if self.demeritPoints <= 3:
                print("WARNING MESSAGE: \n License Suspension is imminenet \n",self.demeritPoints, "x Demerit Points remaining"  )
        else:  
            print("Invalid Entry....")  
            

class Vehicle():
    def __init__(self, registrationNo, make, model, kmDriven, driverDetails) :
        self.registrationNo = registrationNo
        self.make = make
        self.model = model
        self.kmDriven = kmDriven
        self.obj_driver = driverDetails
    
    def displayVehicleData(self):
        print("Vehicle registration number ",self.registrationNo, "is a ", self.make, ". Model is ", self.model, ". Odometer ", self.kmDriven)
        print("The driver of the vehicle is ", self.obj_driver.firstName, self.obj_driver.lastName)
    
    def displayGeneralData(self):
        print("Registration No: ", self.registrationNo, "\nMake: ", self.make, "\nModel: ", self.model, "\nDriven KM : ", self.kmDriven)
    
    def updateKM(self,newDrivenKm):
        self.kmDriven += newDrivenKm
        

class Car(Vehicle):
    def __init__(self, registrationNo, make, model, kmDriven, driverDetails, bodyType, colour, uphostery, NoOfDoors):
        super().__init__(registrationNo, make, model, kmDriven, driverDetails)
        self.bodyType = bodyType
        self.colour = colour
        self.uphostery = uphostery
        self.NoOfDoors = NoOfDoors

    def updateKM(self, newDrivenKm):
        return super().updateKM(newDrivenKm)
    
    def updateColour(self, newColour):
        self.colour = newColour

    def displayVehicleData(self):
        Vehicle.displayVehicleData(self)
        print("\nAdditional details:")
        print("The car details are: body type ", self.bodyType, ", colour ", self.colour,"," ,self.uphostery,",", self.NoOfDoors, "doors.")

        
class Truck(Vehicle):
    def __init__(self, registrationNo, make, model, kmDriven, driverDetails, maxLoad, NoOfAxles, NoOfWheels):
        super().__init__(registrationNo, make, model, kmDriven, driverDetails)
        self.maxLoad = maxLoad
        self.NoOfAxles = NoOfAxles
        self.NoOfWheels = NoOfWheels

    def updateKM(self, newDrivenKm):
        self.kmDriven += newDrivenKm

    def displayVehicleData(self):
        Vehicle.displayVehicleData(self)
        print("Additional details:")
        print("The truck details are: maximum load ", self.maxLoad, "No of Axles ", self.NoOfAxles, ",", self.NoOfWheels, "wheels ,")

def main():
    #instantiation and hard-coding of objects
    states1 = ['Victoria', 'New South Wales', 'Queensland', 'Northern Territory']
    states2 = ['Victoria', 'New South Wales', 'Queensland', 'Tasmania','South Australia']
    address1 = {'Street':'178 Bluff Road','City':'Manly','State':'NSW','PostCode':'2101'}
    address2 = {'Street':'10 Downing Street','City':'Brighton','State':'VIC','PostCode':'3188'}
    driver1 = Driver(3313377,'Gladys','Berejkilan','0414566999', address1, states1, 8)
    driver2 = Driver(9877345, 'Boris','Johnson','0414123456', address2, states2, 2)
    car1 = Car('BBJ702','Mazda','CX3',10000, driver1, 'Hatch','Blue','Leather',5)
    car2 = Car('OYO400','Ford','Festive',39785, driver2, 'Sedan', 'Green','Fabric', 4)
    truck1 = Truck('XJBJ882','Kenworth','BigMOther5000',150000, driver1, '40 tonnes', 5, 18 )
    truck2 = Truck('ARC542','Hyundai','iLoad',76520, driver2, '2 tonnes', 2, 4)

    print("driver1 and driver2 demerit points")
    print("\n..............Increase demerit points - Driver 1....................\n")
    driver1.displayDemeritPoints()
    driver1.addDemeritPoints(9)
    driver1.displayDemeritPoints()

    print("\n................Removing demerit points from Driver 1.................")
    driver1.displayDemeritPoints()
    driver1.deleteDemeritPoints(3)
    driver1.displayDemeritPoints()

    print("\n..............Increase demerit points - Driver 2....................\n")
    driver2.displayDemeritPoints()
    driver2.addDemeritPoints(3)
    driver2.displayDemeritPoints()

    print("\n................Removing demerit points from Driver 2.................")
    driver2.displayDemeritPoints()
    driver2.deleteDemeritPoints(3)
    driver2.displayDemeritPoints()

    print("Driver 1 and Driver 2 details...............\n")
    driver1.displayDriverDetails()
    print("\n")
    driver2.displayDriverDetails()

    print("Car1 details......................\n")
    car1.displayVehicleData()
    car1.updateColour('White')
    car1.updateKM(12000)
    print("\nData after updating car1 colour and driven KMs\n")
    car1.displayVehicleData()
    print("\nCar1 General Data\n")
    car1.displayGeneralData()

    print("\nCar2 details.......................\n")
    car2.displayVehicleData()
    car2.updateColour('Purple')
    car2.updateKM(20000)
    print("\nData after updating car2 colour and driven KMs\n")
    car2.displayVehicleData()
    print("\nCar2 General Data\n")
    car2.displayGeneralData()

    print("Truck1 details......................\n")
    truck1.displayVehicleData()
    truck1.updateKM(55000)
    print("\nData after updating truck 1 driven KMs\n")
    truck1.displayVehicleData()
    print("\nTruck1 General Data\n")
    truck1.displayGeneralData()

    print("Truck2 details......................\n")
    truck2.displayVehicleData()
    truck2.updateKM(70000)
    print("\nData after updating truck 2 driven KMs\n")
    truck2.displayVehicleData()
    print("\nTruck2 General Data\n")
    truck2.displayGeneralData()

if __name__ == '__main__':
    main()
    
  

