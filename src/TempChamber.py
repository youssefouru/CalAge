from src.Error import Error as Er


class TempChamber:
    def __init__(self, temperature):
        """
        Constructor of TempChamber

        Parameters
        ----------
        :param temperature: integer
            The temperature of the chamber
        """
        self.temperature = temperature
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

    def unregister(self, barrcode):
        battery = self.batteries.pop(barrcode)
        return battery
