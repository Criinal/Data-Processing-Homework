import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('records-for-2015.csv')
dataFrame = pd.DataFrame(data)

# 列举出每个表头，对频数进行输出
print(dataFrame['Agency'].value_counts())
print('\n')
print(dataFrame['Create Time'].value_counts())
print('\n')
print(dataFrame['Location'].value_counts())
print('\n')
print(dataFrame['Area Id'].value_counts())
print('\n')
print(dataFrame['Beat'].value_counts())
print('\n')
print(dataFrame['Priority'].value_counts())
print('\n')
print(dataFrame['Incident Type Id'].value_counts())
print('\n')
print(dataFrame['Incident Type Description'].value_counts())
print('\n')
print(dataFrame['Event Number'].value_counts())
print('\n')
print(dataFrame['Closed Time'].value_counts())
print('\n')

# 求5数概括
print(dataFrame.quantile([0, 0.25, 0.5, 0.75, 1]))

# 求缺省值
print(dataFrame.isna().sum())

# 数据可视化
# 直方图

dataFrame['Area Id'].hist()
plt.show()

dataFrame['Beat'].hist()
plt.show()

dataFrame['Priority'].hist()
plt.show()

dataFrame['Incident Type Id'].hist()
plt.show()


# 盒图
dataFrame.boxplot('Priority')
plt.show()


# 缺失值处理，首先输出原数据
print("Info of dataFrame")
print(dataFrame.info())

# 缺失值处理，删除关键数据缺失的数据
dataFrame1 = dataFrame.dropna(subset=['Area Id', 'Beat', 'Priority'])
print("Info of dataFrame1")
print(dataFrame1.info())

# 缺失值处理，用 'unknown' 代替非关键数据
print("Info of dataFrame2")
dataFrame2 = dataFrame1.fillna('unknown')
print(dataFrame2.info())
