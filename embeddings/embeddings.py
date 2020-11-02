from cotools import Paperset
from scorings.Score import Score
import pickle

class Embeddings(object):
    """
    The Embeddings class:
        __init__ args:
            pca: the principal components

            scoring_method: The embeddings scoring method to use for the embeddings "bm25", "BERT", etc...

            documents: a Paperset, the lazyloader where to get the papers from

            description:
                build a sentence embedding index from the Paperset 
    """

    def __init__(self,pca,scoring_method,documents):
        #TODO: Map the documents Paperset class to data
        self.scoring_method = scoring_method
        self.documents = documents
        # principal components
        self.pca = pca

    def score(self,data,scoring_method):
        ''' 
        Build the scoring index
        '''
        if self.score is None:
            self.score = _get_scoring(scoring_method)
        
        #TODO: Create score objects that can do bert, tfidf, etc...
    
    def index(self,documents):
        '''
        Build the embedding index
        Args:
            documents: list of documents
        '''
    
    def _get_scoring(self,scoring_method):
        if not scoring_method:
            return None
        score = Score(scoring_method=scoring_method)
        return score
        

    def build_index(self):
        '''
        Build the sentence embedding index
            scoring_method: The embeddings scoring method to use for the embeddings "bm25", "BERT", etc...
        '''
        self.score = self._get_scoring(self.scoring_method)
        self.score.score_data(self.data)
        if self.scoring_method:
            self.score(self.documents,self.scoring_method)

        self.index(self.documents)

    def load(self,path):
        """
        Unpickle the saved Embeddings object
        """
        with open("%s/embedding" % path, "rb") as handle:
            self.__dict__.update(pickle.load(handle))
    
    def save(self,path):
        """
        Pickle the embedding
        """
        with open("%s/embedding" % path, "wb") as handle:
            pickle.dump(self.__dict__, handle, protocol=pickle.HIGHEST_PROTOCOL)
