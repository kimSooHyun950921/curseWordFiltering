import mapping_word
import sys
import numpy as np
import decompose
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
mpl.rcParams['axes.unicode_minus'] = False

path = '/usr/share/fonts/truetype/nanum/NanumBarunGothicLight.ttf'
fontprop = fm.FontProperties(fname=path, size=18).get_name()

def plotSilhouette(X,y_km):
    silhoutte_avg = silhoulette_score(X,y_km)
    print("For n_clusters =",)
    n_clusters = cluster_labels.shape[0]
    silhouette_vals = silhouette_samples(X,y_km,metric="eulidean")
    y_ax_lower,y_ax_upper=0,0
    yticks = []
    for i, c in enumerate(cluster_labels):
        c_silhouette_vals = silhouette_vals[y_km==c]
        c_silhouette_vals.sort()
        y_ax_upper+=len(c_silhouette_vals)
        color = cm.jet(i/n_clusters)

        plt.barh(range(y_ax_lower,y_ax_upper),c_silhouette_vals,height=1.0,
        edgecolor='none',color=color)
        yticks.append((y_ax_lower+y_ax_upper)/2)
        y_ax_lower +=len(c_silhouette_vals)

    silhoutte_avg = np.mean(silhouette_vals)
    plt.axvline(silhoutte_avg,color='red',linestype='--')
    plt.yticks(yticks,cluster_labels+1)
    plt.ylabel('클러스터')
    plt.xlabel('실루엣 계수')
    X,y = make_blobs(n_samples=150,n_features=2,centers=3,cluster_std=0.5,
    shuffle=True,random_state=0)
    km = KMeans(n_clusters=3,random_state=0)
    y_km = km.fit_predict(X)
    plotSilhouette(X,y_km)



def split_jamo(word):
    jaeum = list()
    moeum = list()
    for i in range(len(word)):
        if word[i] in decompose.jaum_list:
            jaeum.append(word[i])
        if word[i] in decompose.moum_list:
            moeum.append(word[i])
        else:
            pass
    #print(jaeum,moeum)
    return (jaeum,moeum)


#def append_xy(word_list):
def append_xy(word_list):
    center_word = word_list[0]
    center_word = split_jamo(center_word)
    add_for_graph_x = list()
    add_for_grapy_y = list()
    add_tag = list()
    i = 0
    for word in word_list:
        compare_word = split_jamo(word)
        print(compare_word)
        leven_result = levenshtein(center_word,compare_word)
#            print(word_list[i],leven_result[0],leven_result[1])

        add_for_graph_x.append(leven_result[0])
        add_for_grapy_y.append(leven_result[1])
        add_tag.append(word_list[i])

    print(add_for_graph_x)
    print(add_for_grapy_y)
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

def get_X(word_list):
    xy = append_xy(word_list)
    x_array = np.asarray(xy[0],dtype = float)
    y_array = np.asarray(xy[1],dtype = float)
    X = np.array(list(zip(x_array, y_array))).reshape(len(x_array), 2)
    return (X,x_array,y_array)



def clustering(X):
    plt.plot()
    colors = ['b', 'g', 'r',]
    markers = ['o', 'v', 's',]
    K = 3
    kmeans_model = KMeans(n_clusters=K)
    cluster_labels = kmeans_model.fit_predict(X[0])
    range_n_clusters = [2,3,4,5,6]
    plt.plot()
    for i, l in enumerate(kmeans_model.fit(X[0]).labels_):
        plt.plot(X[1][i], X[2][i], color=colors[l], marker=markers[l],ls='None')
        plt.xlim([0, 20])
        plt.ylim([0, 10])
    plt.show()







def main():
    mapping = mapping_word.mapping_word()
    word_list = mapping.mapping_number()
    X = get_X(word_list)
    #print(word_list)
    #print("list",word_list)
    #elbow(X)
    lables = clustering(X)
    plotSilhouette(X[0],lables)

    #center_words = make_distance(word_list,mapping)
    #write_file(center_words)

if __name__ =="__main__":
    main()
