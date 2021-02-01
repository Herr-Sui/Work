# -*- coding: utf-8 -*-

import pandas as pd

Df = pd.read_csv('./car_complain.csv')
Df = Df.drop('problem',axis = 1).join(Df.problem.str.get_dummies(','))

def h(x):
    x = x.replace('一汽-大众','一汽大众')
    return x
Df['brand'] = Df['brand'].apply(h)

#品牌排名
result1 = Df.groupby(['brand'])['id'].agg(['count'])
result1 = result1.sort_values('count',ascending = False)
print(result1)

#车型排名
result2 = Df.groupby(['car_model'])['id'].agg(['count'])
result2 = result2.sort_values('count',ascending = False)
print(result2)

#品牌平均车型排名
result3 = Df.groupby(['brand','car_model'])['id'].agg(['count'])
result3 = result3.sort_values('count',ascending = False)
print(result3)