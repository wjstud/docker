# -*- codind: utf-8 -*-

import pandas as pd

def co2():
    
    df_data = pd.read_excel('ClimateChange.xlsx', sheetname=0) # data sheet
    df_country = pd.read_excel('ClimateChange.xlsx', sheetname=1) # country sheet

    df_data = df_data[df_data['Series code'] == 'EN.ATM.CO2E.KT'] # ����ɸѡ
    df_data = df_data.set_index('Country code') # ����index
    df_data = df_data.drop(['Country name', 'Series code', 'Series name', 'SCALE', 'Decimals'], axis=1) # ȥ������Ҫ����
    df_data = df_data.replace({'..': pd.np.nan}) # ��..ֵ�滻��NaN��ʽ
    df_data = df_data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1) # ǰ�����
#    df_data_drop = df_data.dropna(thresh=2) # ɾ��NaN����
    df_data_new = df_data_drop.apply(sum,axis=1) # ����������ܺ�

    df_country = df_country.set_index('Country code') # ����index
    df_country = df_country.drop(['Capital city','Region','Lending category'],axis=1) #ɾ������Ҫ����

    data = pd.concat([df_data_new,df_country],axis=1) # �ϲ�DataFrame
    data_new = data.dropna() # ɾ��NaN����

    results = pd.concat([data_new.groupby('Income group').sum(),data_new.groupby('Income group').max(),data_new.groupby('Income group').min()],axis=1) # �ϲ�������ܺ�,���ֵ,��Сֵ��DataFrame
    results.columns = ['Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions'] # �滻������
    return results
