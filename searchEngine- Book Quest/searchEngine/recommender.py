import pandas as pd
import numpy as np
import ast
from data import *
import os


class recommender:

  def reco_sys(list1, list2):

    df = data
    final_list = []
    final_list = list1

    if len(list2) != 0:
      a = [list2[i] for i in range(len(list2)) if list2[i] not in list1]
      for j in a:
        final_list.append(j)

    # Reading the 75 cluster data
    cluster_df = pd.read_csv(data_dir+'cluster75_final.csv')
    cluster_df.drop(columns = ['Unnamed: 0'], inplace = True)

    reco = []


    # clustering based on cluster number of principal list + relevant list
    for book_id in final_list:
      
      cluster_need = cluster_df.iloc[book_id]['cluster']
      
      cluster_within_df = cluster_df.groupby('cluster').get_group(cluster_need) # Getting all the  values corresponding to cluster number

      if -1 not in cluster_within_df['inside'].unique():

        inside_cluster_new = cluster_df.iloc[book_id]['inside']    

        inside_cluster = cluster_within_df.groupby('inside').get_group(inside_cluster_new)
        temp = inside_cluster.drop(book_id)
        reco.append(temp.sample(1).index.tolist())

      else:
        cluster_within_df.drop(book_id, inplace = True) # eliminating the book that is from original list in the current list
        reco.append(cluster_within_df.sample(1).index.tolist()) # Getting random 2 books from the cluster

    recommendation = sum(reco, [])

    final_recommendation = []

    #print("Data Frame :",df[['Title', 'Author', 'Genres', 'Plot']].iloc[recommendation].values.tolist())
    final_recommendation = df[['Title', 'Author', 'Genres', 'Plot']].iloc[recommendation].values.tolist() # Obtaing the details for the recommended books

    iteratr = 0

    # # converting recommended books to the form needed
    for sub_reco in final_recommendation:
      sub_reco.append(recommendation[iteratr])
      iteratr = iteratr+1

    return final_recommendation
