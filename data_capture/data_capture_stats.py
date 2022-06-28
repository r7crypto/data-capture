# Data capture stats class

class DataCaptureStats:
    """
    This is the core processing class for the data capture
    """

    # Initializing this data structures as protected ones
    _number_list = []
    _number_dict = {}
    _less_dict = {}
    _between_dict = {}
    _greater_dict = {}

    # We are initializing with the number list to maintain the object's state
    def __init__(self, number_list):
        self._number_list = number_list
        index = 0
        for number in number_list:
            value = number
            if len(self._number_dict) > 0 and number in self._number_dict:
                number = str(number) + '+' + str(index)
            self._number_dict[number] = value
        index += index

        # In this for loops, we are evaluating the repeated values as strings, due to dicts can't have repeated keys
        for k, v in self._number_dict.items():
            if not isinstance(k, str):
                self._less_dict[k] = {key: value for key, value in self._number_dict.items() if value < k}
            else:
                self._less_dict[k] = v

        for k, v in self._number_dict.items():
            if not isinstance(k, str):
                self._greater_dict[k] = {key: value for key, value in self._number_dict.items() if value > k}
            else:
                self._greater_dict[k] = v

    # Main methods for the class
    def less(self, number):
        return len(self._less_dict[number])

    def greater(self, number):
        return len(self._greater_dict[number])

    def between(self, init_number, final_number):
        return len(self._number_list[init_number:final_number]) + 2
