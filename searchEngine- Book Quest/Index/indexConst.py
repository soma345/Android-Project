from data import *
from dictBuid import *
from variable import*
import json
print('reached')
freqMax, normOfdoc, docNo = [],[],[]
dictionary, statOfdoc = {}, [docNo,normOfdoc,freqMax]
postingList, indexStruct = [], [dictionary,statOfdoc]
posting_idx = 0
j = 0
print('reached')
for id,doc in docdict.items():
  max_freq = 1
  docno = id
  for word in doc:
    if word not in dictionary:
        dictionary.update({word:[j,posting_idx]})
        postingList.append([j,1])
        posting_idx+=1 # keeps track of offset in the posting list
    else:
      postings = postingList[dictionary[word][1]]
      if j == postings[-2]:
        postings[-1] += 1
        max_freq = max(max_freq,postings[-1])
      else:
        postings.extend([j,1])
  freqMax.append(max_freq)
  docNo.append(docno)
  j +=1
n_docs = j
normOfdoc = [0 for i in range(n_docs)]
print('reached')
for key in dictionary:
		val = dictionary[key]
		posting = postingList[val[1]]
		dfTemp = len(posting) //2
		val[0] = dfTemp
		idfVal = idf(dfTemp,n_docs)
		#prev_doc = 0
		for i in range(dfTemp):
			doc_id = posting[2*i]
			freq = posting[2*i+1]
			freq_max = freqMax[doc_id]
			f = tf(freq,freq_max)
			normOfdoc[doc_id] += (idfVal*f)**2
normOfdoc = [float("{:.3f}".format(sqrt(val))) for val in normOfdoc]
statOfdoc[1] = normOfdoc
print('reached')
with gzip.GzipFile("index"+'.dict', 'w') as f:
	f.write(json.dumps(indexStruct).encode('utf-8')) 
print('reached')
with gzip.GzipFile("postingList"+'.idx', 'w') as f:
	f.write(json.dumps(postingList).encode('utf-8'))  