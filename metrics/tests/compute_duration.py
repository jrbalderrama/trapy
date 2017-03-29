import metrics
import numpy as np


def test_compute_duration():
    data = np.linspace(0, 1, 101)
    data = np.reshape(data, (data.shape[0], 1))
    result = metrics.compute_duration(data, 100)
    assert result == 1
