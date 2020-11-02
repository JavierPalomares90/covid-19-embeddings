import scorings.ScoringMethod as ScoringMethod
import scorings.TFIDF as TFIDF
import scorings.BM25 as BM25
import scorings.SIF as SIF
import scorings.BERT as BERT

class Score(object):
    '''
    Class to represent the scoring method used for the sentence embedding
    '''

    def __init__(self,scoring_method):
        self.data = data
        self.scoring_method = scoring_method
        self.scoring = None
        super().__init__()
    
    def _get_scoring(self):
        scoring = None
        if self.scoring_method is ScoringMethod.TFIDF:
            scoring =  TFIDF()
        elif self.scoring_method is ScoringMethod.BM25:
            scoring = BM25()
        elif self.scoring_method is ScoringMethod.SIF:
            scoring = SIF()
        elif self.scoring_method is ScoringMethod.BERT:
            scoring = BERT()
        return scoring
        
    
    def build_scoring_index(self,data):
        if not self.scoring:
            self.scoring = _get_scoring()
        
        
