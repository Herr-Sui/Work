# -*- coding: utf-8 -*-

from pandas import DataFrame
Data = {'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],
        '英语':[90,98,88,77,90]}
Df1 = DataFrame(Data,index = ['张飞','关羽','刘备','典韦','许褚'])
print(Df1)
print('均值\n',Df1.mean(),sep='')
print('最小值\n',Df1.min(),sep='')
print('最大值\n',Df1.max(),sep='')
print('方差\n',Df1.var(),sep='')
print('标准差\n',Df1.std(),sep='')
Df2 = DataFrame(Df1.sum(1),columns=['总成绩'])
Df2 = Df2.sort_values('总成绩', ascending=False)
print('总成绩排名\n',Df2,sep='')
