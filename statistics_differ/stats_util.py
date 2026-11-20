"""
Utility functions for statistical calculations.

This module provides utility functions for common statistical tasks,
such as calculating the mean and standard deviation of a dataset.
"""

import math


def calculate_mean(data):
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The arithmetic mean of the input data.

    Raises:
        ValueError: If the input data is empty.
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    return sum(data) / len(data)


def calculate_std_dev(data, sample=True):
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        data (list): A list of numbers.
        sample (bool): Whether to calculate the population or sample
            standard deviation. Defaults to True.

    Returns:
        float: The standard deviation of the input data.

    Raises:
        ValueError: If the input data is empty.
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / (len(data) - sample * 1)
    return math.sqrt(variance)


def calculate_variance(data, sample=True):
    """
    Calculate the variance of a list of numbers.

    Args:
        data (list): A list of numbers.
        sample (bool): Whether to calculate the population or sample
            standard deviation. Defaults to True.

    Returns:
        float: The variance of the input data.

    Raises:
        ValueError: If the input data is empty.
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - sample * 1)


def calculate_skewness(data):
    """
    Calculate the skewness of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The skewness of the input data.
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    mean = calculate_mean(data)
    variance = calculate_variance(data, sample=False)
    return sum((x - mean) ** 3 for x in data) / (len(data) * math.pow(variance, 1.5))


def calculate_kurtosis(data):
    """
    Calculate the kurtosis of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The kurtosis of the input data.
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    mean = calculate_mean(data)
    variance = calculate_variance(data, sample=False)
    return sum((x - mean) ** 4 for x in data) / (len(data) * math.pow(variance, 2)) - 3
