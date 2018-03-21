import pandas as pd

def co2():
    df_data = pd.read_excel('ClimateChange.xlsx', sheetname=0) # data sheet
    df_country = pd.read_excel('ClimateChange.xlsx', sheetname=1) # country sheet

    df_data = df_data[df_data['Series code'] == 'EN.ATM.CO2E.KT'] # 数据筛选
    df_data = df_data.set_index('Country code') # 更换index为Country code列
    df_data = df_data.drop(['Country name', 'Series code', 'Series name', 'SCALE', 'Decimals'], axis=1) # 只保留需要计算的列
    df_data = df_data.replace({'..': pd.np.nan}) # 替换空值为NaN
    df_data = df_data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1) # 前后填充
    df_data_drop = df_data.dropna(thresh=2) # 删除NaN值列
    df_data_new = df_data_drop.apply(sum,axis=1) # 求所有行的总和
    df_data_new = pd.DataFrame(df_data_new, columns=['Sum emissions']) # 设置列索引别名

    df_country = df_country.set_index('Country code')
    df_country = df_country.drop(['Capital city','Region','Lending category'], axis=1)

    data = pd.concat([df_data_new,df_country],axis=1) # 合并DataFrame
    data = data.dropna() # 删除NaN行

    df1 = data.groupby('Income group').sum() # 分组求和,包含下面Income group所有类别

    df_h1 = data[data['Income group'] == 'High income: OECD'].sort_values(by='Sum emissions',ascending=False).head(1) # 按High income: OECD类别排序并取最高值
    df_l1 = data[data['Income group'] == 'High income: OECD'].sort_values(by='Sum emissions',ascending=False).tail(1) # 按High income: OECD类别排序并取最底值
    df_h2 = data[data['Income group'] == 'High income: nonOECD'].sort_values(by='Sum emissions',ascending=False).head(1)
    df_l2 = data[data['Income group'] == 'High income: nonOECD'].sort_values(by='Sum emissions',ascending=False).tail(1)
    df_h3 = data[data['Income group'] == 'Low income'].sort_values(by='Sum emissions',ascending=False).head(1)
    df_l3 = data[data['Income group'] == 'Low income'].sort_values(by='Sum emissions',ascending=False).tail(1)
    df_h4 = data[data['Income group'] == 'Lower middle income'].sort_values(by='Sum emissions',ascending=False).head(1)
    df_l4 = data[data['Income group'] == 'Lower middle income'].sort_values(by='Sum emissions',ascending=False).tail(1)
    df_h5 = data[data['Income group'] == 'Upper middle income'].sort_values(by='Sum emissions',ascending=False).head(1)
    df_l5 = data[data['Income group'] == 'Upper middle income'].sort_values(by='Sum emissions',ascending=False).tail(1)

    df_h1_n = df_h1.set_index('Income group')
    df_h1_n.columns = ['Highest emissions','Highest emission country']
    df_h1_n = df_h1_n[['Highest emission country','Highest emissions']] # 列掉换
    df_h2_n = df_h2.set_index('Income group')
    df_h2_n.columns = ['Highest emissions','Highest emission country']
    df_h2_n = df_h2_n[['Highest emission country','Highest emissions']]
    df_h3_n = df_h3.set_index('Income group')
    df_h3_n.columns = ['Highest emissions','Highest emission country']
    df_h3_n = df_h3_n[['Highest emission country','Highest emissions']]
    df_h4_n = df_h4.set_index('Income group')
    df_h4_n.columns = ['Highest emissions','Highest emission country']
    df_h4_n = df_h4_n[['Highest emission country','Highest emissions']]
    df_h5_n = df_h5.set_index('Income group')
    df_h5_n.columns = ['Highest emissions','Highest emission country']
    df_h5_n = df_h5_n[['Highest emission country','Highest emissions']]

    df_l1_n = df_l1.set_index('Income group')
    df_l1_n.columns = ['Lowest emissions','Lowest emission country']
    df_l1_n = df_l1_n[['Lowest emission country','Lowest emissions']]
    df_l2_n = df_l2.set_index('Income group')
    df_l2_n.columns = ['Lowest emissions','Lowest emission country']
    df_l2_n = df_l2_n[['Lowest emission country','Lowest emissions']]
    df_l3_n = df_l3.set_index('Income group')
    df_l3_n.columns = ['Lowest emissions','Lowest emission country']
    df_l3_n = df_l3_n[['Lowest emission country','Lowest emissions']]
    df_l4_n = df_l4.set_index('Income group')
    df_l4_n.columns = ['Lowest emissions','Lowest emission country']
    df_l4_n = df_l4_n[['Lowest emission country','Lowest emissions']]
    df_l5_n = df_l5.set_index('Income group')
    df_l5_n.columns = ['Lowest emissions','Lowest emission country']
    df_l5_n = df_l5_n[['Lowest emission country','Lowest emissions']]

    df_h = pd.concat([df_h1_n,df_h2_n,df_h3_n,df_h4_n,df_h5_n])
    df_l = pd.concat([df_l1_n,df_l2_n,df_l3_n,df_l4_n,df_l5_n])
    
    results = pd.concat([df1,df_h,df_l],axis=1)
    return results

if __name__ == '__main__':
    co2()
