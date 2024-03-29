from datetime import date
from Form import *
from dateutil.relativedelta import relativedelta


class Battery:

    def __init__(self, barcode, seqnum, storage_location, temperature, diagnostic_frequency, form_factor, battery_name,
                 soc):
        """
        Constructor of Battery

        Parameters
        ----------
        :param barcode: str
            The barcode of the battery.
        :param seqnum: str
            The sequence number of the battery.
        :param storage_location: TempChamber
            The temperature chamber where the battery is stored.
        :param temperature: int
            The temperature of the battery.
        :param diagnostic_frequency: int
            The frequency of diagnost of the battery.
        :param form_factor: Form
            The form of the battery.
        :param battery_name: str
            The name of the battery.
        :param soc: int
            The state of charge of the battery.
        """

        self.barcode = barcode
        self.temperature = temperature
        self.diagnostic_frequency = relativedelta(days=diagnostic_frequency)
        self.form_factor = form_factor
        self.active_status = True
        self.under_diag = False
        self.diagnostic_number = 1
        self.battery_name = battery_name
        self.soc = soc
        self.next_diag = date.today()
        self.seqnum = seqnum
        self.storage_location = storage_location
        storage_location.register(self)

    def can_be_diagnosed(self):
        """
        This method is used to determine whether the battery can be diagnosed or not.
        :return: True if today is past the next diagnostics's day
        """
        return date.today() >= self.next_diag

    def generateFile(self):
        return "res/{}_{}_{}".format(self.battery_name, self.barcode, self.diagnostic_number)

    def generateProtocol(self):
        return "res/{}_{}.mpl".format(self.battery_name, self.soc)

    def toString(self):
        print("Battery")
        print("(barcode={}, seqnum={}, storage_location={}, temperature={}, diagnostic_frequency={}, form_factor={}, battery_name={}, soc={})".format(
                self.barcode, self.seqnum, self.storage_location.name, self.temperature, self.diagnostic_frequency.days,
                self.form_factor.name, self.battery_name, self.soc))
