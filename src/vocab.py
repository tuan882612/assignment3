# tuan trinh 1001885663 tqt5663

from typing import Dict, List
from model import Label

class Word:
    def __init__(self, doc: int, words: List[str], label: int) -> None:
        self.doc = doc
        self.words = words
        self.label = label
        self._process_word()
        
    def _process_word(self) -> None:
        print(f"Processing word: {self.word}")
        
class Vocabulary:
    def __init__(self, data: Dict[str, Dict[str] | str]) -> None:
        self.words: Dict[int, Word] = {}
        self._process_vocab()
        
    def _process_vocab(self) -> None:
        print(f"Processing vocab: {self.word}")
        
    def __repr__(self) -> str:
        return self.word