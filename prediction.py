from composer import *

new_title = input("Enter the title:")
new_tags = input("Enter space separated tags:")
new_desc = input("Enter the description:")

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

for j in pastq:    
    # title
    title_score.append(titlescore(new_ques, j))

    # tags
    tag_score.append(tagscore(new_ques, j))

    # description
    desc_score.append(bodyscore(new_ques, j))

    # topic
    topic_score.append(topicscore(new_ques, j))

# final score
for i_ in range(len(title_score)):
    final_score.append(trained_params[0]*title_score[i_] + trained_params[1]*tag_score[i_] + trained_params[2]*desc_score[i_] + trained_params[3]*topic_score[i_])

final = np.array(final_score)

recall = 20
top_recall = np.argsort(final)[::-1][:recall]

for i in top_recall:
    #print(i)
    print(pastq[i][0], pastq[i][1])