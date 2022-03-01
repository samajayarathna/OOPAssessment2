import json

class Driver():
    '''declare class variable called maxDemeritPoints to assign max demerit points value'''
    maxDemeritPoints = 12

    def __init__(self,licenceNo, firstName, lastName, mobile,address, licenseState, demeritPoints) :
        ''' initilizating instant variables '''
        self.licenceNo = licenceNo
        self.firstName = firstName
        self.lastName = lastName
        self.mobile = mobile
        self.address = address
        self.licenseState = licenseState
        self.demeritPoints = demeritPoints
    
    def displayDriverDetails(self):
        '''Driver details are displayed '''
        print("The driver", self.firstName, self.lastName, ", has a driver licence number : ", self.licenceNo)
        print("Contact phone number is :", self.mobile)
        print("Driver address is :")
        for x in self.address:
            print(x, ":", self.address[x])
        print("licensed to drive in the following states : ")
        for i in range(len(self.licenseState)):
            print(self.licenseState[i], ":", end=" ")

    def displayDemeritPoints(self):
            '''Driver's demerit points value is displayed'''
            print("\nThe driver", self.firstName, self.lastName ,"has", self.demeritPoints, "x Demerit Points remaining.\n")

    def addDemeritPoints(self,newValue):
        '''Takes in a number newValue, calculates new demerit points '''
        totalDemeritPoints = self.demeritPoints + newValue
        if totalDemeritPoints > self.maxDemeritPoints:
            print("Invalid Entry....\n maximum demerit points : 12 ")
        else:
            self.demeritPoints = totalDemeritPoints

    def deleteDemeritPoints(self, delValue):
        '''Takes in a number delValue, calculates new demerit points'''
        if delValue <= self.demeritPoints:
            self.demeritPoints -= delValue
            if self.demeritPoints <= 3:
                print("Successfully updated the new value")
                print("WARNING MESSAGE: \n License Suspension is imminent \n",self.demeritPoints, "x Demerit Points remaining"  )
        else:  
            print("Invalid Entry....")  

    def writeDriverFile(self):
        '''Writes driver details to the file'''
        textFile =open("driverDetails.txt", "a")  
        textFile.write("\nName : ")
        textFile.write(self.firstName)
        textFile.write(" ")
        textFile.write(self.lastName)
        textFile.write("\nLicense NO: ")
        textFile.write(str(self.licenceNo))
        textFile.write("\nMobile :")
        textFile.write(self.mobile)
        textFile.write("\nDemerit Points : ")
        textFile.write(str(self.demeritPoints))
        textFile.write("\n License States : \n")

        stateList = self.licenseState
        addressList = self.address 
        for element in stateList:
            textFile.write(element + ",")
        textFile.write("\nAddress : ")    
        textFile.write(json.dumps(addressList))
        textFile.close() 

def readDriverFile():
        '''Read and display content of the Driver details file'''
        readFile =open("driverDetails.txt", "r")  
        for x in readFile:
            print(x)

class Vehicle():
    def __init__(self, registrationNo, make, model, kmDriven, objDriver) :
        ''' initilizing instant variables '''
        self.registrationNo = registrationNo
        self.make = make
        self.model = model
        self.kmDriven = kmDriven
        self.obj_driver = objDriver
    
    def displayVehicleData(self):
        print("Vehicle registration number ",self.registrationNo, "is a ", self.make, ". Model is ", self.model, ". Odometer ", self.kmDriven)
        print("The driver of the vehicle is ", self.obj_driver.firstName, self.obj_driver.lastName)
        print("Licence no : ",self.obj_driver.licenceNo)
        print("Demerit Points : " ,self.obj_driver.demeritPoints)
        print("licensed to drive in the following states : ")
        for i in range(len(self.obj_driver.licenseState)):
            print(self.obj_driver.licenseState[i], ":", end=" ")

    def GeneralData(self):
        print("Registration No :", self.registrationNo)
        print("Make : ", self.make)
        print("Model : ", self.model)
        print("Driven KMs : ", self.kmDriven)

    def updateKM(self, newDrivenKm):
        if newDrivenKm >= 0:
            print("\nDriven KMs befor changing : ", self.kmDriven)
            self.kmDriven += newDrivenKm
            print("Successfully updated driven KMs")
            print("New driven KMs : ", self.kmDriven)
        else:
            print("Invalid Entry......\n Negative values are not allwoed")
        
class Car(Vehicle):
    def __init__(self, registrationNo, make, model, kmDriven, objDriver, bodyType, colour, uphostery, NoOfDoors):
        ''' initilizing instant variables '''
        super().__init__(registrationNo, make, model, kmDriven, objDriver)
        self.bodyType = bodyType
        self.colour = colour
        self.uphostery = uphostery
        self.NoOfDoors = NoOfDoors

    def updateColour(self, newColour):
        print("Colour before changing: ",self.colour)
        self.colour = newColour
        print("Successfully updated the colour")
        print("New colour is :", self.colour)


    def displayVehicleData(self):
        ''' '''
        Vehicle.displayVehicleData(self)
        print("\nGeneral data: body type ", self.bodyType, ", colour ", self.colour,"," ,self.uphostery,",", self.NoOfDoors, "doors.")
    
   
        
class Truck(Vehicle):
    def __init__(self, registrationNo, make, model, kmDriven, objDriver, maxLoad, NoOfAxles, NoOfWheels):
        super().__init__(registrationNo, make, model, kmDriven, objDriver)
        self.maxLoad = maxLoad
        self.NoOfAxles = NoOfAxles
        self.NoOfWheels = NoOfWheels

    def displayVehicleData(self):
        Vehicle.displayVehicleData(self)
        print("\nAdditional details: ")
        print("maximum load ", self.maxLoad, " , No of Axles ", self.NoOfAxles, ",", self.NoOfWheels, "wheels ,")

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
    print("\n..............Increase demerit points by 9 - Driver 1....................\n")
    print("Driver 1 demerit points before : ")
    driver1.displayDemeritPoints()
    driver1.addDemeritPoints(9)
    driver1.displayDemeritPoints()
    
    print("\n................Removing demerit points by 3 from Driver 1.................")
    print("Driver 1 demerit points before : ")
    driver1.displayDemeritPoints()
    driver1.deleteDemeritPoints(3)
    print("Driver 1 demerit points after decrementing 3 points :")
    driver1.displayDemeritPoints()
    
    print("\n..............Increase demerit points by 3 - Driver 2....................\n")
    print("Driver 2 demerit points before : ")
    driver2.displayDemeritPoints()
    driver2.addDemeritPoints(3)
    print("Driver 2 demerit points after decrementing 3 points :")
    driver2.displayDemeritPoints()

    print("\n................Removing demerit points by 3 from Driver 2.................")
    print("\nDriver 2 demerit points before : ")
    driver2.displayDemeritPoints()
    driver2.deleteDemeritPoints(3)
    
    print("\nDriver 1 and Driver 2 details...............\n")
    driver1.displayDriverDetails()
    print("\n")
    driver2.displayDriverDetails()
    
    print("\nUpdate vehicle colour and driven KMs........................\n")
    print("Update car 1 colour to White\n")
    car1.updateColour('White')
    print("\nUpdate car 1 driven KMs to 2000")
    car1.updateKM(20000)

    print("\nUpdate car 2 driven KMs to -2000")
    car1.updateKM(-12000)

    print("\nUpdate truck1 driven KMs to 15000")
    car1.updateKM(15000)

    print("\n\nCar1 details......................\n")
    car1.displayVehicleData()

    print("\n\nCar2 details.......................\n")
    car2.displayVehicleData()

    print("\n\nTruck1 details......................\n")
    truck1.displayVehicleData()

    print("\nTruck2 details......................\n")
    truck2.displayVehicleData()

    print("\nCar 1 general data")
    car1.GeneralData()
    print("\nCar 2 general data")
    car2.GeneralData()
    print("\nTruck 1 general data")
    truck1.GeneralData()
    print("\nTruck 2 general data")
    truck2.GeneralData()
    
    print("Writing Driver Details to the driverDetails.txt file..........")
    driver1.writeDriverFile()
    driver2.writeDriverFile()
    print("Successfully updated the Driver details file")

    print("Reading driverDetails.txt file content........................")
    print("\nDriver Details file content")
    readDriverFile()
    
if __name__ == '__main__':
    main()
    
  

