# 1. Read a CSV file and print: first 5 rows,info(),describe()
df=pd.read_csv("D:/STUDY/python-basics/data/data.csv")
print(df.head())
print(df.info())
print(df.describe())

# 2. Filter rows where a column value > 50.
print(df[df["Calories"]>350])

# 3. Sort a DataFrame by two columns.
df.sort_values(by=["Calories","Pulse"])

# 4. Group by a column and calculate: mean, max, count
df.groupby("Duration").agg(["mean","max","count"])


# 5. Merge two DataFrames:
df1=pd.read_csv("D:/STUDY/python-basics/data/data.csv")
df2=pd.read_csv("D:/STUDY/python-basics/data/dataclone.csv")
merged=pd.merge(df1,df2,on="Date")
