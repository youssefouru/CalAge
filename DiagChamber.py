from Battery import Battery
from Form import Form as Fr



class DiagChamber:
    def __init__(self, channels=48, *channels_of_form):
        self.occupied_channel = 0
        self.channels = channels

    def register(self, battery):
        ...
