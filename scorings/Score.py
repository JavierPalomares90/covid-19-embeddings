
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

        self.total_tokens = 0
        self.avg_doc_len = 0
        self.num_docs = 0
        
        self.doc_freq = Counter()
        self.word_freq = Counter()
        self.avg_freq = 0

        self.score = dict()
        self.avg_score = dict()

        self.tags = Counter()
    
    def _get_doc_tokens_and_tags(self,doc_text):
        #TODO: Finish impl
        pass

    def _filter_tags(self,threshold):
        valid_tags = dict()
        for tag,score in self.tags.items():
            if(score > self.num_docs * threshold):
                valid_tags[tag] = score
        self.tags = valid_tags
    
    def index(self,docs):
        """
        Index the documents using the scoring method
        Input: The Paperset lazy loader containing the documents
        """
        num_docs = len(docs)
        self.num_docs = num_docs
        for i in range(num_docs):
            doc = doc[i]
            # get the text
            doc_text = cotools.text(doc)
            tokens,tags = _get_doc_tokens_and_tags(doc_text)

            # update the number of times a token appears
            self.word_freq.update(tokens)

            # update the number of times a token appears in a document
            # use set to get unique tokens only
            self.doc_freq.update(set(tokens))

            if tags is not None:
                # update the list of tags
                self.tags.update(tags.split())
        
        self.total_tokens = sum(self.word_freq.values())

        # number of unique tokens 
        num_tokens  = len(self.word_freq.values())
        # avg frequency per token
        self.avg_freq = self.total_tokens / num_tokens

        # average doc length 
        self.avg_doc_len = self.total_tokens / self.num_docs

        # compute scores using the scoring method
        for token, freq in self.doc_freq.items():
            #TODO: implement compute_score
            self.score[token] = self.compute_score(freq)
        
        self.avg_score[token] = sum(self.score.values()) / len(self.score)

        # filter for tags that appear in at least 1% of documents
        _filter_tags(.009)

    
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
