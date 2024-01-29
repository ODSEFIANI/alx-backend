#!/usr/bin/env python3
'''pagination
'''
import csv
from typing import List


def index_range(page, page_size):
    if not isinstance(page, int) or not isinstance(page_size, int) or page <= 0 or page_size <= 0:
        raise ValueError("Both arguments must be integers greater than 0.")
    
    start_index, end_index = (page - 1) * page_size, page * page_size
    return start_index, end_index


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"


    def __init__(self):
        self.__dataset = None


    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        try:
            start_index, end_index = index_range(page, page_size)
            return self.dataset()[start_index:end_index]
        except ValueError:
            return []

