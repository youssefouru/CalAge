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
        self.channels = {x: channels.get(x, 0) for x in Fr[1::]}
        self.loaded_batteries = {x: [] for x in Fr[1::]}
        self.sealed = False
        self.start_date = date.today()
        self.finish_date = self.start_date + self.time

    def load_battery(self, battery):
        """
        This method will load the battery into diagnostic.

        Parameters
        ----------
        :param battery:  The battery we want to register.
        :return: error code.
        """
        if battery.temperature is not self.temperature:
            return Err.ERR_TEMP

        if self.channels[battery.form_factor] <= 0:
            return Err.ERR_NO_SLOTS

        if not battery.can_be_diagnosed():
            return Err.ERR_DIAG_TOO_EARLY

        self.loaded_batteries[battery.form_factor].append(battery)
        self.channels[battery.form_factor] -= 1
        return Err.ERR_NONE

    def start_diagnostic(self):
        self.sealed = True
        for shape in Fr[1::]:
            for battery in self.loaded_batteries[shape]:
                battery.under_diag = True
        self.finish_date = self.start_date + self.time

    def isFinished(self):
        return date.today() >= self.finish_date

    def unload(self, aborted=False):
        if not (self.isFinished() or aborted):
            return Err.ERR_SEALED_CHAMBER
        self.sealed = False
        for shape in Fr[1::]:
            for battery in self.loaded_batteries[shape]:
                self.channels[shape] += 1 if not aborted else 0
                battery.under_diag = False
                battery.next_diag = date.today() if not aborted else date.today() + battery.diagnostic_frequency
                battery.diagnostic_number += 0 if not aborted else 1
            self.loaded_batteries[shape] = []
