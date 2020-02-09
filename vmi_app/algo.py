# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:21:28 2020

@author: saisr
"""

#from sklearn import metrics
def model_vmi(input_variable):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    inp =input_variable
    
    car=['A','B','C','D','E','F']
    car1=['a','b','c','d','e','f']
    
    A=[]
    list=['C:/Users/Harshith/Dev/cfehome/django_projects/vmi/vmi_app/1_Nano_mean.csv','C:/Users/Harshith/Dev/cfehome/django_projects/vmi/vmi_app/2_New_Honda_city.csv','C:/Users/Harshith/Dev/cfehome/django_projects/vmi/vmi_app/4_Volkswagen_Vento.csv',
          'C:/Users/Harshith/Dev/cfehome/django_projects/vmi/vmi_app/6_hyundai_Verna.csv','C:/Users/Harshith/Dev/cfehome/django_projects/vmi/vmi_app/8_Skoda_Rapid.csv','C:/Users/Harshith/Dev/cfehome/django_projects/vmi/vmi_app/11_Maruti_swift.csv']
    
    for k in range(0,len(list)):
        data=pd.read_csv(list[k])
        l=data.shape
        
        x=data.iloc[:,0:l[1]-1].values
        y=data.iloc[:,l[1]-1].values
        
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
        
        model=LinearRegression()
        model.fit(x_train,y_train)
        
        sum=x[0][:]
        for i in range(1,l[0]):
            sum=sum+x[i][:]
        
        for i in range(0,len(sum)):
            sum[i]=sum[i]/l[0]
        
        sum = [sum]
        q=model.predict(sum)
        q=q.tolist()
        #print cars[k],q
        A.append(q[0])
   
    least=min(A)
    A=[(i/least) for i in A]
    A=[i*5 for i in A]
    A=[round(i,1) for i in A]
    
    print (A)
    flag=0
    
    for p in range(0,len(car)):
        if(inp== car[p] or inp==car1[p]):
            return (A[p])
            flag=1
            
    if(flag==0):
        p="Not Found"
        return (p)
            
        
