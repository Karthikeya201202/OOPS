import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
class LinearRegression:
    def __init__(self,learning_rate,iterations=None,max_iterations=1000):
        if iterations==None:
            self.learning_rate=learning_rate
            self.max_iterations=1000
        else:
            self.iterations=iterations
            self.learning_rate=learning_rate
            self.max_iterations=1000
    def fit(self,X,y):
        self.m,self.n=X.shape
        self.w=np.zeros(self.n) #weight matrix
        self.b=0  #bais
        self.X=np.array(X)
        self.y=np.array(y)
        # y_pred=self.predict(self.X)
        # dw= (-2*self.X.T.dot(self.y-y_pred))/self.m
        # db= (-2*np.sum(self.y-y_pred))/self.m
        loss_={}
        iterations_=0
        loss=0
        if self.iterations !=None:
            for i in range(self.iterations):
                y_pred=self.predict(self.X)
                dw=(-2*self.X.T.dot(self.y-y_pred))/self.m
                db=(-2*np.sum(self.y-y_pred))/self.m
                self.w=self.w-self.learning_rate*dw
                self.b=self.b-self.learning_rate*db
        else:
            i=1
            curr_loss=(np.mean((y-y_pred)**2))/self.m
            loss_[0]=curr_loss
            while curr_loss>=loss_[i-1] and i<self.max_iterations:
                self.w=self.w-self.learning_rate*dw
                self.b=self.b-self.learning_rate*db
                y_pred=self.predict(self.X)
                curr_loss=(np.mean((y-y_pred)**2))/self.m
                dw= (-2*self.X.T.dot(self.y-y_pred))/self.m
                db= (-2*np.sum(self.y-y_pred))/self.m
                loss_[i]=curr_loss
                i+=1
            iterations_=i+1
            loss=curr_loss
        
        return self
    def predict(self,X):
        y_pred=X.dot(self.w)+self.b
        
        return y_pred

        
    
def main():
    df=pd.read_csv(r"/Users/karthikeya/Documents/Python/Notebook/BLR/Bengaluru_House_Data.csv")
    X=df.loc[:,['total_sqft']]
    y=df.loc[:,['price']]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
    print(X_train.shape,y_train.shape)
    model=LinearRegression(learning_rate=0.01)
    model.fit(X_train,y_train) 
    y_pred=model.predict(X_test)
    
    return y_pred

if __name__=='__main__':
    main()
    
       
    
        
            
            
        
        
        