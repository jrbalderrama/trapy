from __future__ import division


def compute_duration(data, frequency):
    """ Compute the duration of the overall task.    
   
    :param data: kinematic rotation matrix
    :type data: numpy.ndarray
    :param frequency: acquisition frequency
    :return: total duration of the task
    """

    return (data[1:, 0].shape[0]) * frequency


