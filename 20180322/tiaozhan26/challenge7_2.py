import pandas as pd
import matplotlib.pyplot as plt

def co2_gdp_plot():

    df_data = pd.read_excel('ClimateChange.xlsx', sheetname=0)
    df_co2 = df_data[df_data['Series code'] == 'EN.ATM.CO2E.KT']
    df_gdp = df_data[df_data['Series code'] == 'NY.GDP.MKTP.CD']
    df_co2 = df_co2.set_index('Country code')
    df_gdp = df_gdp.set_index('Country code')
    df_co2 = df_co2.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    df_gdp = df_gdp.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    df_co2 = df_co2.replace({'..': pd.np.nan})
    df_gdp = df_gdp.replace({'..': pd.np.nan})
    df_co2 = df_co2.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df_gdp = df_gdp.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    df_co2 = df_co2.apply(sum,axis=1)
    df_gdp = df_gdp.apply(sum,axis=1)
    df_co2 = (df_co2 - df_co2.min())/(df_co2.max() - df_co2.min())
    df_gdp = (df_gdp - df_gdp.min())/(df_gdp.max() - df_gdp.min())
    df_co2 = pd.DataFrame(df_co2,columns=['CO2'])
    df_gdp = pd.DataFrame(df_gdp,columns=['GDP'])
    df_co2 = df_co2.reset_index()
    df_gdp = df_gdp.reset_index()
    country_index = []
    for country in ['CHN', 'USA', 'GBR', 'FRA','RUS']:
        for index in df_co2['Country code'].index:
            if country == df_co2['Country code'][index]:
                country_index.append(index)
    fig = plt.subplot()
    fig.set_title('GDP-CO2')
    fig.set_xlabel('Countries')
    fig.set_ylabel('Values')
    p1 = fig.plot(range(len(df_co2)),df_co2.CO2)
    p2 = fig.plot(range(len(df_gdp)),df_gdp.GDP)
    plt.legend((p1[0],p2[0]),('CO2-SUM','GDP-SUM'))
    plt.xticks(country_index,['CHN', 'USA', 'GBR', 'FRA','RUS'],rotation='vertical')
    china_co2 = '{:.3f}'.format(df_co2[df_co2['Country code'] == 'CHN'].CO2.values[0])
    china_gdp = '{:.3f}'.format(df_gdp[df_gdp['Country code'] == 'CHN'].GDP.values[0])
    china = [china_co2,china_gdp]
    print(china)
    plt.show()

if __name__ == '__main__':
    co2_gdp_plot()
