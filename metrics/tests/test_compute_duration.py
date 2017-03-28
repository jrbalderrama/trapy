from unittest import TestCase
import metrics
# alternatively:
# from metrics import compute_duration
import numpy as np

import os
from os import path


class TestComputeDuration(TestCase):
    def setUp(self):
        cwd = os.getcwd()
        filename = path.join(cwd, "data", "data.csv")
        self.data = np.loadtxt(filename, delimiter=',')
        # converting dummy data to a numpy.ndarray
        self.data = np.reshape(self.data, (self.data.shape[0], 1))

    def test_compute_duration(self):
        frequency = 0.01
        result = metrics.compute_duration(self.data, frequency)
        self.assertEqual(result, 1)
