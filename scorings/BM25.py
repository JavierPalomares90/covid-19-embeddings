import scorings.Score as Score
"""
Class to do scoring using BM25
"""

class BM25(Score,k1=0.1,b=0.75):
    def __init__(self):
        super().__init__()
        #k1 and b are tunable parameters
        self.k1=k1
        self.b=b

    def _get_token_weight(self,freq,score,num_tokens):
        # Calculate BM25 score
        k = self.k1 * ((1 - self.b) + self.b * num_tokens / self.avg_doc_len)
        return score * (freq * (self.k1 + 1)) / (freq + k)
