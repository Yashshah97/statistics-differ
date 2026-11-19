"""
Core diff engine logic.

This module provides the core functionality for computing differences between two sets of statistics.
"""

class StatisticsDiffer:
    """
    Compute differences between two sets of statistics.

    Attributes:
        stats1 (list): First set of statistics.
        stats2 (list): Second set of statistics.
    """

    def __init__(self, stats1, stats2):
        self.stats1 = stats1
        self.stats2 = stats2

    def _diff(self, stat1, stat2):
        """
        Compute the difference between two individual statistics.

        Args:
            stat1 (float): First statistic.
            stat2 (float): Second statistic.

        Returns:
            float: Difference between the two statistics.
        """
        return abs(stat1 - stat2)

    def diff(self):
        """
        Compute the differences between all pairs of corresponding statistics.

        Returns:
            list: List of differences, where each difference is a tuple of (index, stat1, stat2, diff).
        """
        return [(i, self.stats1[i], self.stats2[i], self._diff(stat1, stat2)) for i, stat1, stat2 in zip(range(len(self.stats1)), self.stats1, self.stats2)]

def merge(stats1, stats2, merged_stats):
    """
    Perform a three-way merge of statistics.

    Args:
        stats1 (list): First set of statistics.
        stats2 (list): Second set of statistics.
        merged_stats (list): Merged statistics.

    Returns:
        list: List of merged statistics.
    """
    for i, stat1, stat2 in zip(range(len(stats1)), stats1, stats2):
        if merged_stats[i] is None:
            merged_stats[i] = stat1
        elif stat1 != merged_stats[i]:
            raise ValueError("Conflicting values at index {}".format(i))
        else:
            continue

    return merged_stats
