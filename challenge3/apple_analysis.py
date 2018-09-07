# -*- coding :utf-8 -*-
import pandas as pd
def quarter_volume():
    data=pd.read_csv('apple.csv',header=0)
    data1=data[['Date','Volume']]
    data1['Date1']=pd.to_datetime(data1['Date'])
    del data1['Date']
    data2=data1.set_index('Date1')
    data2=data2.resample('Q').sum()
    data3=data2.sort_values(by='Volume',ascending=False)
    return data3['Volume'].iloc[1]
if __name__=='__main__':
    print(quarter_volume())
