import pandas as pd
import numpy as np
import math
import ast
from collections import defaultdict
import matplotlib.pyplot as plt
import string
from nltk.stem import PorterStemmer
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk
import gzip
import os
full_path = os.path.realpath(__file__)
file_path = os.path.dirname(full_path)
data_dir = str(file_path) + '\\'


def stopword_handling():
  my_file = open(data_dir + 'stopwords.txt', 'r')
  stopwords = my_file.readlines()
  stopwords = list(map(str.strip, stopwords))

def csv_to_dataframe(data_dir):
  data = pd.read_csv(data_dir + 'booksummaries.txt', sep = "\t")
  data.columns = ['Wikipedia_ID', 'Freebase_ID', 'Title', 'Author', 'Publication_Date', 'Genres', 'Plot']
  datatemp = data.copy(deep=True)
  data.drop(labels = ['Wikipedia_ID', 'Freebase_ID', 'Publication_Date'], inplace = True, axis = 1)
  datatemp.drop(labels = ['Wikipedia_ID',  'Freebase_ID', 'Publication_Date'], inplace = True, axis = 1)
  return data, datatemp

def clean_data(data, datatemp):
  data = data.dropna(subset = ['Genres'])
  datatemp = datatemp.dropna(subset = ['Genres'])
  data.reset_index(drop = True, inplace = True)
  datatemp.reset_index(drop = True, inplace = True)
  return data, datatemp

def genre_to_dict(data, datatemp):
  data['Genres'] = data['Genres'].map(lambda x: ast.literal_eval(x))
  data['Genres'] = data['Genres'].map(lambda x: list(x.values()))

  datatemp['Genres'] = datatemp['Genres'].map(lambda x: ast.literal_eval(x))
  datatemp['Genres'] = datatemp['Genres'].map(lambda x: list(x.values()))
  return data, datatemp

data, datatemp = csv_to_dataframe(data_dir)
data, datatemp = clean_data(data, datatemp)
data, datatemp = genre_to_dict(data, datatemp)

