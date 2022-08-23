from Form import Form as Fr
from Error import Error as Err
from datetime import date
from dateutil.relativedelta import relativedelta
import numpy as np


class DiagChamber:

    def __init__(self, temperature, time=7, channels=None):
        """
        Constructor of the diagnostic chamber.

        Parameters
        ----------
        :param temperature: int
         The temperature of the chamber.
        :param time: timerelativedelta
            The diagnostic time.
        :param channels : {Form : int }
            A map representing the maximum slots per form factor of batteries
        """
        self.temperature = temperature
        self.time = relativedelta(days=time)
        self.channels = {Fr(i): channels[i] for i in range(0, len(channels))}
        self.loaded_batteries = {}
        self.sealed = False
        self.finish_date = date.today() + self.time

    def load_battery(self, battery, channel):
        """
        This method will load the battery into diagnostic.

        Parameters
        ----------
        :param channel: The channel assigned to the battery
        :param battery:  The battery we want to register.
        :return: error code.
        """
        if self.channels[battery.form_factor] <= 0:
            return Err.ERR_NO_SLOTS
        if battery.under_diag:
            return Err.ERR_ILLEGAL_ARGUMENT

        self.loaded_batteries[channel] = battery
        self.channels[battery.form_factor] -= 1
        return Err.ERR_NONE

    def start_diagnostic(self):
        self.finish_date = date.today() + self.time
        self.sealed = True
        for (slot, battery) in self.loaded_batteries.items():
            battery.under_diag = True

    def isFinished(self):
        return date.today() >= self.finish_date

    def unload(self, aborted=False):
        if not (self.isFinished() or aborted):
            print("Unloading too early")
            return Err.ERR_SEALED_CHAMBER
        copy = self.loaded_batteries
        for (slot, battery) in self.loaded_batteries.items():
            battery.under_diag = False
            if not aborted:
                battery.diagnostic_number += 1
                battery.next_diag = date.today() + battery.diagnostic_frequency
            if aborted:
                battery.next_diag = date.today()
            self.channels[battery.form_factor] += 1

        self.loaded_batteries = {}
        self.sealed = False
        for (channel, battery) in copy.items():
            print("{}:{}->{}".format(channel, battery.barcode, battery.storage_location.name))

    def advance_time(self, time=1):
        """
        This for prototyping purposes
        :param time:
        :return:
        """
        self.finish_date -= relativedelta(days=time)

    def toString(self):
        print("Diagnostic Chamber:")
        numBat = len(self.loaded_batteries)
        print("Temperature={}, Time={} days, Batteries={}".format(self.temperature, self.time.days, numBat))
        for (channel, battery) in self.loaded_batteries.items():
            print("Channel {}:".format(channel))
            battery.toString()
