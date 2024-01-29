#!/usr/bin/env python3
'''pagination
'''

#!/usr/bin/env python3
"""
1. Simple pagination
"""

import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page_number: int = 1, items_per_page: int = 10) -> List[List]:
        """
        Finds the correct indexes to paginate dataset.
        """
        assert isinstance(page_number, int)
        assert isinstance(items_per_page, int)
        assert page_number > 0
        assert items_per_page > 0
        csv_size = len(self.dataset())
        start_index, end_index = index_range(page_number, items_per_page)
        end_index = min(end_index, csv_size)
        if start_index >= csv_size:
            return []
        return self.dataset()[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start and end index.
    """
    return ((page - 1) * page_size, page * page_size)

