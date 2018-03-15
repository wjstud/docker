import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    data = data.loc[:,['Date','Volume']] # 重新选择需要的列
    data['Date'] = pd.to_datetime(data['Date']) # 将Date列转为时间序列
    data = data.set_index(['Date']) # 将Date列设置为index
    total_volume = data.resample('Q').sum() # 按季度重新采样并sum
    second_value = total_volume.sort_values(by='Volume',ascending=False)[1:2] # 选择切片范围
    second_date = second_value.index
    second_volume = second_value['Volume']
    return second_volume[0] # type类型为Series,所以任需［0］
'''
# 标准答案

def q():
    data = pd.read_csv('apple.csv', header=0)
    s = data.Volume # 选择需要的列
    s.index = pd.to_datetime(data.Date) # 索引设置为转换成时间序列的Date列
    second_volume = s.resample('q').sum().sort_values()[-2] # 按季度采样并统计排序
    return second_volume


if __name__ == '__main__':
    print(q())
'''
