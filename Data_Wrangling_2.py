import pandas as pd

data = {'Box' : ['Box1', 'Box1', 'Box1', 'Box2','Box2', 'Box2'],'Dimension': ['Length' , 'Width',
        'Height', 'Length', 'Width' , 'Height'],'Value':[6,4,2,5,3,4]}
data2 = pd.DataFrame (data,columns=['Box','Dimension','Value'])


data3 = data2.pivot_table(index=['Box'], columns = 'Dimension', values = 'Value').reset_index()


vol = data3['Volume'] = data3.Length*data3.Width*data3.Height #volume of rectangle = L*W*H