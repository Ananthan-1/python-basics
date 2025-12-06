import matplotlib.pyplot as plt
import numpy as np

# 1. Create a line plot of numbers 1 to 10 vs their squares.
d1=[1,2,3,4,5,6,7,8,9,10]
d2=[x*x for x in d1]
plt.plot(d1,d2)
plt.show()

# 2. Using a list of 5 categories and 5 values, draw a bar chart.
list1=["Vehicles","Goods","Food","Medicine","Electronics"]
list2=[200,105,5000,900,460]
plt.bar(list1,list2,color="blue")
plt.show()

# 3. Create a scatter plot of two random arrays of size 50.
r1=np.random.rand(50)
r2=np.random.rand(50)
plt.scatter(r1,r2)
plt.show()

# 4. Plot a histogram of 500 normally distributed values.
data1=np.random.randn(500)
plt.hist(data1)
plt.show()

# 5. Load the iris dataset and draw: pairplot,heatmap of correlations
df = sns.load_dataset("iris")
sns.pairplot(df, hue="species")
plt.show()
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()