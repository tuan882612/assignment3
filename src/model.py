# tuan trinh 1001885663 tqt5663

from typing import Dict, List
from logger import Logger
from enum import Enum

class Label(Enum):
    Zero = '0'
    One = '1'
    
class Word:
    def __init__(self, doc: int, words: List[str], label: Label) -> None:
        self.doc: int = doc
        self.words: List[str] = words
        self.label: Label = label
        
    def __repr__(self) -> str:
        return f"{self.doc} {self.words} {self.label}"

class Vocabulary:
    def __init__(self, data: List[List[str]]) -> None:
        self.words: Dict[int, Word] = {}
        self._process_vocab(data)
        
    def _process_vocab(self, data: List[List[str]]) -> None:
        Logger.info("Processing vocabulary...")
        for row in data:
            doc = int(row[0])
            words = row[1:-1]
            label = Label(row[-1])
            self.words[doc] = Word(doc, words, label)

class Model:
    def __init__(self, data: List[List[str]]) -> None:
        self.vocabs: Vocabulary = Vocabulary(data)
        self.k = 1  # Laplace smoothing factor
        self.word_counts: Dict[Label, Dict[str, int]] = {Label.Zero: {}, Label.One: {}}
        self.label_counts: Dict[Label, int] = {Label.Zero: 0, Label.One: 0}
        self.total_words: int = 0
        self.unique_words: set = set()
        self._train()

    def _train(self) -> None:
        Logger.info("Training model...")
        
        # Count the occurrences of each word for each label
        for word_obj in self.vocabs.words.values():
            label = word_obj.label
            self.label_counts[label] += 1
            for word in word_obj.words:
                self.unique_words.add(word)  # Add word to unique words set
                if word not in self.word_counts[label]:
                    self.word_counts[label][word] = 0
                self.word_counts[label][word] += 1
                self.total_words += 1

        v_size = len(self.unique_words)  # Correct vocabulary size

        # Apply Add-1 Laplace smoothing
        self.probs: Dict[Label, Dict[str, float]] = {Label.Zero: {}, Label.One: {}}
        for label, counts in self.word_counts.items():
            total_count = sum(counts.values())
            v_size = len(self.vocabs.words)
            
            for word in counts:
                self.probs[label][word] = (counts[word] + self.k) / (total_count + v_size * self.k)
                
            # Handle unseen words
            self.probs[label]["_"] = self.k / (total_count + v_size * self.k)

    def predict(self, words: List[str]) -> Label:
        # calculate score for each label
        total_docs = sum(self.label_counts.values())
        scores = {label: self.label_counts[label] / total_docs for label in self.label_counts}
        for word in words:
            for label in scores:
                scores[label] *= self.probs[label].get(word, self.probs[label]["_"])
        
        total_score = sum(scores.values())
        norm_scores = {label: score / total_score for label, score in scores.items()}

        return max(norm_scores, key=norm_scores.get)
