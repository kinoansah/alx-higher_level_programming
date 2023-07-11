#!/usr/bin/python3
"""My List Module a custom list type."""


class MyList(list):
    """Custom list type that add the functionality to print list sorted."""

    def print_sorted(self):

        """Print the list in ascending(sorted) order."""
        print(sorted(self))
