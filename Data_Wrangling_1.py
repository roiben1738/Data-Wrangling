import pandas as pd

x1 = {'Student' : ['Ice Bear' , 'Panda' , 'Grizzly'], 'Math' :[80,95,79]}
y1 = pd.DataFrame(x1,columns=['Student','Math'])

x2 = {'Student' : ['Ice Bear' , 'Panda' , 'Grizzly'], 'Electronics' :[85,81,83]}
y2 = pd.DataFrame(x2,columns=['Student','Electronics'])

x3 = {'Student' : ['Ice Bear' , 'Panda' , 'Grizzly'], 'GEAS' :[90,79,93]}
y3 = pd.DataFrame(x3,columns=['Student','GEAS'])

x4 = {'Student' : ['Ice Bear' , 'Panda' , 'Grizzly'], 'ESAT' :[93,89,88]}
y4 = pd.DataFrame(x4,columns=['Student','ESAT'])

d =  pd.merge(y1,y2, how = 'right', on ='Student')
d2 =  pd.merge(d,y3, how = 'right', on ='Student')
d3 =  pd.merge(d2,y4, how = 'right', on ='Student')

final = pd.melt(d3,id_vars= 'Student', value_vars = ['Math' ,'Electronics', 'GEAS' , 'ESAT'])
final2 = final.rename(columns = {'variable':'Subject', 'value':'Grades'})
final3 = final2.sort_values('Student')
final4 = final3.reset_index()
final5 = final4.drop(columns='index')

