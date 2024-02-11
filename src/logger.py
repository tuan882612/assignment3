# tuan trinh 1001885663 tqt5663

import datetime
import traceback

class Logger:
    @classmethod
    def info(cls, message: str) -> None:
        print(f"{datetime.datetime.now()} - INFO - {message}")
        
    @classmethod
    def error(cls, message: str, err: Exception = None, verbose: bool = False) -> None:
        if verbose and err:
            print(f"{datetime.datetime.now()} - ERROR - {message}")
            print(f"Exception: {str(err)}\nTrackback: {traceback.format_exc()}")
            return
        print(f"{datetime.datetime.now()} - ERROR - {message}")