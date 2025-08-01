import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
class LogisticRegression:
    def __init__(self,iterations,learning_rate):
        self.iterations=iterations
        self.learning_rate=learning_rate
    
    def fit(self,X,y):
        self.X=X
        self.y=y 
        self.m,self.n=self.X.shape #m->records n->features
        self.w=np.zeros(self.n)
        self.b=0 #bais
        
        for i in range(self.iterations):
            A = 1 / ( 1 + np.exp( - (self.X.dot( self.w ) + self.b ) ) ) 
        
            # calculate gradients         
            tmp = ( A - self.y.T )         
            tmp = np.reshape( tmp, self.m )         
            dw = np.dot( self.X.T, tmp ) / self.m          
            db = np.sum( tmp ) / self.m  
            w=w-self.learning_rate*dw
            b=b-self.learning_rate*db
            
            return self
    def predict(self,X_test):
        Z=1 / ( 1 + np.exp( - (X_test.dot( self.w ) + self.b ) ) ) 
        #cut off probability  0.5
        Y=np.where(Z>0.5,1,0)
        return Y
    
    
# def main():
#     df=pd.read_csv(r"")
#     X=
#     y=
#     X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
#     model_logistic=LogisticRegression(iterations=100,learning_rate=0.01)
#     model_logistic.fit(X_train,y_train)
#     y_pred=model_logistic.predict(X_test)
    
    
    
            
            
            
            
        