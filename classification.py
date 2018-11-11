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
    center_word = word_list[0]
    add_for_graph_x = list()
    add_for_grapy_y = list()
    add_tag = list()
    i = 0
    n = 0
    while i < (len(word_list)-1):
        j = i + 1
        while j < (len(word_list)):
            leven_result = leven.levenshteins(word_list[i],word_list[j])
            #print("word",word_list[i],"leven[0]",leven_result[0],"leven[1]",leven_result[1])
            print(leven_result)
            add_for_graph_x.append(leven_result[0])
            add_for_grapy_y.append(leven_result[1])
            add_tag.append((word_list[i],word_list[j]))
            j+=1
        n+=1
        #print(n)
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



def clustering(X):
    plt.plot()
    colors = ['b', 'g', 'r','y']
    markers = ['o', 'v', 's','x']
    K = 4
    kmeans_model = KMeans(n_clusters=K)
    print(kmeans_model)
    cluster_labels = kmeans_model.fit_predict(X[0])
    print(cluster_labels)
    range_n_clusters = [2,3,4,5,6]
    plt.plot()
    for i, l in enumerate(kmeans_model.fit(X[0]).labels_):
        print(i,l)
        plt.plot(X[1][i], X[2][i], color=colors[l], marker=markers[l],ls='None')
        plt.xlim([0, 20])
        plt.ylim([0, 10])
    plt.show()







def main():
    mapping = mapping_word.mapping_word()
    word_list = mapping.mapping_number()
    X = get_distance(word_list)

    #print(word_list)
    #print("list",word_list)
    #elbow(X[0])
    lables = clustering(X)
    #plotSilhouette(X[0],lables)

    #center_words = make_distance(word_list,mapping)
    #write_file(center_words)

if __name__ =="__main__":
    main()
