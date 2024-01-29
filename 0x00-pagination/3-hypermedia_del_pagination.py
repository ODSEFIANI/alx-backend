#!/usr/bin/env python3
"""
3. Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Sclass derver
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """dunction
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """indexing
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """
        gethyper
        """
        dt = []
        folowing = index + page_size
        for idx in range(index, index + page_size):
            if not self.indexed_dataset().get(idx):
                folowing += 1
            dt.append(self.indexed_dataset()[idx])
        rst = {
                  'data': dt,
                  'index': index,
                  'next_index': folowing,
                  'page_size': page_size
                  }
        return rst
