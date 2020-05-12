import scorings.Score as Score
"""
Class to do scoring using TFIDF
"""

class TFIDF(Score):
    def __init__(self):
        super().__init__()

    def _get_token_weight(self,freq,score,num_tokens):
        # For Idf, the weight is just the score
        return score
