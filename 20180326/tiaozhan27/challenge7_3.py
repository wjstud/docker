import pandas as pd
import matplotlib.pyplot as plt

def climate_plot():

    df_data = pd.read_excel('ClimateChange.xlsx', sheetname=0)
    df_data2 = pd.read_excel('GlobalTemperature.xlsx', sheetname=0)

    df1 = df_data.loc[df_data['Series code'].isin(['EN.ATM.CO2E.KT','EN.ATM.METH.KT.CE','EN.ATM.NOXE.KT.CE','EN.ATM.GHGO.KT.CE','EN.CLC.GHGR.MT.CE'])]
    df1_1 = df1.drop(['Country code','Country name','Series code','Series name','SCALE','Decimals',2011],axis=1)
    df1_2 = df1_1.replace({'..':pd.np.nan})
    df1_3 = df1_2.dropna(how='all')
    df1_4 = df1_3.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df1_5 = df1_4.apply(sum)
    df1_6 = (df1_5 - df1_5.min())/(df1_5.max() - df1_5.min())
    df1_6 = pd.DataFrame(df1_6,columns=['Total GHG'])

    df2 = df_data2.loc[:,['Date','Land Average Temperature','Land And Ocean Average Temperature']]
    df2.index = pd.to_datetime(df2.Date)
    df2_1 = df2.drop('Date', axis=1)
    df2_2 = df2_1['1990':'2010']
    df2_3 = df2_2.resample('A').sum()
    df2_4 = (df2_3 - df2_3.min())/(df2_3.max() - df2_3.min())
    df2_5 = df2_4.set_index(df1_6.index)
    
    df12 = pd.concat([df2_5, df1_6],axis=1)

    df34 = df2_1.resample('Q').mean()

    fig = plt.subplot(2,2,1,facecolor='lightgray')
    plt.grid(True,color='white',zorder=0)
    fig.set_xlabel('Years')
    fig.set_ylabel('Values')
    fig.plot(df12.index,df12['Land Average Temperature'],color='blue',zorder=10)
    fig.plot(df12.index,df12['Land And Ocean Average Temperature'],color='green',zorder=10)
    fig.plot(df12.index,df12['Total GHG'],color='red',zorder=10)
    plt.legend(('Land Average Temperature','Land And Ocean Average Temperature','Total GHG'),loc=4)

    fig = plt.subplot(2,2,2)
    fig.set_xlabel('Years')
    fig.set_ylabel('Values')
    fig.bar(df12.index,df12['Land Average Temperature'],width=0.2)
    fig.bar(df12.index+0.2,df12['Land And Ocean Average Temperature'],width=0.2)
    fig.bar(df12.index+0.4,df12['Total GHG'],width=0.2)
    plt.legend(('Land Average Temperature','Land And Ocean Average Temperature','Total     GHG'),loc=2)

    fig = plt.subplot(2,2,3)
    fig.set_xlabel('Quarters')
    fig.set_ylabel('Temperature')
    df34.plot(kind='area', ax=fig)
    
    fig = plt.subplot(2,2,4)
    fig.set_xlabel('Values')
    fig.set_ylabel('Values')
    df34.plot(kind='kde', ax=fig)

    plt.show()

if __name__ == '__main__':
    climate_plot()

