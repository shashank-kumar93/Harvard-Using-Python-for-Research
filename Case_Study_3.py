import numpy as np, random, scipy.stats as ss
import pandas as pd

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]


#Exercise1
data = pd.read_csv("asset-v1_HarvardX+PH526x+2T2019+type@asset+block@wine.csv")

#Exercise2
data['is_red'] = np.where(data['color'] == 'red', 1, 0)

df =   data.drop(['quality', 'high_quality','color'], axis=1)
print (df['is_red'][df.is_red==1])

#Exercise3
import sklearn.preprocessing as skp
from sklearn.decomposition import PCA

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

newdf = df.select_dtypes(include=numerics)

X_scaled = skp.scale(df)

lis = [col for col in newdf.columns]

numeric_data = pd.DataFrame(X_scaled,columns = lis)

pca = PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)
print(principal_components.shape)


#Exercise4
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]

y = principal_components[:,1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show() 

#Exercise5
np.random.seed(1) # do not change this!

x = np.random.randint(0, 2, 1000)
y = np.random.randint(0 ,2, 1000)


def accuracy(predictions, outcomes):
    # write your code here!
    total = len(outcomes)
    count = 0
    for indx,i in enumerate(predictions):
        for indy,j in enumerate(outcomes):
            if indx==indy and i==j:
                count +=1
    return ((count*100)/total)

accuracy(x,y)

#Exercise6
x = np.zeros(len(data['high_quality']))
y = data ['high_quality']

accuracy(x,y)

#Exercise7
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])
library_predictions = knn.predict(numeric_data)
res = accuracy(library_predictions,data["high_quality"])

#Exercise8
random.seed(123)
n_rows = data.shape[0]
selection = random.sample(range(n_rows), 10)

#Exercise9
predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])
my_predictions = []
for p in predictors[selection]:
    my_predictions.append(knn_predict(p, predictors[training_indices,:], outcomes[training_indices], k=5))

percentage = accuracy(my_predictions,data.high_quality.iloc[selection])

 

    
