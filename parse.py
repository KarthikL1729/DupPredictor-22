import csv 
import html2text
import gensim
from gensim.utils import tokenize
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.porter import PorterStemmer

def parse(filename):

    with open(filename, 'r') as f:
        data = csv.reader(f)
        data = list(data)

    return data

dat = parse('QueryResultsSU.csv')
fields = dat[0]
dat = dat[1:]

h = html2text.HTML2Text()

h.ignore_links = True
# Links ignored
stopwords = gensim.parsing.preprocessing.STOPWORDS
with open('parsed_SU.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    for i in dat:

        i[0] = h.handle(i[0])                                                           # Converting html to text
        i[0] = list(tokenize(i[0], lowercase=True, deacc=True, errors='ignore'))        # Tokenizing
        i[0] = [word for word in i[0] if word not in stopwords] # Removing stopwords
        i[0] = [PorterStemmer().stem(word) for word in i[0]]                       # Stemming                        

        i[1].replace('<', ' ')                                                          # Replacing the characters and cleaning tags 
        i[1].replace('>', ' ')
        i[1].replace('-', ' ')

        i[1] = list(tokenize(i[1]))

        i[2] = h.handle(i[2])
        i[2] = list(tokenize(i[2], lowercase=True, deacc=True, errors='ignore'))
        i[2] = [word for word in i[2] if word not in stopwords]
        i[2] = [PorterStemmer().stem(word) for word in i[2]] 
        
        writer.writerow(i)

dat_dup = parse('QueryResults_dup.csv')
fields = dat_dup[0]
dat_dup = dat_dup[1:]

with open('parsed_dup.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    for i in dat_dup:

        i[3] = h.handle(i[3])                                                           # Converting html to text
        i[3] = list(tokenize(i[3], lowercase=True, deacc=True, errors='ignore'))        # Tokenizing
        i[3] = [word for word in i[3] if word not in stopwords] # Removing stopwords
        i[3] = [PorterStemmer().stem(word) for word in i[3]]                       # Stemming                        

        i[5].replace('<', ' ')                                                          # Replacing the characters and cleaning tags 
        i[5].replace('>', ' ')
        i[5].replace('-', ' ')

        i[5] = list(tokenize(i[5]))

        i[4] = h.handle(i[4])
        i[4] = list(tokenize(i[4], lowercase=True, deacc=True, errors='ignore'))
        i[4] = [word for word in i[4] if word not in stopwords]
        i[4] = [PorterStemmer().stem(word) for word in i[4]] 

        j = list()
        j.append(i[3])
        j.append(i[5])
        j.append(i[4])

        writer.writerow(j)

with open('parsed_SU.csv', 'a') as f:
    writer = csv.writer(f)
    for i in dat_dup:

        i[0] = h.handle(i[0])                                                           # Converting html to text
        i[0] = list(tokenize(i[0], lowercase=True, deacc=True, errors='ignore'))        # Tokenizing
        i[0] = [word for word in i[0] if word not in stopwords] # Removing stopwords
        i[0] = [PorterStemmer().stem(word) for word in i[0]]                       # Stemming                        

        i[2].replace('<', ' ')                                                          # Replacing the characters and cleaning tags 
        i[2].replace('>', ' ')
        i[2].replace('-', ' ')

        i[2] = list(tokenize(i[2]))

        i[1] = h.handle(i[1])
        i[1] = list(tokenize(i[1], lowercase=True, deacc=True, errors='ignore'))
        i[1] = [word for word in i[1] if word not in stopwords]
        i[1] = [PorterStemmer().stem(word) for word in i[1]] 

        j = list()
        j.append(i[0])
        j.append(i[2])
        j.append(i[1])
        
        writer.writerow(j)