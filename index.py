import argparse
import logging
import os
from embeddings.embeddings import Embeddings
from scorings.ScoringMethod import ScoringMethod
import cotools


'''
Class to build the sentence embedding index
'''

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(lineno)d -- %(message)s")

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--document_path",default="./docs",help="The path to the documents.")
    parser.add_argument("-s","--save_path",default="./embedding",help="Where to save the embeddings to.")
    args = parser.parse_args()
    return args

def build_embeddings(document_path,vector_path):
    embeddings = Embeddings(pca=3,scoring_method=ScoringMethod.BM25,documents=document_path)
    embeddings.build_index()
    return embeddings
    

def main():
    args = get_args()
    document_path = args.document_path
    save_path = args.save_path
    if not os.path.exists(document_path):
        # TODO: Change to automatically get the data using cotools
        logging.error("Did not find documents at {}".format(document_path))
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    logging.debug("Building embedding from documents at {}. Saving embedding at {}".format(document_path,save_path))
    embeddings = build_embeddings(document_path,save_path)
    embeddings.save(save_path)


if __name__ == "__main__":
    main()