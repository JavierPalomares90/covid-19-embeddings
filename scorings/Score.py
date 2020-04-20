
""" 
Base Score class
"""

import math
import pickle
import cotools

from collections import Counter

class Score(object):
    
    def __init__(self):
        super().__init__()

        self.total_words = 0
        self.tokens = 0
        self.avg_doc_len = 0
        
        self.doc_freq = Counter()
        self.word_freq = Counter()
        self.avg_freq = 0

        self.idf = dict()
        self.avg_idf = dict()

        self.tags = Counter()
    
    def index(self,docs):
        """
        Index the documents using the scoring method
        Input: The Paperset lazy loader containing the documents
        """
        #TODO: Complete impl
        num_docs = len(docs)
        for i in range(num_docs):
            doc = doc[i]
            # get the text
            doc_text = cotools.text(doc)
            #TODO: Get the tags
        pass
    
    def weights(self,docs):
        """
        Build the weight vector for each token in the input token
        Input: 
        """
        #TODO: Complete impl
        pass
    
    def load(self,path):
        """
        Unpickle the saved Score object
        """
        with open("%s/scoring" % path, "rb") as handle:
            self.__dict__.update(pickle.load(handle))
    
    def save(self,path):
        """
        Pickle the object
        """
        with open("%s/scoring" % path, "wb") as handle:
            pickle.dump(self.__dict__, handle, protocol=pickle.HIGHEST_PROTOCOL)
