import csv
import math

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
        u_topic = unions(i[0], j[0])
        size_i = 0
        size_j = 0
    
        for idx, word in enumerate(u_topic):
            title_i.append(i[0].count(word)/len(i[0]))      # Normalizing to wt
            title_j.append(j[0].count(word)/len(j[0]))
            size_i += (i[0].count(word)/len(i[0]))**2
            size_j += (j[0].count(word)/len(j[0]))**2     # Size parameter for denominator

        title_score.append(sum((ele[0] * ele[1])/(math.sqrt(size_i)*math.sqrt(size_j)) for ele in zip(title_i, title_j)))

        # tags
        tag_i = []
        tag_j = []
        u_tag = unions(i[1], j[1])
        size_i = 0
        size_j = 0

        for idx, word in enumerate(u_tag):
            tag_i.append(i[1].count(word)/len(i[1]))      # Normalizing to wt
            tag_j.append(j[1].count(word)/len(j[1]))
            size_i += (i[1].count(word)/len(i[1]))**2
            size_j += (j[1].count(word)/len(j[1]))**2     # Size parameter for denominator

        tag_score.append(sum((ele[0] * ele[1])/(math.sqrt(size_i)*math.sqrt(size_j))) for ele in zip(tag_i, tag_j))

        # description
        desc_i = []
        desc_j = []
        u_desc = unions(i[2], j[2])
        size_i = 0
        size_j = 0

        for idx, word in enumerate(u_desc):
            desc_i.append(i[1].count(word)/len(i[2]))      # Normalizing to wt
            desc_j.append(j[1].count(word)/len(j[2]))
            size_i += (i[1].count(word)/len(i[2]))**2
            size_j += (j[1].count(word)/len(j[2]))**2     # Size parameter for denominator

        desc_score.append(sum((ele[0] * ele[1])/(math.sqrt(size_i)*math.sqrt(size_j)) for ele in zip(desc_i, desc_j)))

print(title_score)
print(tag_score)
print(desc_score)