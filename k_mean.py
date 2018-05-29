import numpy as np
from sklearn.decomposition import PCA
import random
from matplotlib import pyplot as plt

def distance ( first, second , a = 1):
    return np.linalg.norm(first - second, axis=a)
input = open("cluster.csv", "r")

input.readline()
datas = []
for i in range(3823):
    data = input.readline()
    datas.append([int(i) for i in data.split(',')])
pca = PCA(n_components=2)
datas = pca.fit_transform(datas)
k = 5
m=[]
for i in range(k):
    rand = random.randint(0,3822)
    m.append(datas[rand])
bi=[]
difference = 1
while difference != 0:
    for i in datas:
        b = []
        dif = []
        for j in m:
            dif.append(distance(i,j,None))
        for j in m:
            if distance(i,j,None) == min(dif):
                b.append(1)
            else:
                b.append(0)
        bi.append(b)
    m_old = m
    new = []
    e = 0
    for j in m:
        kk = 0
        sum1 = np.zeros(2)
        sum2 = np.zeros(2)
        for i in range(3823):
            sum1 = sum1 + (datas[kk]*bi[kk][e])
            sum2 = sum2 + bi[kk][e]
            kk += 1
        new.append(sum1 / sum2)
        e += 1
    m = new
    m = np.asarray(m)
    m_old = np.asarray(m_old)
    difference = distance(m,m_old,None)

objects = np.ndarray((k,2))
found = []
for every in datas:
    which = []
    for ev in m:
        which.append(distance(every,ev,None))
    mi = min(which)
    ino = which.index(mi)
    if not ino in found:
        objects [ino] = every
        found.append(ino)
sum = 0
i = 0
for j in m:
    sum = sum + distance(j,objects[i],None)
    i += 1
print(sum)

def cluster(data):
    which = []
    for ev in m:
        which.append(distance(data,ev,None))
    mins = min(which)
    indexs = which.index(mins)
    return indexs

colors = ['g','r','y','b','m']
fig,ax = plt.subplots()
for i in range(k):
        points = np.array([datas[j] for j in range(len(datas)) if cluster(datas[j]) == i])
        ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
plt.show()
