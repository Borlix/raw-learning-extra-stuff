# First ML project - A Flower Species Classifier

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris() 
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species']= iris.target

df_for_graph = df.copy()
df_for_graph['species_name'] = pd.Categorical.from_codes(iris.target, iris.target_names)
sns.pairplot(df_for_graph, hue='species_name', markers=["o", "s", "D"])
print("Close the graph window to run the machine learning code!")
plt.show()

from sklearn.model_selection import train_test_split
x = df.drop('species', axis=1)
y = df['species']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=30)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=30)
model.fit(x_train, y_train)

print("Model training complete!")

from sklearn.metrics import accuracy_score

predictions = model.predict(x_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy :{accuracy*100}%")