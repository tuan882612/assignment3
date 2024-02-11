# tuan trinh 1001885663 tqt5663

from logger import Logger
from data import Data
from model import Model, Vocabulary

def main() -> None:
    data = Data("data/train.txt") 
    model = Model(data.collected)

    test_data = Data("data/test.txt").collected[0][1:-1]
    predicted_label = model.predict(test_data)
    Logger.info(f"Predicted label: {predicted_label}")

    
if __name__ == "__main__":
    main()
