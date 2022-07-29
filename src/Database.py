import Form
from DiagChamber import DiagChamber
from Form import translator
from TempChamber import TempChamber
from Battery import Battery
from Request import Request as Rq
import pickle


class Database:

    def __init__(self):
        self.tempChambers = {}
        self.batteries = {}
        self.diagChambers = {}
        self.numBat = 0
        self.numTemp = 0
        self.numDiag = 0
        self.name = "res/database.pickle"

    def register_component(self, head, *params):
        if head == Rq.REGISTER_BATTERY:
            barcode = params[0]
            seqnum = params[1]
            storage_location = self.tempChambers.get(int(params[2]), None)
            temperature = int(params[3])
            diagnostic_frequency = int(params[4])
            form_factor = Form.translator.get(params[5], None)
            battery_name = params[6]
            soc = int(params[7])
            battery = Battery(barcode, seqnum, storage_location, temperature, diagnostic_frequency, form_factor,
                              battery_name, soc)
            self.batteries[self.numBat] = battery
            self.numBat += 1
        elif head == Rq.REGISTER_TEMPERATURE_CHAMBER:
            temperature = int(params[0])
            tempChamber = TempChamber(temperature)
            self.tempChambers[self.numTemp] = tempChamber
            self.numTemp += 1
        elif head == Rq.REGISTER_DIAGNOSTIC_CHAMBER:
            temp = int(params[0])
            time = int(params[1])
            channels = [int(x) for x in params[2].split(",")]
            self.diagChambers[self.numDiag] = DiagChamber(temp, time, channels)
            self.numDiag += 1

    def get(self, ty, number):
        if ty == "-b":
            return self.batteries.get(number, None)
        elif ty == "-tc":
            return self.tempChambers.get(number, None)
        elif ty == "-dc":
            return self.diagChambers.get(number, None)
        else:
            return None

    def save(self):
        with open(self.name, 'wb') as my_file:
            pickle.dump(self.batteries, my_file)
            pickle.dump(self.tempChambers, my_file)
            pickle.dump(self.diagChambers, my_file)
            my_file.close()

    def load(self):
        with open(self.name, 'rb') as my_file:
            self.batteries = pickle.load(my_file)
            self.tempChambers = pickle.load(my_file)
            self.diagChambers = pickle.load(my_file)
            my_file.close()

    def needToBeDiagnosed(self):
        b = []
        for chamber in self.tempChambers:
            for (barcode, battery) in chamber.batteries.item():
                if battery.can_be_diagnosed():
                    b.append(battery)

        return b

