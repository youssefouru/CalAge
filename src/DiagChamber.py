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
        return date.today() == self.finish_date

    def unload(self, aborted=False):
        if self.sealed or (not aborted):
            return Err.ERR_SEALED_CHAMBER
        for (shape, batteries) in self.loaded_batteries.items():
            for battery in batteries:
                battery.under_diag = False
                battery.next_diag = date.today() if not aborted else date.today() + battery.diagnostic_frequency
                battery.diagnostic_number += 0 if aborted else 1
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
