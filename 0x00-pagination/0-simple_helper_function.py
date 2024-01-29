#!/usr/bin/env python3
'''pagination
'''
def index_range(page, page_size):
    """
    Calculate the start and end indices for a given page and page size.

    Parameters:
    - page: An integer representing the page number (1-indexed).
    - page_size: An integer representing the number of items per page.

    Returns:
    A tuple of two integers (start_index, end_index) representing the range
    of indexes to return in a list for the specified pagination parameters.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
