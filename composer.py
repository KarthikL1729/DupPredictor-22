import score
import numpy as np

iter = 10

EC_score = np.zeros((iter, 4))
para_best = np.zeros((iter, 4))

def compose(params, title, tag, desc, topic):
    comp_matrix = np.zeros((title.shape[0], title.shape[1]))
    for i in range(title[0].shape):
        for j in range(title[1].shape):
            comp_matrix[i][j] = params[0]*title[i][j] + params[1]*tag[i][j] + params[2]*desc[i][j] + params[3]*topic[i][j]
    
    return comp_matrix

for i in range(iter):
    params = np.zeros(4)
    params[0] = np.random.uniform(0, 1)
    params[1] = np.random.uniform(0, 1)
    params[2] = np.random.uniform(0, 1)
    params[3] = np.random.uniform(0, 1)

    for i in range(4):
        para_i = params[i]
        para_best[i] = para_i

        para_i = 0

        while(para_i < 1):
            comp_matrix = compose(params, title_score, tag_score, desc_score, topic_score)
            EC = ECscore(comp_matrix)

            if(EC > EC_score[i]):
                EC_score[i] = EC
                para_best[i] = para_i
            para_i += 0.01

best_EC_index = np.argmax(EC_score, axis=0)

trained_params = np.array([para_best[best_EC_index[0]][0], para_best[best_EC_index[1]][1], para_best[best_EC_index[2]][2], para_best[best_EC_index[3]][3]])
        