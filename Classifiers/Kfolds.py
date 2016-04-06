
from sklearn import tree
from sklearn.cross_validation import KFold
from sklearn import svm
import numpy as np
import csv

file="Normalized_big.csv"

categories = {
	'HW': 0, 
	'AW': 1
}


cols=["HFF%","HGF","HGA","HG+/-","HPPSuccess","HPKSuccess","HOSh%","HOSv%","HPDO","Hwinstreak","HStanding","AFF%","AGF","AGA","AG+/-","APPSuccess","APKSuccess","AOSh%","AOSv%", "APDO","Awinstreak","AStanding","Class"]

data=[]
target=[]
with open(file,'r') as d:
			r = csv.reader(d)
			i=0
			for row in r:
				data.append([])
				for item in row[:len(row)-1]:
					data[i].append(float(item))
				data[i]=np.array(data[i])
				target.append(int(row[len(row)-1]))
				i=i+1

target=np.array(target)
data=np.array(data)
clf = svm.LinearSVC(max_iter=2000000)
scores=[]
cv = KFold(len(target), n_folds=10)
for i, (train, test) in enumerate(cv):
		print "Fold "+str(i)+" : "
		clf.fit(data[train],target[train])
		print "Predictions : "
		print clf.predict(data[test])
		print "Score : "
		print clf.score(data[test],target[test])
		scores.append(clf.score(data[test],target[test]))
print scores
scores=np.array(scores)
print "Mean : " + str(np.mean(scores))







'''
tree = tree.DecisionTreeClassifier()

# categories.values() returns a list of the values (in order) - which is nice :)
string_tree = string_tree.fit(data, categories.values())

# closest to bob - or category 0
test = [
	[20, 182], 
]

print string_tree.predict(test)
'''