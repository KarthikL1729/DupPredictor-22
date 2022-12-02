from score import *
from gensim import corpora, models, matutils
from pprint import pprint

title_score = []
tag_score = []
desc_score = []
topic_score = []

for i in dup:
    for j in pastq:

        # title
        title_score.append(titlescore(i, j))

        #print("title: ")
        #print(np.dot(title_i, title_j)/ (math.sqrt(size_i)*math.sqrt(size_j)))

        # tags
        tag_score.append(tagscore(i, j))

        #print("tag: ")
        #print( np.dot(tag_i, tag_j) / (math.sqrt(size_i)*math.sqrt(size_j)) )

        # description
        desc_score.append(bodyscore(i, j))

        #print("desc: ")
        #print( np.dot(desc_i, desc_j) / (math.sqrt(size_i)*math.sqrt(size_j)) )

        # topic
        topic_score.append(topicscore(i, j))

        #topic_score.append( matutils.cossim(doc_i, doc_j) )

        #print("topic: ")
        # print( lda_model.get_document_topics(corpus_i) )
        # print( lda_model.get_document_topics(corpus_j) )

        #print(matutils.cossim(doc_i, doc_j))
        #print( np.dot(prob_i, prob_j) / ( norm(prob_i)*norm(prob_j) ) )
        # print()


# print(title_score)
# print(tag_score)
# print(desc_score)
# print(topic_score)

title_score = np.array(title_score, ndmin=2)
desc_score = np.array(desc_score, ndmin=2)
tag_score = np.array(tag_score, ndmin=2)
topic_score = np.array(topic_score, ndmin=2)

title_score = np.reshape(title_score, (len(dup), len(pastq)))
desc_score = np.reshape(desc_score, (len(dup), len(pastq)))
tag_score = np.reshape(tag_score, (len(dup), len(pastq)))
topic_score = np.reshape(topic_score, (len(dup), len(pastq)))
