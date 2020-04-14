from cotools import Paperset

class Embeddings:
    """
    The Embeddings class:
        __init__ args:
            scoring_method: The embeddings scoring method to use for the embeddings "bm25", "BERT", etc...


            description:
                build a sentence embedding index from the Paperset 

    """

    def __init__(self,pca,scoring_method=None):
        self.scoring_method = scoring_method
        self.pca = pca

class EmbeddingIndex:
    """
    The EmbeddingIndex class:
        __init__ args:
            data: a Paperset, the lazyloader where to get the papers from

            description:
                build a sentence embedding index from the Paperset 
    """
    def __init__(self, data):
        self.data = data

    def score(self,data,scoring_method):
        ''' 
        Build the scoring index
        '''
        #TODO: Create score objects that can do bert, tfidf, etc...
    
    def index(self,data):
        '''
        Index the data
        '''




    def build_index(self,pca,scoring_method=None):
        '''
        Build the setence embedding index
            scoring_method: The embeddings scoring method to use for the embeddings "bm25", "BERT", etc...
        '''
        if scoring_method:
            score(self.data,scoring_method)

        index(self.data)