from datetime import date
from Error import Error as Err
from Form import *


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
        self.seqnum = seqnum
        self.storage_location = storage_location
        self.temperature = temperature
        self.diagnostic_frequency = diagnostic_frequency
        self.form_factor = form_factor
        self.active_status = True
        self.under_diag = False
        self.diagnostic_number = 1
        self.battery_name = battery_name
        self.soc = soc
        self.next_diag = date.today()

    def can_be_diagnosed(self):
        """
        This method is used to determine whether the battery can be diagnosed or not.
        :return: True if today is past the next diagnostics's day
        """
        return date.today() >= self.next_diag

    def generateFile(self):
        return "{}_{}_{}.txt".format(self.barcode, self.seqnum, self.diagnostic_number)

    def generateProtocol(self):
        return "{}_{}.txt".format(translator(self.form_factor), self.soc)
