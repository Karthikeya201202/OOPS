import numpy as np
import pandas as pd
import random

class KMeans:
    def __init__(self,clusters,iterations=None):
        self.clusters=clusters
        self.threshold=1e-2
        self.iterations=iterations
    def fit(self,X):
        # In 1st iteration we randomly assign n clusters
        unique_values=list(set(X))
        intial_clusters=random.sample(unique_values,self.clusters)
        dict_={}
        for i in range(self.clusters):
            dict_[f'cluster_{i}']=[]
        # print("intial_clusters: ", intial_clusters)
        for j in X:
            dist_={}
            for i in range(len(intial_clusters)):
                dist_[i]=abs(intial_clusters[i]-j)
            sorted_dist_=list(sorted(dist_.items(),key=lambda x:x[1]))
            # print(sorted_dist_)
            dict_[f'cluster_{sorted_dist_[0][0]}'].append(j)
        
        num_iterations=self.iterations if self.iterations is not None else 100
        for iteration in range(num_iterations):
            updated_clusters=[np.mean(dict_[f'cluster_{i}']) for i in range(self.clusters)]
            # print("Updated Clusters: ", updated_clusters)
            for i in range(self.clusters):
                dict_[f'cluster_{i}']=[]
            for j in X:
                dist_={}
                for i in range(len(updated_clusters)):
                    dist_[i]=abs(updated_clusters[i]-j)
                sorted_dist_=list(sorted(dist_.items(),key=lambda x:x[1]))
                # print(sorted_dist_)
                dict_[f'cluster_{sorted_dist_[0][0]}'].append(j)
        self.centroids={}
        for cluster in range(self.clusters):
            self.centroids[f'cluster_{cluster}']=np.mean(dict_[f'cluster_{cluster}'])
            
        return self.centroids
    def predict(self,X_test):
        predictions=[]
        for X_ in X_test:
            temp_op={}
            for i in range(self.clusters):
                temp_op[f'cluster_{i}']=abs(X_-self.centroids[f'cluster_{i}'])
            sorted_res=list(sorted(temp_op.items(),key=lambda x:x[1]))
            predictions.append((X_,sorted_res[0][0]))
        # return predictions
        df=pd.DataFrame(predictions,columns=['X','Cluster'])
        return df
    
# import sys
# sys.exit()
               
if __name__=="__main__":
    x=[1,4,6,9,10,12,5,13,9]
    kmeans=KMeans(3)
    print(kmeans.fit(x))
    X_test=[11,14,18]
    print(kmeans.predict(X_test))
    