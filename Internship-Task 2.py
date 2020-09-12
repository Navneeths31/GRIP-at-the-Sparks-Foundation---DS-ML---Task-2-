from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data1=[[2.5,21],[5.1,47],[3.2,27],[8.5,75],[3.5,30],[1.5,20],[9.2,88],[5.5,60],[8.3,81],[2.7,25],[7.7,85],[5.9,62],[4.5,41],[3.3,42],[1.1,17],[8.9,95],[2.5,30],[1.9,24],[6.1,67],[7.4,69],[2.7,30],[4.8,54],[3.8,35],[6.9,76],[7.8,86]]
data=DataFrame(data1,columns=['Hours','Scores'])
print(data)
print('\n\n\n')

x=data.iloc[:,:-1].values
y=data.iloc[:,1].values
x_train, x_test, y_train, y_test= train_test_split(x, y,train_size=0.80,test_size=0.20,random_state=0)

linearregressor= LinearRegression()
linearregressor.fit(x_train, y_train)
y_predict= linearregressor.predict(x_train)

val1=linearregressor.predict([[9.25]])
val=val1[0]
print("Student who studied for 9.25 hours will get",int(round(val)),"marks")
