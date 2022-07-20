import Form
from Battery import Battery
from Form import *
from TempChamber import TempChamber


class Database:

    def __init__(self):
        self.tempChambers = {}
        self.batteries = {}
        self.diagChambers = {}
        self.numBat = 0
        self.numTemp = 0
        self.numDiag = 0

    def register_component(self, comp):
        head = comp[0]
        returnValue = head + " "
        if head == "-b":
            barcode = comp[1]
            seqnum = comp[2]
            storage_location = self.tempChambers[int(comp[3])]
            temperature = int(comp[4])
            diagnostic_frequency = int(comp[5])
            form_factor = Form.translator[comp[6]]
            battery_name = comp[7]
            soc = int(comp[8])
            battery = Battery(barcode, seqnum, storage_location, temperature, diagnostic_frequency, form_factor,
                              battery_name, soc)
            self.batteries[self.numBat] = battery
            returnValue += self.numBat
            self.numBat += 1
        elif head == "-tc":
            temperature = int(comp[1])
            tempChamber = TempChamber(temperature)
            self.tempChambers[self.numTemp] = tempChamber
            returnValue += self.numTemp
            self.numTemp += 1
        elif head == "-dc":
            ...

        return returnValue

    def get(self, comp, number):
        if comp == "-b":
            return self.batteries.get(number, None)
        elif comp == "-tc":
            return self.tempChambers.get(number, None)
        elif comp == "-dc":
            return self.diagChambers.get(number, None)
        else:
            return None
