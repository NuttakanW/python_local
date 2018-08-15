from sklearn import neighbors, datasets
iris = datasets.load_iris()
X,y = iris.data, iris.target
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(X,y)
print(iris.target_names[knn.predict([[3,5,4,2]])])
