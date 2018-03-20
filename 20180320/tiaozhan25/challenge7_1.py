# -*- codind: utf-8 -*-

import pandas as pd

def co2():
    
    df_data = pd.read_excel('ClimateChange.xlsx', sheetname=0) # data sheet
    df_country = pd.read_excel('ClimateChange.xlsx', sheetname=1) # country sheet

    df_data = df_data[df_data['Series code'] == 'EN.ATM.CO2E.KT'] # 数据筛选
    df_data = df_data.set_index('Country code') # 更改index
    df_data = df_data.drop(['Country name', 'Series code', 'Series name', 'SCALE', 'Decimals'], axis=1) # 去除不需要的列
    df_data = df_data.replace({'..': pd.np.nan}) # 将..值替换成NaN格式
    df_data = df_data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1) # 前后填充
#    df_data_drop = df_data.dropna(thresh=2) # 删除NaN的行
    df_data_new = df_data_drop.apply(sum,axis=1) # 求所有年份总和

    df_country = df_country.set_index('Country code') # 更换index
    df_country = df_country.drop(['Capital city','Region','Lending category'],axis=1) #删除不需要的列

    data = pd.concat([df_data_new,df_country],axis=1) # 合并DataFrame
    data_new = data.dropna() # 删除NaN的行

    results = pd.concat([data_new.groupby('Income group').sum(),data_new.groupby('Income group').max(),data_new.groupby('Income group').min()],axis=1) # 合并分组后总和,最大值,最小值的DataFrame
    results.columns = ['Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions'] # 替换列索引
    return results
