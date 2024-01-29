#!/usr/bin/env python3
'''pagination
'''
#!/usr/bin/env python3
"""
Contains class with methods to create simple pagination from csv data
"""
import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Reads from csv file and returns the dataset.
        Returns:
            List[List]: The dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Asserts that the value is a positive integer.
        Args:
            value (int): The value to be asserted.
        """
        assert isinstance(value, int) and value > 0

    def get_page(self, page_number: int = 1, items_per_page: int = 10) -> List[List]:
        """
        Returns a page of the dataset.
        Args:
            page_number (int): The page number.
            items_per_page (int): The page size.
        Returns:
            List[List]: The page of the dataset.
        """
        self.assert_positive_integer_type(page_number)
        self.assert_positive_integer_type(items_per_page)
        dataset = self.dataset()
        start_index, end_index = index_range(page_number, items_per_page)
        try:
            page_data = dataset[start_index:end_index]
        except IndexError:
            page_data = []
        return page_data

    def get_hyper(self, page_number: int = 1, items_per_page: int = 10) -> dict:
        """
        Returns a page of the dataset.
        Args:
            page_number (int): The page number.
            items_per_page (int): The page size.
        Returns:
            List[List]: The page of the dataset.
        """
        total_pages = len(self.dataset()) // items_per_page + 1
        page_data = self.get_page(page_number, items_per_page)
        info = {
            "page": page_number,
            "items_per_page": items_per_page if items_per_page <= len(page_data) else len(page_data),
            "total_pages": total_pages,
            "data": page_data,
            "prev_page": page_number - 1 if page_number > 1 else None,
            "next_page": page_number + 1 if page_number + 1 <= total_pages else None
        }
        return info

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start and end index.
    """
    return ((page - 1) * page_size, page * page_size)

