#importing libraries
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#loading breast cancer data
bs = load_breast_cancer()

#extracting features of the dataset
x = bs.feature_names

#extracting labels of the dataset
y = bs.target_names

print("*"*30)
print(y)
print("*"*30)

#splitting data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(bs.data, bs.target,  test_size=0.3, random_state=1)

#Using Support Vector Classifier
clf = svm.SVC(kernel='linear')
clf.fit(x_train, y_train)
predic = clf.predict(x_test)
print("Using SVM Tree ", accuracy_score(y_test, predic)*100)

#Using DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=50)
clf.fit(x_train, y_train)
predic = clf.predict(x_test)
print("Using Decision Tree ", accuracy_score(y_test, predic)*100)

#Uisng KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=10)
clf.fit(x_train, y_train)
predic = clf.predict(x_test)
a = list(x)
plt.scatter(bs.data[:, 1], bs.target)
plt.show()
print("Using KNN Tree ", accuracy_score(y_test, predic)*100)

#Using LogisticRegression
clf = LogisticRegression()
clf.fit(x_train, y_train)
predic = clf.predict(x_test)
print("Using Logistic Tree ", accuracy_score(y_test, predic)*100)

#Uisng Naive Bayes
clf = GaussianNB()
clf.fit(x_train, y_train)
predic = clf.predict(x_test)
print("Using Gaussian Tree ", accuracy_score(y_test, predic)*100)
