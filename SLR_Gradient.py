import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
class LinearRegression:
    def __init__(self,iterations,learning_rate):
        self.iterations=iterations
        self.learning_rate=learning_rate
    def fit(self,X,y):
        self.m,self.n=X.shape
        self.w=np.zeros(self.n) #weight matrix
        self.b=0  #bais
        self.X=X
        self.y=y
        y_pred=self.predict(self.X)
        dw= (-2*self.X.T.dot(self.y-y_pred))/self.m
        db= (-2*np.sum(self.y-y_pred))/self.m
        
        for i in range(self.iterations):
            self.w=self.w-self.learning_rate*dw
            self.b=self.b-self.learning_rate*db
        
        return self
    def predict(self,X):
        y_pred=X.dot(self.w)+self.b
        
        return y_pred

        
    
def main():
    df=pd.read_csv(r"/Users/karthikeya/Documents/Python/Notebook/BLR/Bengaluru_House_Data.csv")
    X=df.loc[:,['total_sqft']].values
    y=df.loc[:,['price']].values
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
    print(X_train.shape,y_train.shape)
    model=LinearRegression(iterations=300,learning_rate=0.01)
    model.fit(X_train,y_train) 
    y_pred=model.predict(X_test)
    
    return y_pred

if __name__=='__main__':
    y_pred=main()
    
       
    
        
            
            
        
        
        