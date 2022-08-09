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

    def register_component(self, head, params):
        match head:
            case "-b":
                barcode = params[0]
                seqnum = params[1]
                storage_location = self.tempChambers.get(params[2], None)
                temperature = int(params[3])
                diagnostic_frequency = int(params[4])
                form_factor = Form.translator.get(params[5], None)
                battery_name = params[6]
                soc = int(params[7])
                battery = Battery(barcode, seqnum, storage_location, temperature, diagnostic_frequency, form_factor,
                                  battery_name, soc)
                self.batteries[self.numBat] = battery
                self.numBat += 1
            case "-tc":
                temperature = int(params[0])
                name = params[1]
                tempChamber = TempChamber(temperature, name)
                self.tempChambers[name] = tempChamber
                self.numTemp += 1
            case "-dc":
                temp = int(params[0])
                time = int(params[1])
                channels = [int(x) for x in params[2].split(",")]
                self.diagChambers[self.numDiag] = DiagChamber(temp, time, channels)
                self.numDiag += 1
            case other:
                pass

    def get(self, ty, number):
        match ty:
            case "-b":
                return self.batteries.get(number, None)
            case "-tc":
                return self.tempChambers.get(number, None)
            case "-dc":
                return self.diagChambers.get(number, None)
            case other:
                return None

    def remove(self, head, id):
        match head:
            case "-b":
                self.batteries.pop(int(id), None)
                self.numBat -= 1
            case "-tc":
                self.tempChambers.pop(id, None)
                self.numTemp -= 1
            case "-dc":
                self.diagChambers.pop(int(id), None)
                self.numDiag -= 1

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

    def toString(self):

        for (name, tc) in self.tempChambers.items():
            tc.toString()

        for (number, dc) in self.diagChambers.items():
            print(dc)
