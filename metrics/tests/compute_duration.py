import metrics
import numpy as np


def test_compute_duration():
    urange = np.arange(0, 1.01, 0.01)
    # converting data to a numpy.ndarray
    data = np.reshape(urange, (urange.shape[0], 1))
    result = metrics.compute_duration(data, 100)
    assert result == 1
