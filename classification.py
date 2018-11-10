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

def jamo_levenshtein(s1, s2, cost=None, debug=False):
    if len(s1) < len(s2):
        return jamo_levenshtein(s2, s1, debug)
    if len(s2) == 0:
        return len(s1)
    def substitution_cost(c1, c2):
        if c1 == c2:
            return 0
        elif c1 in decompose.jaum_list and c2 in decompose.jaum_list:
            return dic.jaeum_cost.get(c1)[dic.jaeum.index(c2)]
        elif c1 in decompose.moum_list and c2 in decompose.moum_list:
            return 1+abs(dic.moeum_cost.get(c1) - dic.moeum_cost.get(c2))
        else:
            return 2



    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1]+1
            deletions = current_row[j]+1
            # Changed
            substitutions = previous_row[j] + substitution_cost(c1, c2)
            #print("jamo:",c1,c2,substitution_cost(c1,c2))

            current_row.append(min(insertions, deletions, substitutions))

        if debug:
            print(['%.3f'%v for v in current_row[1:]])
        previous_row = current_row

    return previous_row[-1]


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




def make_distance(word_list,mapping):
    center_words = list()
    j=0
    while j < len(word_list):
        xy = append_xy(j,word_list)
        distances = get_all_distance(xy[0],xy[1],word_list)
        print(distances)
        removing_word_result = remove_similiar_word(distances,word_list)
        word_list = removing_word_result[0]
        center_words.append(removing_word_result[1])

        j+=1
    for i in range(len(center_words)):
        print(center_words[i])
    print(len(center_words))
    return center_words


#?
def remove_similiar_word(distance_list,word_list):
    temp_word_list = list()
    for i in range(len(distance_list)):
        element = distance_list[i]
        distance = element[0]
        if distance < 2.5:
            popping_word = word_list.remove(element[3])
            temp_word_list.append(element[3])
            half_index = int(len(temp_word_list)/2)
    return (word_list,temp_word_list[half_index])


        #draw_plot(add_for_graph_x,add_for_grapy_y,word_list,word_list[1001])
def levenshtein(center,compare):
    print(center, compare)
    jaeum_dif = jamo_levenshtein(center[0],compare[0])*1.5
    moeum_dif = jamo_levenshtein(center[1],compare[1])
    return (jaeum_dif,moeum_dif)



#?
def get_all_distance(jaeum,moeum,lables):
    all_distance= list()
    for label,x,y in zip(lables,jaeum,moeum):
        distance = get_distance(x,y)
        all_distance.append((distance,x,y,label))
    all_distance = sorted(all_distance,key=lambda distance: distance[0])
    return all_distance

#?
def get_distance(x,y):
    return math.sqrt(x*x + y*y)
    #plt.show()

#?
def write_file(center_words):
    with open('center_words.csv','w') as f:
        for center_word in center_words:
            print(center_word)
            f.write(str(center_word)+'\n')
#?
def draw_graph(jaeum,moeum):

    plt.title(word,FontProperties=fontprop)
    plt.scatter(jaeum,moeum)
    plt.axis([0,20,0,10])
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
