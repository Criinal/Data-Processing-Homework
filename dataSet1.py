import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('winemag-data-130k-v2.csv')
dataFrame = pd.DataFrame(data)

# 列举出每个表头，对频数进行输出
print(dataFrame['country'].value_counts())
print('\n')
print(dataFrame['description'].value_counts())
print('\n')
print(dataFrame['designation'].value_counts())
print('\n')
print(dataFrame['points'].value_counts())
print('\n')
print(dataFrame['price'].value_counts())
print('\n')
print(dataFrame['province'].value_counts())
print('\n')
print(dataFrame['region_1'].value_counts())
print('\n')
print(dataFrame['region_2'].value_counts())
print('\n')
print(dataFrame['variety'].value_counts())
print('\n')
print(dataFrame['winery'].value_counts())
print('\n')

# 求5数概括
print(dataFrame.quantile([0, 0.25, 0.5, 0.75, 1]))

# 求缺省值
print(dataFrame.isna().sum())

# 数据可视化
# 直方图
dataFrame['points'].hist()
plt.show()

dataFrame['price'].hist()
plt.show()

# 盒图
dataFrame.boxplot('points')
plt.show()

dataFrame.boxplot('price')
plt.show()


# 缺失值处理，首先输出原数据
print("Info of dataFrame")
print(dataFrame.info())
# 缺失值处理，删除关键数据缺失的数据
dataFrame1 = dataFrame.dropna(subset=['country','description','designation'])
print("Info of dataFrame1")
print(dataFrame1.info())
# 缺失值处理，用 'unknown' 代替非关键数据
print("Info of dataFrame2")
dataFrame2 = dataFrame1.fillna('unknown')
print(dataFrame2.info())

# 另一种处理思路：使用酒的评分与价格的相关性，按照规则，评分越高价格越高
# python苦手不会处理
