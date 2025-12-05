# 1. Create a NumPy array of numbers from 1 to 20 and reshape it into 4x5.
arr=np.arange(1,21)
reshaped_arr=arr.reshape(4,5)

# 2. Create a random array of size 10 and find: mean,max,min,standard deviation
randarr=np.random.rand(10)
print("ARRAY:",randarr)
print("MEAN:",randarr.mean())
print("MAX:",randarr.max())
print("MIN:",randarr.min())
print("STD:",randarr.std())

# 3. Create two arrays [1,2,3] and [4,5,6] and perform: addition,multiplication,dot product
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print("SUM:",arr1+arr2)
print("PRODUCT:",arr1*arr2)
print("DOT PRODUCT:",np.dot(arr1,arr2))

# 4. Using np.arange(), create array from 50 to 100 with step 5.
ar=np.arange(50,100,5)
print(ar)

# 5. Create a 3x3 array and extract: first row,last column,middle element
arr3=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(arr3)
print("FIRST ROW:",arr3[0])
print("LAST COLUMN:",arr3[:,-1])
print("MIDDLE ELEMENT:",arr3[1,1])