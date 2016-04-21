#! usr/bin/env python3

"""
Remove commas from input data,
turn data into list.
"""

import re, sys, statistics

class BoxAndWhisker():
    """
    Returns values needed for box and whisker plot.
    """

    def __init__(self, data_list, true_median=0, high_median=0,
                 low_median=0, lowest=0, highest=0):
        self.data_list = data_list
        self.true_median = true_median
        self.high_median = high_median
        self.low_median = low_median
        self.lowest = lowest
        self.highest = highest

        # call functions
        self.create_ordered_data()

    def create_ordered_data(self):
        """
        Create ordered list of ints.

        Call find_medians.
        """
        # remove ,s and spaces
        self.data_list = re.split(r'\s*[, ]\s*', self.data_list.strip())
        self.data_list = [int(data) for data in self.data_list]
        self.data_list.sort()

        # call functions
        self.find_medians()
        self.find_min_max()
        return self.data_list

    def find_min_max(self):
        """
        Find min and max of data_list.
        """
        self.lowest, self.highest = min(self.data_list), max(self.data_list)
        return self.lowest, self.highest

    def find_medians(self):
        """
        Find true_median, high_median, low_median.
        """
        # find median
        self.true_median = statistics.median(self.data_list)

        # find low_median, high_median
        # If input list is even

        if len(self.data_list) % 2 == 0:
            low_half = [self.data_list[val] for val in
                        range(len(self.data_list) // 2 - 1)]
            top_half = [self.data_list[val2] for val2 in
                        range(len(self.data_list) // 2 + 1,
                        len(self.data_list))]
            print(low_half, top_half)
            self.low_median = statistics.median(low_half)
            self.high_median = statistics.median(top_half)

        # If input list is odd
        elif len(self.data_list) % 2 != 0:
            low_half = [self.data_list[val] for val in
                        range(len(self.data_list) // 2)]
            top_half = [self.data_list[val] for val in
                        range(len(self.data_list) // 2 + 1,
                        len(self.data_list))]
            print(low_half, top_half, sep='\n')
            self.low_median = statistics.median(low_half)
            self.high_median = statistics.median(top_half)

        return self.true_median, self.low_median, self.high_median

    def get_data(self):
        return self.data_list

    def get_true_median(self):
        return self.true_median

    def get_low_median(self):
        return self.low_median

    def get_high_median(self):
        return self.high_median

    def get_min(self):
        return self.lowest

    def get_max(self):
        return self.highest

    def __str__(self):
        """
        Print String rep of box and whisker info.
        """
        print('All data: ' + str(self.data_list), 'True median: ' +
              str(self.true_median), 'High Median: ' + str(self.high_median),
              'Low Median: ' + str(self.low_median),
              'Lowest: ' + str(self.lowest), 'Highest: ' + str(self.highest),
              sep='\n')


if __name__ == "__main__":
    inp = sys.stdin.read()
    my_data = BoxAndWhisker(inp)
    my_data.__str__()
