from math import sqrt,log2
from variable import*
def tf(f,augNorm,K=0.5):
	'''Computing tf using augmented frequency method'''
	return (K + (1-K)*(f/augNorm))*(1 + log2(f))
def idf(df,N):
    '''IDF using Smoothed inv. freq.'''
    return log2(N/(1+df)) + 1
def tf_idf(f,valMax,df,docNum,ParamK=0.5):
	# computing the tf-idf 
	return tf(f,valMax,ParamK)*idf(df,docNum)