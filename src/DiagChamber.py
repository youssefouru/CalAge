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
        self.loaded_batteries = {x: [] for x in Fr}
        self.sealed = False
        self.finish_date = date.today() + self.time

    def load_battery(self, battery):
        """
        This method will load the battery into diagnostic.

        Parameters
        ----------
        :param battery:  The battery we want to register.
        :return: error code.
        """
        if self.channels[battery.form_factor] <= 0:
            return Err.ERR_NO_SLOTS
        if battery.under_diag:
            return Err.ERR_ILLEGAL_ARGUMENT

        self.loaded_batteries[battery.form_factor].append(battery)
        self.channels[battery.form_factor] -= 1
        return Err.ERR_NONE

    def start_diagnostic(self):
        self.finish_date = date.today() + self.time
        self.sealed = True
        for (shape, batteries) in self.loaded_batteries.items():
            for battery in batteries:
                battery.under_diag = True

    def isFinished(self):
        return date.today() >= self.finish_date

    def unload(self, aborted=False):
        if self.sealed or (not aborted):
            return Err.ERR_SEALED_CHAMBER
        print("unloading")
        for (shape, batteries) in self.loaded_batteries.items():
            for battery in batteries:
                battery.under_diag = False
                if not aborted:
                    battery.diagnostic_number += 1
                    battery.next_diag = date.today() + battery.diagnostic_frequency
                if aborted:
                    battery.next_diag = date.today()
            self.channels[shape] += len(batteries)
            self.loaded_batteries[shape] = []
        self.sealed = False

    def advance_time(self, time=1):
        """
        This for prototyping purposes
        :param time:
        :return:
        """
        self.finish_date -= relativedelta(days=time)
        print(self.finish_date)

    def toString(self):
        print("Diagnostic Chamber:")
        numBat = 0
        for (shape, batteries) in self.loaded_batteries.items():
            numBat += len(batteries)
        print("Temperature={}, Time={} days, Batteries={}".format(self.temperature, self.time.days, numBat))
