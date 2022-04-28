import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

dataset = load_iris()
names = dataset.feature_names
features = dataset.data
labels = dataset.target
feature_train, feature_test, label_train, label_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)
model = LogisticRegression(max_iter=500)
model.fit(feature_train, label_train)
label_pred = model.predict(feature_test)
from sklearn.metrics import accuracy_score

print(accuracy_score(label_pred, label_test))
