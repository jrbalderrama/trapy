import metrics
import numpy as np
import os
from os import path
from unittest import TestCase


class TestComputeDuration(TestCase):
    def setUp(self):
        cwd = os.getcwd()
        filename = path.join(cwd, "data", "data.csv")
        # obtain raw data from file
        self.data = np.loadtxt(filename, delimiter=',')
        # converting raw data to a numpy.ndarray
        self.data = np.reshape(self.data, (self.data.shape[0], 1))

    def test_compute_duration(self):
        expected = 1
        result = metrics.compute_duration(self.data, 100)
        self.assertEqual(result, expected)
