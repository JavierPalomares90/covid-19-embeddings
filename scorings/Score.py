
""" 
Base Score class
"""

import math
import pickle
import cotools

from collections import Counter

class Score(object):
    
    def __init__(self,scoring_method):
        super().__init__()

        self.total_tokens = 0
        self.avg_doc_len = 0
        self.num_docs = 0
        
        self.doc_freq = Counter()
        self.word_freq = Counter()
        self.avg_freq = 0

        self.scores = dict()
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
            self.scores[token] = self.compute_score(freq)
        
        self.avg_score[token] = sum(self.scores.values()) / len(self.scores)

        # filter for tags that appear in at least 1% of documents
        _filter_tags(.009)

    
    def weights(self,doc):
        """
        Build the weight vector for the tokens in the document
        Input: 
        """

        weights = list()
        # get the text
        doc_text = cotools.text(doc)
        tokens,_ = _get_doc_tokens_and_tags(doc_text)

        num_tokens = len(tokens)

        for token in tokens:
            # get the frequency and score for the token
            freq = self.word_freq.get(token)
            score = self.scores.get(token)
            if not freq:
                freq = self.avg_freq
            if not score:
                score = self.avg_score
            
            token_weight = self._get_token_weight(freq,score,num_tokens)
            weights.append(token_weight)
        
        # boost weights of tag tokens to equal the largest weight in the list
        if self.tags:
            tags = {token: self.tags[token] for token in tokens if token in self.tags}
            if tags:
                max_weight = max(weights)
                max_tag = max(tags.values())
                weights = [max(max_weight * (tags[tokens[x]] / max_tag), weight)
                           if tokens[x] in tags else weight for x, weight in enumerate(weights)]
                           
        return weights
    
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
