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

dat = parse('QueryResults.csv')
fields = dat[0]
dat = dat[1:]

h = html2text.HTML2Text()

h.ignore_links = True
# Links ignored
stopwords = gensim.parsing.preprocessing.STOPWORDS
with open('parsed.csv', 'w') as f:
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