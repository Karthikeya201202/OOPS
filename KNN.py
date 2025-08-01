import pandas as pd
import numpy as np

import numpy as np
import pandas as pd
import heapq

class KNeighborsRegressor:
    
    def __init__(self, neighbors: int, metric='euclidean'):
        self.neighbors = neighbors
        self.metric = metric
        
    def euclidean(self, X1, X2):
        dist = np.sqrt(np.sum((X1 - X2) ** 2))  # Generalized for n-dim
        return dist
        
    def fit(self, X, y):
        self.X = X
        self.y = y
        return self
            
    def predict(self, X_test):
        y_pred = []
        for _, row in X_test.iterrows():  # Iterate over rows of X_test
            distances = []
            for i, train_row in self.X.iterrows():  # Iterate over training data (X)
                dist = self.euclidean(train_row.values[:2], row.values[:2])  # Use values directly
                distances.append((dist, i))  # Store distance and index
            
            # Get the nearest neighbors using heapq
            nearest_neighbors = heapq.nsmallest(self.neighbors, distances, key=lambda x: x[0])

            # Predict the mean of the nearest neighbors
            y_pred.append(np.mean([self.y[i] for _, i in nearest_neighbors]))
        
        return np.array(y_pred)  # Return predictions as a NumPy array

    
            
            
            
        
            
    
    
                
                    
                    
                    
                    
            
            
            
            
        