from __future__ import division


def compute_duration(data, frequency):
    """ Compute the duration of the overall task.    
   
    :param data: kinematic rotation matrix
    :type data: numpy.ndarray
    :param frequency: acquisition frequency (Hz)
    :return: total duration of the task
    """
    # all rows but one of the first column
    return (data[1:, 0].shape[0]) / frequency
