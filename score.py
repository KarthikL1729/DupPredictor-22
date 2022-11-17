import csv

def unions(l1, l2):
    return list(set().union(l1, l2))


def parse(filename):

    with open(filename, 'r') as f:
        data = csv.reader(f)
        data = list(data)

    return data


dup = parse('parsed_dup.csv')
dup = dup[1:]

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
        for idx, word in enumerate(u_topic):
            title_i.append(i[0].count(word))
            title_j.append(j[0].count(word))

        title_score.append(sum(ele[0] * ele[1] for ele in zip(title_i, title_j)))

        # tags
        tag_i = []
        tag_j = []
        u_tag = unions(i[1], j[1])
        for idx, word in enumerate(u_tag):
            title_i.append(i[1].count(word))
            title_j.append(j[1].count(word))

        tag_score.append(sum(ele[0] * ele[1] for ele in zip(tag_i, tag_j)))

        # description
        desc_i = []
        desc_j = []
        u_desc = unions(i[2], j[2])
        for idx, word in enumerate(u_desc):
            desc_i.append(i[2].count(word))
            desc_j.append(j[2].count(word))

        desc_score.append(sum(ele[0] * ele[1] for ele in zip(desc_i, desc_j)))

#print(title_score)
#print(tag_score)
#print(desc_score)