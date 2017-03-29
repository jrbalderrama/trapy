import metrics
import numpy as np
from os import path
import os


def read_data():
    cwd = os.getcwd()
    filename = path.join(cwd, "data", "data.csv")
    # obtain raw data from file
    data = np.loadtxt(filename, delimiter=',')
    # converting raw data to a numpy.ndarray
    return np.reshape(data, (data.shape[0], 1))


def test_compute_duration():
    data = read_data()
    result = metrics.compute_duration(data, 100)
    assert result == 1
