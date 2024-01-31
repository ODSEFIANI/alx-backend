#!/usr/bin/env python3
'''pagination
'''
import csv
from typing import List, Tuple, Dict
import math


class Server:
    """class
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """dunction
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page_number: int = 1, items_per_page: int = 10) -> List[List]:
    """function
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

    def get_hyper(self, page_number: int = 1, items_per_page: int = 10) -> Dict[str, any]:
    """function
    """
        assert isinstance(page_number, int)
        assert isinstance(items_per_page, int)
        assert page_number > 0
        assert items_per_page > 0

        page_data = self.get_page(page_number, items_per_page)
        csv_size = len(self.dataset())
        total_pages = math.ceil(csv_size / items_per_page)

        next_page = page_number + 1 if (page_number * items_per_page) < csv_size else None
        prev_page = page_number - 1 if page_number > 1 else None

        return {
            "page_size": len(page_data),
            "page": page_number,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function
    """
    return ((page - 1) * page_size, page * page_size)
