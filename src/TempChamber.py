from src.Error import Error as Er


class TempChamber:
    def __init__(self, temperature, name):
        """
        Constructor of TempChamber

        Parameters
        ----------
        :param temperature: integer
            The temperature of the chamber
        """
        self.temperature = temperature
        self.name = name
        self.batteries = {}

    def register(self, battery):
        """
        This method register a battery to the chamber.

        Parameters
        ----------
        :param battery: Battery
            The battery we want to register
        :return: int
            an error code to tell us if the battery has been registered
        """
        if battery.temperature == self.temperature:
            self.batteries[battery.barcode] = battery
            return Er.ERR_NONE
        else:
            return Er.ERR_TEMP

    def unregister(self, barcode):
        battery = self.batteries.pop(barcode)
        return battery

    def check_diag(self):
        batteries = []
        for (barcode, battery) in self.batteries.items():
            if battery.can_be_diagnosed():
                batteries.append(barcode)
        return batteries

    def toString(self):
        print("Temperature Chamber {}".format(self.name))
        for (barcode, battery) in self.batteries.items():
            battery.toString()
