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

dat = parse('QueryResultsSU_new.csv')
fields = dat[0]
dat = dat[1:100]
dat_temp = dat

h = html2text.HTML2Text()

h.ignore_links = True
# Links ignored
stopwords = gensim.parsing.preprocessing.STOPWORDS
with open('parsed_SU.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    for i in dat_temp:

        i[1] = h.handle(i[1])                                                           # Converting html to text
        i[1] = list(tokenize(i[1], lowercase=True, deacc=True, errors='ignore'))        # Tokenizing
        i[1] = [word for word in i[1] if word not in stopwords] # Removing stopwords
        i[1] = [PorterStemmer().stem(word) for word in i[1]]                       # Stemming                        

        i[3].replace('<', ' ')                                                          # Replacing the characters and cleaning tags 
        i[3].replace('>', ' ')
        i[3].replace('-', ' ')

        i[3] = list(tokenize(i[3]))

        i[2] = h.handle(i[2])
        i[2] = list(tokenize(i[2], lowercase=True, deacc=True, errors='ignore'))
        i[2] = [word for word in i[2] if word not in stopwords]
        i[2] = [PorterStemmer().stem(word) for word in i[2]] 
        
        j = list()
        j.append(i[0])
        j.append(i[1])
        j.append(i[2])
        j.append(i[3])

        writer.writerow(j)

dat_dup = parse('QueryResults_dup_new.csv')
dat_dup_temp = dat_dup
fields = dat_dup[0]
dat_dup = dat_dup[1:20]
dat_master = [[l[0], l[1], l[2], l[3]] for l in dat_dup]
dat = dat + dat_master
#print(len(dat))
with open('parsed_SU.csv', 'a') as f:
    writer = csv.writer(f)
    for i in dat_dup_temp:

        i[1] = h.handle(i[1])                                                           # Converting html to text
        i[1] = list(tokenize(i[1], lowercase=True, deacc=True, errors='ignore'))        # Tokenizing
        i[1] = [word for word in i[1] if word not in stopwords] # Removing stopwords
        i[1] = [PorterStemmer().stem(word) for word in i[1]]                       # Stemming                        

        i[3].replace('<', ' ')                                                          # Replacing the characters and cleaning tags 
        i[3].replace('>', ' ')
        i[3].replace('-', ' ')

        i[3] = list(tokenize(i[3]))

        i[2] = h.handle(i[2])
        i[2] = list(tokenize(i[2], lowercase=True, deacc=True, errors='ignore'))
        i[2] = [word for word in i[2] if word not in stopwords]
        i[2] = [PorterStemmer().stem(word) for word in i[2]] 
        
        j = list()
        j.append(i[0])
        j.append(i[1])
        j.append(i[2])
        j.append(i[3])
        
        writer.writerow(j)


with open('parsed_dup.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fields[4:8])
    for i in dat_dup_temp:

        i[5] = h.handle(i[5])                                                           # Converting html to text
        i[5] = list(tokenize(i[5], lowercase=True, deacc=True, errors='ignore'))        # Tokenizing
        i[5] = [word for word in i[5] if word not in stopwords] # Removing stopwords
        i[5] = [PorterStemmer().stem(word) for word in i[5]]                       # Stemming                        

        i[7].replace('<', ' ')                                                          # Replacing the characters and cleaning tags 
        i[7].replace('>', ' ')
        i[7].replace('-', ' ')

        i[7] = list(tokenize(i[7]))

        i[6] = h.handle(i[6])
        i[6] = list(tokenize(i[6], lowercase=True, deacc=True, errors='ignore'))
        i[6] = [word for word in i[6] if word not in stopwords]
        i[6] = [PorterStemmer().stem(word) for word in i[6]] 

        j = list()
        j.append(i[4])
        j.append(i[5])
        j.append(i[6])
        j.append(i[7])

        writer.writerow(j)