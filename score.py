import csv
import math
import numpy as np
from numpy.linalg import norm

from gensim import corpora, models, matutils
from pprint import pprint


def unions(l1, l2):
    return list(set().union(l1, l2))


def parse(filename):

    with open(filename, 'r') as f:
        data = csv.reader(f)
        data = list(data)

    return data

def titlescore(q_i, q_j):
    title_i = []
    title_j = []

    i_title = q_i[1].replace("'", "").strip('][').split(', ')  # changing from string to list
    j_title = q_j[1].replace("'", "").strip('][').split(', ')

    u_title = unions(i_title, j_title)
    size_i = 0
    size_j = 0

    for idx, word in enumerate(u_title):
        title_i.append(i_title.count(word)/len(i_title)
                       )      # Normalizing to wt
        title_j.append(j_title.count(word)/len(j_title))
        size_i += (i_title.count(word)/len(i_title))**2
        # Size parameter for denominator
        size_j += (j_title.count(word)/len(j_title))**2

    return np.dot(title_i, title_j)/(math.sqrt(size_i)*math.sqrt(size_j))

def bodyscore(q_i, q_j):

    body_i = []
    body_j = []

    i_body = q_i[2].replace("'", "").strip('][').split(', ')
    j_body = q_j[2].replace("'", "").strip('][').split(', ')

    u_body = unions(i_body, j_body)
    size_i = 0
    size_j = 0

    for idx, word in enumerate(u_body):
        body_i.append(i_body.count(word)/len(i_body))
        body_j.append(j_body.count(word)/len(j_body))
        size_i += (i_body.count(word)/len(i_body))**2
        size_j += (j_body.count(word)/len(j_body))**2

    return np.dot(body_i, body_j)/(math.sqrt(size_i)*math.sqrt(size_j))

def tagscore(q_i, q_j):

    tag_i = []
    tag_j = []

    i_tag = q_i[3]#.replace("'", "").strip('][').split(', ')
    j_tag = q_j[3]#.replace("'", "").strip('][').split(', ')

    u_tag = unions(i_tag, j_tag)
    size_i = 0
    size_j = 0

    for idx, word in enumerate(u_tag):
        tag_i.append(i_tag.count(word)/len(i_tag))
        tag_j.append(j_tag.count(word)/len(j_tag))
        size_i += (i_tag.count(word)/len(i_tag))**2
        size_j += (j_tag.count(word)/len(j_tag))**2

    return np.dot(tag_i, tag_j)/(math.sqrt(size_i)*math.sqrt(size_j))

def topicscore(q_i, q_j):
    
    i_title = q_i[1].replace("'", "").strip('][').split(', ')  # changing from string to list
    j_title = q_j[1].replace("'", "").strip('][').split(', ')
    i_body = q_i[2].replace("'", "").strip('][').split(', ')
    j_body = q_j[2].replace("'", "").strip('][').split(', ')

    i_topics = unions(i_title, i_body)
    j_topics = unions(j_title, j_body) 
    
    corpus_i = id2word_dict.doc2bow(i_topics)
    prob_i = np.array(lda_model[corpus_i])[:, 1]
    doc_i = lda_model[corpus_i]

    
    corpus_j = id2word_dict.doc2bow(j_topics)
    prob_j = np.array(lda_model[corpus_j])[:, 1]
    doc_j = lda_model[corpus_j]


    return np.dot(prob_i, prob_j)/(norm(prob_i)*norm(prob_j)) 

dup = parse('parsed_dup.csv')
dup = dup[1:]                                       # Removing headers

pastq = parse('parsed_SU.csv')
pastq = pastq[1:]

titles_data = []
desc_data = []

# getting all past q titles and decs
for p in pastq:

    # title
    p_title = p[1].replace("'", "").strip('][').split(
        ', ')  # changing from string to list

    titles_data = unions(titles_data, p_title)

    # description
    p_desc = p[2].replace("'", "").strip('][').split(', ')

    desc_data = unions(desc_data, p_desc)


# topic data
u_topic = unions(titles_data, desc_data)

# building LDA model on past q
dataset = [d.split() for d in u_topic]
id2word_dict = corpora.Dictionary(dataset)  # maps each word to a unique id

# maps word ids to word frequencies
corpus = [id2word_dict.doc2bow(word) for word in dataset]

# number of topics (this should be 100 according to the paper)
num_topics = 50

# Build LDA model
lda_model = models.LdaMulticore(
    corpus=corpus, id2word=id2word_dict, num_topics=num_topics, minimum_probability=0.0)

# # Print the Keywords in the 10 topics and the keywords contributions to the topic
# pprint(lda_model.print_topics())
# doc_lda = lda_model[corpus]

