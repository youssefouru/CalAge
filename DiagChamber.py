from Battery import Battery
from Form import Form as Fr
from Error import Error as Er
from datetime import date
from dateutil.relativedelta import relativedelta


class DiagChamber:
    def __init__(self, channels=48, channels_of_form=None):
        """
        Constructor of the diagnostic chamber.

        Parameters
        ----------
        :param channels: The maximum number of channels.
        :param channels_of_form: This map will link each kind of form to the number of slots dedicated.
        """
        self.occupied_channel = []
        self.channels = channels
        self.channels_of_form = [] if channels_of_form is None else channels_of_form
        self.batteries = {}
        for form in Fr[1::]:
            self.occupied_channel[form] = 0 if form in channels_of_form else -1
            self.batteries[form] = []

    def register_for_diagnostic(self, battery):
        """
        This method will register the battery into diagnostic.

        Parameters
        ----------
        :param battery:  The battery we want to register.
        :return: error code.
        """
        today = date.today()
        if today >= battery.next_diag:
            self.batteries[battery.form_factor].append((battery.barcode, battery.seqnum, battery.diagnostic_number))
            battery.next_diag += relativedelta(months=1)
            battery.diagnostic_number += 1
            return Er.ERR_NONE
        else:
            return Er.ERR_DIAG_TOO_EARLY
