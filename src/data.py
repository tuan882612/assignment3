# tuan trinh 1001885663 tqt5663

from typing import Any
from logger import Logger

class Data:
    def __init__(self, path: str) -> None:
        if not path:
            Logger.error("Path to data file is required")
            return
        self.path: str = path
        self._load_data()
        
    def _load_data(self) -> None:
        try:
            with open(self.path, "r") as f:
                for line in f:
                    print(line.split())
        except Exception as e:
            Logger.error("Failed to load data", e, True)
            return
        Logger.info("Data loaded successfully")
        
    def __repr__(self) -> str:
        pass
