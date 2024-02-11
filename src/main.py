# tuan trinh 1001885663 tqt5663

from logger import Logger
from data import Data

def main() -> None:
    Logger.info("Starting the application...")
    dt = Data("data/train.txt")
    
if __name__ == "__main__":
    main()
