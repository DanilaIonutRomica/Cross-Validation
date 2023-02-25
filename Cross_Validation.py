import random
import numpy as np
import matplotlib.pyplot as plt



class Cross_Validation:
    def __init__(self,list_data,list_results,number_of_folds):
        self.list_data=list_data
        self.list_results=list_results
        self.number_of_folds=number_of_folds
        self.excluded_indexs=[]
    
    def get_other_index(self,elem,len_list):
        if elem not in self.excluded_indexs and elem !=len_list:
            return int(elem)
        else:
            other_index=random.randint(0,len_list)
            if other_index not in self.excluded_indexs and other_index != len_list:
                return int(other_index)
            else:
                self.get_other_index(int(other_index),len_list)
    
    def shuffle(self):
        size_of_a_block=int(len(self.list_results)/self.number_of_folds)
        list_indexs_for_each_fold=[]
        indexs=[i for i in range(0,len(self.list_results))]
        other_counter=0
        for i in range(0,self.number_of_folds):
            index_in_i_th_fold=[]
            random.shuffle(indexs)   
            for j in range(0,size_of_a_block):
                 index_in_i_th_fold.append(indexs[other_counter])
                 other_counter+=1
            list_indexs_for_each_fold.append(index_in_i_th_fold)
        
        list_of_folds_with_elements=[]
        list_of_folds_with_results=[]
        for i in range(0,self.number_of_folds):
            elem_in_i_th_fold=[]
            res_in_i_th_fold=[]
            for j in range(0,size_of_a_block):
                elem_in_i_th_fold.append(self.list_data[list_indexs_for_each_fold[i][j]])
                res_in_i_th_fold.append(self.list_results[list_indexs_for_each_fold[i][j]])
            list_of_folds_with_elements.append(elem_in_i_th_fold)
            list_of_folds_with_results.append(res_in_i_th_fold)
        return list_of_folds_with_elements,list_of_folds_with_results
    def plot(self):
        list_of_folds,rez=self.shuffle()
        color=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
                for j in range(self.number_of_folds)]
        for i in range(0,self.number_of_folds):
            plt.plot(list_of_folds[i],'o',color=color[i])
        plt.show()
        
                
                           
list_of_points=[]
list_of_results=[]

for i in range(0,100):
    x=random.randint(0,100)
    y=random.randint(0,100)
    list_of_points.append([x,y])
    if x>50:
        list_of_results.append("Yes")
    else:
        list_of_results.append("No")

print(list_of_points)

c_v=Cross_Validation(list_of_points,list_of_results,3)
list_of_folds,lis_rez=c_v.shuffle()
c_v.plot()
            
        