from collections import defaultdict
from math import log10
from turtle import clear
from dictBuid import*
from expand import*

def modify_query(result,relDocList,irrelDocList, query, alpha=0.75, beta=0.15):
    N = len(result)
    reVec, irreVec, docFreq = [], [], defaultdict(set)
    # Count term frequency and document frequency for each term in each document
    for i in result:
        vecList = defaultdict(int)
        terms = docdict[i]       # terms: all terms in a document
        for term in terms:
            docFreq[term].add(i)
            vecList[term] += 1
        if i in relDocList:
            reVec.append(vecList)  
        else:
            irreVec.append(vecList)
   
    for vector in reVec + irreVec:
        for term in vector:
            tf = log10(1+vector[term])
            idf = log10(float(N)/len(docFreq[term]))
            vector[term] = tf  * idf * 10000
    # Rocchio Algorithm
    DR, DNR = len(reVec), len(irreVec)
    vectorMod = defaultdict(float)
    for vector in reVec:
        for term in vector:
            vectorMod[term] += vector[term] * alpha / DR 
    for vector in irreVec:
        for term in vector:
            vectorMod[term] = max(0, vectorMod[term] - vector[term] * beta / DNR)
    query = expQuery(vectorMod,query)
    #print(query)
    return (query)


