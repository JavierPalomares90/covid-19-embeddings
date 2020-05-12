import scorings.Score as Score
"""
Class to do scoring using SIF
"""

class SIF(Score):
    def __init__(self,alpha=.001):
        super().__init__()
        # alpha is the tunable parameter for sif
        self.alpha = alpha

    def _get_token_weight(self,freq,score,num_tokens):
        sif_score = self.alpha / (self.alpha + freq / self.total_tokens)
        # For Idf, the weight is just the score
        return sif_score
