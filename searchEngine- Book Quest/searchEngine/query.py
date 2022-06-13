from unittest import result
import nltk
import json
import gzip
from variable import*
from data import*
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import OrderedDict
from feedback import*


class qProcessing:
    def __init__(self,query):
        self.query = query
    # defining the tokenizer to get tokens from each query
    def tokenizedList(self) :
        tokens = nltk.word_tokenize(self.query)
        return tokens
    #This function will stem the each query 
    def Stemmer(self,tokenList) :
        ps = nltk.stem.PorterStemmer()
        stemmed = []
        for words in tokenList :
            stemmed.append(ps.stem(words))
        #print("all teh token" +stemmed)
        return stemmed 
    def removeStopWord(self,stopWord):
        cleantext = []
        for words in self.query :
            if words not in stopWord:
                cleantext.append(words)
        return cleantext  
    def qDictcreation(self,qList):
        query_vocab = []
        for word in qList.split():
            if word not in query_vocab:
                query_vocab.append(word)
        query_wc = {}
        for word in query_vocab:
            query_wc[word] = qList.lower().split().count(word)
        return query_wc
    def resultConcat(self,result):
        Output =[]
        for doc in result:
            temp = (datatemp.iloc[int(doc[3:])]).values.tolist()
            temp.append(int(doc[3:]))
            Output.append(temp)
        return(Output)
    def retDs (self):
        with gzip.GzipFile(data_dir+'index.dict', 'r') as f:  
            IDXret = json.loads(f.read().decode('utf-8'))
        with gzip.GzipFile(data_dir+'postingList.idx', 'r') as f:		
            POSTret = json.loads(f.read().decode('utf-8'))
        return(IDXret,POSTret)
    def simCalculation(self,res,docNorm,qVal):
        # calculating the cosine similarity
        for valTemp,docNormed in zip(res,docNorm):
            valTemp[0] = valTemp[0]/(docNormed*qVal) if docNormed>0 and qVal>0 else 0
        res.sort(key=lambda x:[-x[0],x[-1]],reverse=False)
        return res
    def read_queryset(self,query):
        query_wc = query
        IDX,POST = self.retDs()
        # loading the values from Inverted Index
        dic = IDX[0]
        docstat = IDX[1]
        po = POST
        docNo = docstat[0]
        docNorm = docstat[1]
        docFreqmax= docstat[2]
        n_docs = len(docNo)
        q_norm = 0
        # final result list initialization
        res = [[0,docTemp] for docTemp in docNo]
        for w in query_wc.keys():
            if w not in dic:
                continue
            postings = po[dic[w][1]]
            df = dic[w][0]
            df = idf(df,n_docs)
            q_f = query_wc[w]
            q_tf_idf = q_f * df
            q_norm += (q_tf_idf**2)
            prev_doc = 0
            for doc_id,freq in zip(postings[::2], postings[1::2]):
                doc_id += prev_doc
                prev_doc = doc_id
                freq_max = docFreqmax[doc_id]
                f = tf(freq,freq_max)
                res[doc_id][0] += (f*df*q_tf_idf)
        qNormval = sqrt(q_norm)
        resTemp = self.simCalculation(res,docNorm,qNormval)
        maxret = 0
        finres =[]
        for it in resTemp:
            if it[0]>0 and maxret<5:
                finres.append(it[-1])
                maxret+=1
                #print("\n")
            else:
                break
        return (finres)
def procStep(tempquery):
    nltk.download('punkt')
    nltk.download('stopwords')
    stopWord = set(stopwords.words('english'))
    qObj = qProcessing(tempquery)
    qObj.query = qObj.tokenizedList()
    query = qObj.removeStopWord(stopWord)
    qList = []
    for w in qObj.Stemmer(query):
        qList.append(w)
    qList = ' '.join(qList)  
    global queryList
    queryList = qList
    query_wc = qObj.qDictcreation(qList)
    result = qObj.read_queryset(query_wc)
    finResult = qObj.resultConcat(result)
    #print(finResult)
    return(finResult)

def resultConcat2(result):
    Output =[]
    for doc in result:
        temp = (datatemp.iloc[int(doc[3:])]).values.tolist()
        temp.append(int(doc[3:]))
        Output.append(temp)
    return(Output)

def getResult(result , relDocList):
    irrelDocListNew = []
    relDocListNew = []
    resNew =[]
    for i in result:
        resNew.append('doc'+str(i))
        if i not in relDocList:
            irrelDocListNew.append('doc'+str(i))
        else:
            relDocListNew.append('doc'+str(i)) 
    modQuery  = modify_query(resNew,relDocListNew,irrelDocListNew,queryList)  
    res1 = (procStep(modQuery))
    if len(relDocListNew)>=2:
        finalRes = resultConcat2(relDocListNew[:2])
    else:
        finalRes = resultConcat2(relDocListNew)
    for i in res1:
        if i[4] not in result:
            finalRes.append(i)
    return finalRes[:5]
    


