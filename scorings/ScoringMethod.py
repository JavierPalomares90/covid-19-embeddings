from enum import Enum

class ScoringMethod(Enum):
    TFIDF = "tfidf"
    BM25 = "bm25"
    SIF = "sif"
    BERT = "bert"
