from parse import dat, stopwords
from score import titlescore, tagscore, bodyscore, topicscore, pastq
#import composer
from tqdm import tqdm
import html2text
import gensim
import copy
from gensim.utils import tokenize
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.porter import PorterStemmer
import numpy as np

new_title = input("Enter the title:\n")
new_tags = input("Enter space separated tags:\n")
new_desc = input("Enter the description:\n")

# Preprocessing the new question data

title = list(tokenize(new_title, lowercase=True, deacc=True, errors='ignore'))        # Tokenizing
title = [word for word in title if word not in stopwords]                             # Removing stopwords
title = [PorterStemmer().stem(word) for word in title]                                # Stemming

desc = list(tokenize(new_desc, lowercase=True, deacc=True, errors='ignore'))        # Tokenizing
desc = [word for word in desc if word not in stopwords]                             # Removing stopwords
desc = [PorterStemmer().stem(word) for word in desc]                                # Stemming

tag = list(tokenize(new_tags))

title = str(title)
desc = str(desc)
tag = str(tag)
dumid = str(00)                     # Dummy id                                                           # Id of the new question

new_ques = [dumid, title, desc,  tag]

# Calculating the score

title_score = []
tag_score = []
desc_score = []
topic_score = []
final_score = []

for j in tqdm(range(len(pastq)), desc="Calculating component scores"):    
    # title
    title_score.append(titlescore(new_ques, pastq[j]))

    # tags
    tag_score.append(tagscore(new_ques, pastq[j]))

    # description
    desc_score.append(bodyscore(new_ques, pastq[j]))

    # topic
    topic_score.append(topicscore(new_ques, pastq[j]))

# final score
trained_params = np.loadtxt('trained_params.txt')

for i_ in tqdm(range(len(title_score)), desc="Calculating final score"):
    final_score.append(trained_params[0]*title_score[i_] + trained_params[1]*tag_score[i_] + trained_params[2]*desc_score[i_] + trained_params[3]*topic_score[i_])

final = np.array(final_score)

recall = 20
top_recall = np.argsort(final)[::-1][:recall]

for i in top_recall:
    #print(i)
    print(dat[i][0], dat[i][1])