# Base class to start the process
from data_capture.data_capture_stats import DataCaptureStats

# Another approach could be to inherit from DataCaptureStats and override the init
class DataCapture:
    """
    This is the Base class to initalize the process
    """
    def __init__(self):
        self.number_list = []

    # Not allowing negatives values
    def add(self, number):
        if number < 0:
            return 'Number must be a positive integer'
        self.number_list.append(number)

    # This method returns an instance of DataCaptureStats, doing some encapsulaption
    def build_stats(self):
        return DataCaptureStats(self.number_list)
