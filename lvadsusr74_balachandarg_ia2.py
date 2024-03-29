# -*- coding: utf-8 -*-
"""LVADSUSR74-BalachandarG-IA2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JiYHhBWiYUDuAuNI6UqBlhMiTjt8lNtR
"""

import numpy as np
import pandas as pd

#1
rgb_array =np.array([[[255,0,0],[0,255,0],[0,0,255]],
                     [[255,255,0],[255,0,255],[0,255,255]],
                     [[127,127,127],[200,200,200],[50,50,50]]])
print(rgb_array)

#2
import numpy as np
import statistics
individual_data = [167,156,178],[45,67,87],[24,34,56]

a = np.array(individual_data)
b=np.mean((a),axis =0)
c=np.std((a),axis =0)
print(a)
print(b)
print(c)

#3
#considering the 3d array

import numpy as np
arr3 = np.array([[[255,0,0],[0,255,0],[0,0,255]],
                     [[255,255,0],[255,0,255],[0,255,255]],
                     [[127,127,127],[200,200,200],[50,50,50]]])
arr1 = np.ravel(arr3)
print((arr1).reshape(1,27))

#4
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1[:,:1])

#5
arr1 = np.array([[4,5,6],
                 [8,9,3],
                  [-1,2,-1]])
average_arr1=np.mean(arr1,axis=1)
print(average_arr1)

#6
temperature = np.array([[34,22,23],[11,11,12]])
print(temperature)

#7
import pandas as pd
data = {'Name':['Alice','Bob','Charlie','David','Eve','Frank','Grace'],
        'Age':[25,30,35,40,45,50,55],
        'City':['Newyork','Los Angeles','Chicago','Houstan','Miami','Phoenix','Bostan'],
        'Department':['HR','IT','Finance','Marketing','Sales','IT','HR']}
df = pd.DataFrame(data)
employee = (df['Age'] < 45) & (df['Department'] != 'HR')
employees = df[employee]
relevant_detail = employees[['Name','City']]
print(relevant_detail)

#8
product_data = {'Product':['Apples','Bananas','Cherries','Flour'],
                'Category':['Fruit','Fruit','Fruit','Bakery'],
                'Price':[20,10,3,1.50],
                'promotion':[True,False,True,False]}
df = pd.DataFrame(product_data)
above_average_data = df.groupby('Category')['Price'].mean()
#average_data = df['Price'] > df.groupby('Category')['Price'].mean()
print(above_average_data)

#9
employee_data = {'employee':['alice','bob','charlie','david'],
                 'department':['HR','IT','Finance','IT'],
                 'Manager':['john','rachel','emily','rachel']}
project_data = {'employee':['alice','charlie','eve'],
                'project':['p1','p3','p2']}
employee_df = pd.DataFrame(employee_data)
project_df = pd.DataFrame(project_data)
overall_data = pd.merge(employee_df,project_df,on='employee',how='left')
print(overall_data)

#10
data = {'department': ['electronics','electronics','clothing','clothing','homegoods'],
        'salesperson':['alice','bob','charlie','david','eve'],
        'sales':[70000,50000,30000,40000,60000]}
df = pd.DataFrame(data)
sales_info = df.groupby(['department','salesperson'])['sales'].mean()
print(sales_info)