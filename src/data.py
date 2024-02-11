# tuan trinh 1001885663 tqt5663

from typing import List
from logger import Logger

class Data:
    def __init__(self, path: str) -> None:
        if not path:
            Logger.error("Path to data file is required")
            return
        self.collected: List[List[str]] = []
        self._load_data(path)
        
    def _load_data(self, path: str) -> None:
        try:
            with open(path, "r") as f:
                for line in f:
                    self.collected.append(line.split())
        except Exception as e:
            Logger.error("Failed to load data", e, True)
            return
