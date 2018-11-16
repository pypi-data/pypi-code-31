#--------------------------------------------------------
# Feature Selectors For Unsupervised Learning
# with TFIDF Vectors
# 2017.11.3 Hans roh
#--------------------------------------------------------

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import VarianceThreshold, SelectKBest, SelectPercentile, chi2
from sklearn.metrics.pairwise import cosine_similarity
import sklearn.cluster as cl
import numpy as np
import pandas as pd
import pickle
import sys, os
import time
from pprint import pprint as pp

class Variant:		
	def __init__ (self, samples):
		self.samples = samples
		
	def select (self, top_n = 6000, min_tfidf = 0.1, reverse = False):	
		D = self.samples.matrix.toarray ()
		
		scores = np.var (D, axis = 0)
		# shape check
		assert len (scores) == len (D [0])
		
		ids = np.argsort(scores)[::-1]
		if reverse:			
			topn_ids = ids [-top_n:]
		else:
			topn_ids = ids [:top_n]
		
		top_feats = [(self.samples.names [i], i, scores [i]) for i in topn_ids]
		print ("{} features was selected".format (len (top_feats)))
		return top_feats
		

class ClusterMaxPool (Variant):	
	def select (self, top_n = 6000, min_tfidf = 0.1, reverse = False):	
		# https://stats.stackexchange.com/questions/266220/tfidf-for-feature-selection-method-for-unlabeled-text-documents
		D = self.samples.matrix.toarray ()
		covar = np.cov (D, rowvar = False)	
		k_means = cl.KMeans(init='k-means++', n_clusters = top_n, n_init=10)
		k_means.fit (covar)
		
		CS = {}
		for i, c in enumerate (k_means.labels_):
			if c not in CS:
				CS [c] = []			
			CS [c].append (self.samples.names [i])
		pp (CS)


