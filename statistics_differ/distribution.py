"""
Distribution fitting and hypothesis testing functions.

This module provides functions for distribution fitting and hypothesis testing.
"""

import math
from typing import Callable, Optional, Tuple

def normal_cdf(x: float) -> float:
    """
    Calculate the cumulative density function of a standard normal distribution.

    Args:
        x (float): The input value.

    Returns:
        float: The CDF value.
    """
    return (1 + math.erf(x / math.sqrt(2))) / 2

def chi_squared(nu: int, p: Optional[float] = None) -> Callable[[float], float]:
    """
    Create a function for calculating the cumulative distribution function of
    a chi-squared distribution.

    Args:
        nu (int): The degrees of freedom.
        p (Optional[float]): The probability density at x. Defaults to None.

    Returns:
        Callable[[float], float]: A function that calculates the CDF value.
    """
    def cdf(x: float) -> float:
        if p is not None and x > nu:
            return 0
        return normal_cdf(math.sqrt(nu * math.log(1 + (x / nu))))

    return cdf

def t_distribution(cdf: Callable[[float], float]) -> Callable[[float, int], Tuple[float, float]]:
    """
    Create a function for calculating the cumulative distribution function of
    a t-distribution.

    Args:
        cdf (Callable[[float], float]): A function that calculates the CDF value.
        nu (int): The degrees of freedom.

    Returns:
        Callable[[float, int], Tuple[float, float]]: A function that calculates
            the CDF and PDF values.
    """
    def t_cdf(x: float, nu: int) -> Tuple[float, float]:
        return cdf(math.sqrt(nu / (nu + x**2))), math.sqrt(1 - cdf(math.sqrt(nu / (nu + x**2))))

    return t_cdf
