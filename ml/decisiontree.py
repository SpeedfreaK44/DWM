# -*- coding: utf-8 -*-
"""DECISIONTREE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZfQj-HVXsFrPjkFFXENDikbQNCQ6BAku

## Kmeans clustering example
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

df = pd.DataFrame(data={"x0":[7, 5, 7, 3, 4, 1, 0, 2, 8, 6, 5, 3], 'x1':[5, 7, 7, 3, 6, 4, 0, 2, 7, 8, 5, 7]})
df

kmeans = KMeans(n_clusters = 2,init = 'random')

model = kmeans.fit(df)
y_kmeans = model.predict(df)
c = kmeans.cluster_centers_
print('Cluseters are',c)
print(y_kmeans)
model.predict([[10,10]])

plt.scatter(df['x0'],df['x1'],c=y_kmeans,s=50,cmap='Set1')
plt.grid()
plt.scatter(kmeans.cluster_centers_[:,0],
            kmeans.cluster_centers_[:,1],
            c='black',s=200)
plt.xlabel('x0')
plt.xlabel('x1')
print(kmeans.cluster_centers_)

# avg b/w centroid and others cluster points

c1_centroid = c[0]
c2_centroid = c[1]

cluster1_points = df[y_kmeans == 0]
cluster2_points = df[y_kmeans == 1]

m1 = ((cluster1_points['x0']-c1_centroid[0])**2 + (cluster1_points['x1']-c1_centroid[1])**2)**0.5
m2 = ((cluster2_points['x0']-c2_centroid[0])**2 + (cluster2_points['x1']-c2_centroid[1])**2)**0.5

print(m1.mean())
print(m2.mean())

