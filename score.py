import csv
import math

from gensim import corpora, models
from pprint import pprint

def unions(l1, l2):
    return list(set().union(l1, l2))


def parse(filename):

    with open(filename, 'r') as f:
        data = csv.reader(f)
        data = list(data)

    return data


dup = parse('parsed_dup.csv')
dup = dup[1:]                                       # Removing headers

pastq = parse('parsed_SU.csv')
pastq = pastq[1:]

title_score=[]
tag_score=[]
desc_score=[]

for i in dup:
    for j in pastq:

        # title
        title_i = []
        title_j = []

        i_0 = i[0].replace("'", "").strip('][').split(', ')     #changing from string to list
        j_0 = j[0].replace("'", "").strip('][').split(', ')

        u_title = unions(i_0, j_0)
        size_i = 0
        size_j = 0

        for idx, word in enumerate(u_title):
            title_i.append(i_0.count(word)/len(i_0))      # Normalizing to wt
            title_j.append(j_0.count(word)/len(j_0))
            size_i += (i_0.count(word)/len(i_0))**2
            size_j += (j_0.count(word)/len(j_0))**2     # Size parameter for denominator

        title_score.append(sum((ele[0] * ele[1])/(math.sqrt(size_i)*math.sqrt(size_j)) for ele in zip(title_i, title_j)))

        # tags
        tag_i = []
        tag_j = []

        i_1 = i[1].replace("'", "").strip('][').split(', ')
        j_1 = j[1].replace("'", "").strip('][').split(', ')

        u_tag = unions(i_1, j_1)
        size_i = 0
        size_j = 0

        for idx, word in enumerate(u_tag):
            tag_i.append(i_1.count(word)/len(i_1))      # Normalizing to wt
            tag_j.append(j_1.count(word)/len(j_1))
            size_i += (i_1.count(word)/len(i_1))**2
            size_j += (j_1.count(word)/len(j_1))**2     # Size parameter for denominator

        tag_score.append(sum((ele[0] * ele[1])/(math.sqrt(size_i)*math.sqrt(size_j))) for ele in zip(tag_i, tag_j))

        # description
        desc_i = []
        desc_j = []

        i_2 = i[2].replace("'", "").strip('][').split(', ')
        j_2 = j[2].replace("'", "").strip('][').split(', ')

        u_desc = unions(i_2, j_2)
        size_i = 0
        size_j = 0

        for idx, word in enumerate(u_desc):
            desc_i.append(i_2.count(word)/len(i_2))      # Normalizing to wt
            desc_j.append(j_2.count(word)/len(j_2))
            size_i += (i_2.count(word)/len(i_2))**2
            size_j += (j_2.count(word)/len(j_2))**2     # Size parameter for denominator

        desc_score.append(sum((ele[0] * ele[1])/(math.sqrt(size_i)*math.sqrt(size_j)) for ele in zip(desc_i, desc_j)))

        # topic
        u_topic = unions(u_title, u_desc)

        dataset = [d.split() for d in u_topic]
        id2word = corpora.Dictionary(dataset)       #maps each word to a unique id

        corpus = [id2word.doc2bow(word) for word in dataset]        #maps word ids to word frequencies

        # number of topics (this should be 100 according to the paper)
        num_topics = 10
        
        # Build LDA model
        lda_model = models.LdaMulticore(corpus=corpus, id2word=id2word, num_topics=num_topics)

        # # Print the Keywords in the 10 topics and the keywords contributions to the topic
        # pprint(lda_model.print_topics())
        # doc_lda = lda_model[corpus]
        

#print(title_score)
#print(tag_score)
#print(desc_score)