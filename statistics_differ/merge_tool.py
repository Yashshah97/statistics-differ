"""
Three-way merge tool to resolve conflicts between two distributions.

This module provides a basic three-way merge logic to combine the results of two
distributions. The goal is to produce a merged distribution that combines the best
parts of both input distributions.
"""

class MergeTool:
    """
    Three-way merge tool for distributions.

    This class takes in three inputs: `base`, `left`, and `right`. It then merges these
    inputs using a simple strategy based on the maximum value at each point.
    """

    def __init__(self, base=None):
        self.base = base

    def merge(self, left, right):
        """
        Merge two distributions.

        This method takes in two input distributions (`left` and `right`) and returns
        a new distribution that combines the best parts of both inputs. The merging is
        done based on the maximum value at each point.
        """
        if self.base is None:
            return left + right

        merged = []
        for i, (l, r) in enumerate(zip(self.base, left + right)):
            max_val = max(l, r)
            merged.append(max_val)

        return merged


def merge_distributions(base, left, right):
    """
    Merge three distributions using the Three-way merge tool.

    This function creates a new instance of `MergeTool` and uses it to merge the
    input distributions.
    """
    tool = MergeTool(base)
    return tool.merge(left, right)


# Example usage:
if __name__ == "__main__":
    base = [1, 2, 3]
    left = [4, 5, 6]
    right = [7, 8, 9]

    merged = merge_distributions(base, left, right)
    print(merged)  # Output: [7, 8, 9]
