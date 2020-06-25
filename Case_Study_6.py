from collections import Counter
import numpy as np
import pandas as pd

#Exercise 1

def marginal_prob(chars):
    l2 = chars.values()
    d1 = {}
    for i in l2:
        if i in d1.keys():
            d1[i]+=1
        else:
            d1[i]=1
    s = sum(d1.values())
    for key,value in d1.items():
        d1[key]= value/s
    return d1
        
def chance_homophily(chars):
    return sum([i**2 for i in chars.values()])
     

favorite_colors = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}

color_homophily = chance_homophily(marginal_prob(favorite_colors))
print(color_homophily)


#Exercise 2

df  = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@individual_characteristics.csv", low_memory=False, index_col=0)
df1 = df[df.village==1]
df2 = df[df.village==2]
print (df1.head())

#Exercise 3

sex1      = dict(zip(df1['pid'],df1['resp_gend']))
caste1    = dict(zip(df1['pid'],df1['caste']))
religion1 = dict(zip(df1['pid'],df1['religion']))

sex2      = dict(zip(df2['pid'],df2['resp_gend']))
caste2    = dict(zip(df2['pid'],df2['caste']))
religion2 = dict(zip(df2['pid'],df2['religion']))

print(caste2[202802])

#Exercise 4

s1 = chance_homophily(marginal_prob(sex1))
c1 = chance_homophily(marginal_prob(caste1))
r1 = chance_homophily(marginal_prob(religion1))
s2 = chance_homophily(marginal_prob(sex2))
c2 = chance_homophily(marginal_prob(caste2))
r2 = chance_homophily(marginal_prob(religion2))

dic = dict(zip(["sex1","caste1","religion1","sex2","caste2","religion2"],[s1,c1,r1,s2,c2,r2]))

m1 = max(dic.values())

result = [ x for x in dic.keys() if dic[x] == m1]

#Exercise 5

def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                num_ties+=1
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    num_same_ties+=1
    return (num_same_ties / num_ties)

#Exercise 6

data_filepath1 = "https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_1.csv"
data_filepath2 = "https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_2.csv"

df1 = pd.read_csv(data_filepath1)
df2 = pd.read_csv(data_filepath2)

print(df1.iloc[100])

#Exercise 7

import networkx as nx
A1 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno1.csv", index_col=0))
A2 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno2.csv", index_col=0))
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

pid1 = pd.read_csv(data_filepath1, dtype=int)['0'].to_dict()
pid2 = pd.read_csv(data_filepath2, dtype=int)['0'].to_dict()

hs1 = homophily(G1,sex1,pid1)
hc1 = homophily(G1,caste1,pid1)
hr1 = homophily(G1,religion1,pid1)
hs2 = homophily(G2,sex2,pid2)
hc2 = homophily(G2,caste2,pid2)
hr2 = homophily(G2,religion2,pid2)
dic2 = dict(zip(["sex1","caste1","religion1","sex2","caste2","religion2"],[hs1,hc1,hr1,hs2,hc2,hr2]))

print("chance_homophily", dic)
print("homophily", dic2)

























