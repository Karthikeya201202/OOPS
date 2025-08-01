import numpy as np
class GradientDescent:
    def __init__(self,X,y,learning_rate,iterations=None):
        self.learning_rate=learning_rate
        self.iterations=iterations
        self.X=X
        self.y=y
        self.weight=0
        self.bias=0
        self.threshold=1e-6
        self.previous_cost=None
        
    def loss_(self,y_pred,y_true):
        self.mse=(np.sum((y_pred-y_true)**2))/len(y_true)
        return self.mse
    
    
    def run(self):
        self.current_cost=[]
        self.current_weights=[]
        num_iterations=self.iterations if self.iterations is not None else 1000
        if self.iterations!=None:
            for i in range(num_iterations):
                y_pred=self.weight*self.X+self.bias
                mse=self.loss_(y_pred,self.y)
                if self.previous_cost is not None and abs(mse-self.previous_cost) <self.threshold:
                    break
                self.current_cost.append(mse)
                self.current_weights.append(self.weight)
                # Calculating the gradients
                weight_derivative = -(2/len(self.y)) * sum(self.X * (self.y-y_pred))
                bias_derivative = -(2/len(self.y)) * sum(self.y-y_pred)
                self.previous_cost=mse
                self.weight=self.weight-self.learning_rate*(weight_derivative)
                self.bias=self.bias-self.learning_rate*(bias_derivative)
            self.best_score_=mse
            self.optimal_weight=self.weight
        # else:
        #     for i in range(1000):
        #         y_pred=self.weight*self.X+self.bias
        #         mse=self.loss_(y_pred,self.y)
        #         if self.previous_cost is not None and abs(mse-self.previous_cost) <self.threshold:
        #             break
        #         self.current_cost.append(mse)
        #         self.current_weights.append(self.weight)
        #         # Calculating the gradients
        #         weight_derivative = -(2/len(self.y)) * sum(self.X * (self.y-y_pred))
        #         bias_derivative = -(2/len(self.y)) * sum(self.y-y_pred)
        #         self.previous_cost=mse
        #         self.weight=self.weight-self.learning_rate*(weight_derivative)
        #         self.bias=self.bias-self.learning_rate*(bias_derivative)
        #     self.best_score_=mse
        #     self.optimal_weight=self.weight
        return self.best_score_ , self.optimal_weight
    
if __name__=="__main__":
    X = np.array([32.50234527, 53.42680403, 61.53035803, 47.47563963, 59.81320787,
           55.14218841, 52.21179669, 39.29956669, 48.10504169, 52.55001444,
           45.41973014, 54.35163488, 44.1640495 , 58.16847072, 56.72720806,
           48.95588857, 44.68719623, 60.29732685, 45.61864377, 38.81681754])
    Y = np.array([31.70700585, 68.77759598, 62.5623823 , 71.54663223, 87.23092513,
           78.21151827, 79.64197305, 59.17148932, 75.3312423 , 71.30087989,
           55.16567715, 82.47884676, 62.00892325, 75.39287043, 81.43619216,
           60.72360244, 82.89250373, 97.37989686, 48.84715332, 56.87721319])
    
    learning_rate=0.01
    iterations=100
    
    gd=GradientDescent(X,Y,learning_rate=learning_rate,iterations=iterations)
    best_score,weights=gd.run()
    print(best_score,weights)
    
                
                
        
                    
                
        
        