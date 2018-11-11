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
import levenshtein as leven
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
import mglearn
from sklearn.preprocessing import StandardScaler
mpl.rcParams['axes.unicode_minus'] = False

path = '/usr/share/fonts/truetype/nanum/NanumBarunGothicLight.ttf'
fontprop = fm.FontProperties(fname=path, size=18).get_name()

def plotSilhouette(X,y_km):
    silhoutte_avg = silhoulette_score(X,y_km)
    for n_clusters in range_n_clusters:
        fig = tools.make_subplots(rows=1,cols=2,print_grid=False,)



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
def kmenas_clustering(X):
    plt.plot()
    colors =  ['b', 'g', 'r', 'y','c']
    markers = ['o', 'v', 's', 'x','d']
    K = 2
    kmeans_model = KMeans(n_clusters=K)
    print(kmeans_model)
    cluster_labels = kmeans_model.fit_predict(X[0])
    print(cluster_labels)
    label = kmeans_model.fit(X[0]).labels_
    range_n_clusters = [2,3,4,5,6]
    plt.plot()
    for i, l in enumerate(kmeans_model.fit(X[0]).labels_):
        print(i,l)
        plt.plot(X[1][i], X[2][i], color=colors[l], marker=markers[l],ls='None')
        plt.xlim([0, 20])
        plt.ylim([0, 10])
    plt.show()
    print(metrics.silhouette_score(X[0],label,metric='euclidean'))

def agg_clustering(X):
    scaler = StandardScaler()
    scaler.fit(X[0])
    X_scaled = scaler.transform(X[0])
    agg = AgglomerativeClustering(n_clusters=4)
    plt.plot()
    colors =  ['b', 'g', 'r', 'y','c']
    markers = ['o', 'v', 's', 'x','d']
    assignment = agg.fit_predict(X_scaled)
    print(mglearn.discrete_scatter(X_scaled[:, 0], X_scaled[:, 1], assignment))
    print(metrics.silhouette_score(X_scaled,assignment))
    plt.legend(["클러스터 0", "클러스터 1", "클러스터 2"], loc="best")
    plt.xlabel("특성 0")
    plt.ylabel("특성 1")
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








def main():
    mapping = mapping_word.mapping_word()
    word_list = mapping.mapping_number()
    X = get_distance(word_list)

    #print(word_list)
    #print("list",word_list)
    #elbow(X[0])
    #lables = clustering(X)
    AggClustering(X)
    #dbs_clus(X)
    #plotSilhouette(X[0],lables)

    #center_words = make_distance(word_list,mapping)
    #write_file(center_words)

if __name__ =="__main__":
    main()
