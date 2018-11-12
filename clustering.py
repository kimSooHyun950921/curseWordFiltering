import mapping_word
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import math
import dic
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
from sklearn.metrics import silhouette_samples
from matplotlib import cm
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
import mglearn
from sklearn.preprocessing import StandardScaler
import word_dist_matrix as mat
mpl.rcParams['axes.unicode_minus'] = False
import csv
import os
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

import pandas as pd

path = '/usr/share/fonts/truetype/nanum/NanumBarunGothicLight.ttf'
fontprop = fm.FontProperties(fname=path, size=18).get_name()





def split_jamo(word):
    jaeum = list()
    moeum = list()
    for i in range(len(word)):
        if word[i] in dic.jaum_list:
            jaeum.append(word[i])
        if word[i] in dic.moum_list:
            moeum.append(word[i])
        else:
            pass
    #print(jaeum,moeum)
    return (jaeum,moeum)




#def append_xy(word_list):
def get_levenshtein(word_list):
    center_word = word_list[1024]
    add_for_graph_x = list()
    add_for_grapy_y = list()
    add_tag = list()
    i = 1
    n = 0
    while i < len(word_list):
        print(i)
        leven_result = leven.levenshteins(center_word,word_list[i])
            #print("word",word_list[i],"leven[0]",leven_result[0],"leven[1]",leven_result[1])
        print(leven_result)
        if leven_result[0] !=0 and leven_result!=0:
            add_for_graph_x.append(leven_result[0])
            add_for_grapy_y.append(leven_result[1])
            add_tag.append(word_list[i])
        i+=1
    return (add_for_graph_x,add_for_grapy_y)
    #return[(add_for_graph_x,add_for_grapy_y,add_tag),(

def elbow(X):
    sse = []
    for i in range(1,11):
        km = KMeans(n_clusters=i,init="k-means++",random_state=0)
        km.fit(X)
        sse.append(km.inertia_)
    plt.plot(range(1,11),sse,marker='o')
    plt.xlabel('클러스터 개수')
    plt.ylabel('SSE')
    plt.show()



def get_distance(word_list):
    xy = get_levenshtein(word_list)
    x_array = np.asarray(xy[0],dtype = float)
    y_array = np.asarray(xy[1],dtype = float)
    X = np.array(list(zip(x_array, y_array))).reshape(len(x_array), 2)
    return (X,x_array,y_array)


#colors =  ['b', 'g', 'r', 'y','c']
#markers = ['o', 'v', 's', 'x','d']
def kmeans_clustering(X):
    plt.plot()
    colors =  ['b', 'g', 'r', 'y','c']
    markers = ['o', 'v', 's', 'x','d']
    K = 2
    kmeans_model = KMeans(n_clusters=K)
    print(kmeans_model)
    cluster_labels = kmeans_model.fit_predict(X)
    print(cluster_labels)
    label = kmeans_model.fit(X).labels_
    range_n_clusters = [2,3,4,5,6]
    plt.plot()
    for i, l in enumerate(kmeans_model.fit(X).labels_):
        print(i,l)
        plt.plot(X[0][i], X[0][i], color=colors[l], marker=markers[l],ls='None')
        plt.xlim([0, 20])
        plt.ylim([0, 10])
    plt.show()
    print(metrics.silhouette_score(X,label,metric='euclidean'))

def agg_clustering(X,n):
    scaler = StandardScaler()
    scaler.fit(X)
    X_scaled =X# scaler.transform(X)
    agg = AgglomerativeClustering(n_clusters=n,affinity='euclidean',linkage='ward')
    plt.plot()

    assignment = agg.fit_predict(X_scaled)
    print(mglearn.discrete_scatter(X_scaled[:, 0], X_scaled[:, 1], assignment))
    print(metrics.silhouette_score(X_scaled,assignment))
    plt.show()


def dbs_clus(X):
    scaler = StandardScaler()
    scaler.fit(X[0])
    #X_scaled = scaler.transform(X[0])
    #print(X_scaled)
    dbscan = DBSCAN()
    clusters = dbscan.fit_predict(X[0])
    print("클러스터 레이블:\n{}".format(clusters))
    plt.scatter(X[0][:, 0], X[0][:, 1], c=clusters,  s=50, edgecolors='black')
    plt.show()

def dend(X):
    row_clusters = linkage(X,method='ward')
    result = pd.DataFrame(row_clusters,
                 columns=['cluster_1','cluster_2','거리','클러스터 멤버수'],
                 index =['클러스터 %d'%(i+1) for i in range(row_clusters.shape[0])])
    #print(result)
    row_dendr = dendrogram(row_clusters )
    plt.tight_layout()
    plt.ylabel('euclide distance')
    plt.show()
    agg_clustering(X,2)






def write_file(file_name,X):
    file_name = ''+file_name+'.csv'
    with open(file_name,'w') as csvfile:
        writer = csv.writer(csvfile,delimiter=',')
        print(len(X))
        writer.writerows(X)

def get_word_list():
    mapping = mapping_word.mapping_word()
    #select = input("input leven - ")
    select = "leven"
    word_list = list()
    print(select)
    if select == "jamo":
        word_list = mapping.read_word()
    elif select =="leven":
        word_list =  mapping.mapping_number()
        word_list = word_list[:-2]
    print(word_list)
    return (word_list,select)

def make_matrix():
    result = get_word_list()
    word_list = result[0]
    select = result[1]
    X = list()
    file_name = ''+select+".csv"
    if os.path.isfile(file_name):
        X = read_file(file_name)

    else:
        X = mat.make_matrix_for_clustering(word_list,select)
        write_file(select,X)

    return X

def read_file(file_name):
    all_list = list()
    with open(file_name,"r") as csv_file:
        while True:
            line = csv_file.readline()
            if not line:
                break
            line.replace('\n','')
            list_data = line.split(',')
            all_list.append(list(list_data))
    return all_list


def start_clustering():
    X = make_matrix()
    s = np.array(X,dtype=float)
    print(s)
    #elbow(s)
    #ables = kmeans_clustering(s)(
    dend(s)








def main():
    start_clustering()



    #print(word_list)
    #print("list",word_list)
    #elbow(s)
    #AggClustering(X)
    #dbs_clus(X)
    #plotSilhouette(X[0],lables)

    #center_words = make_distance(word_list,mapping)
    #write_file(center_words)

if __name__ =="__main__":
    main()
