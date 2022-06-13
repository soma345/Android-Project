from data import*

# Removing Non-Ascii characters
def _removeNonAscii(s): 
    return "".join(i for i in s if ord(i)<128)
# Tokenizing the words and removing punctuations and stopwords
def plot_tokenizer(w):
    stop = set(list(string.punctuation) + ['``', "'s", "''"] + stopwords.words('english'))
    return [item for item in word_tokenize(w.lower()) if item not in stop]
# Stemming
def stem(x1):
    ps = PorterStemmer()
    stemmed = []
    for a in x1:
        stemmed.append(ps.stem(a))
    return stemmed

#Processing the dataframe to create the dictionary
data['Plot'] = data['Plot'].map(_removeNonAscii)
data['plot_token'] = data['Plot'].map(lambda x: plot_tokenizer(x))
data['plot_token'] = data['plot_token'].apply(lambda x: stem(x)) # this is a dataframe column that has the tokenized and stemmed words
# Converting dataframe column to dictionary
docdict = {}
for i in range(len(data)):
  docdict['doc' + str(i)] = data['plot_token'].iloc[i]
