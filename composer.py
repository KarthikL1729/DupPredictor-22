from score import *
from parse import *
import numpy as np

iter = 10

EC_score = np.zeros((iter, 4))
para_best = np.zeros((iter, 4))


def ECscore(comp_matrix):
    recall = 20
    EC_score = 0

    for index, i in enumerate(comp_matrix):
        top_recall = np.argsort(i)[::-1][:recall]

        for idx in top_recall:
            # print(pastq[idx][0])
            # print(pastq[len(i)-len(comp_matrix)+index][0])
            # print()

            if(pastq[idx][0] == pastq[len(i)-len(comp_matrix)+index][0]):
                EC_score += 1
                break

    # print(EC_score)

    return EC_score/len(comp_matrix)


def compose(params, title, tag, desc, topic):
    comp_matrix = np.zeros((np.shape(title)[0], np.shape(title)[1]))
    for i in range(np.shape(title)[0]):
        for j in range(np.shape(title)[1]):
            comp_matrix[i][j] = params[0]*title[i][j] + params[1] * \
                tag[i][j] + params[2]*desc[i][j] + params[3]*topic[i][j]

    return comp_matrix


for i_ in range(iter):
    params = np.zeros(4)
    params[0] = np.random.uniform(0, 1)
    params[1] = np.random.uniform(0, 1)
    params[2] = np.random.uniform(0, 1)
    params[3] = np.random.uniform(0, 1)

    for i in range(4):
        para_best[i_][i] = params[i]

        params[i] = 0

        while(params[i] < 1):
            comp_matrix = compose(params, title_score,
                                  tag_score, desc_score, topic_score)
            EC = ECscore(comp_matrix)

            if(EC > EC_score[i_][i]):
                EC_score[i_][i] = EC
                para_best[i_][i] = params[i]

            params[i] += 0.01

best_EC_index = np.argmax(EC_score, axis=0)
print(best_EC_index)

#trained_params = np.array([para_best[best_EC_index[0]][0], para_best[best_EC_index[1]][1], para_best[best_EC_index[2]][2], para_best[best_EC_index[3]][3]])
