import pandas as pd
import os
import io
import re
f = io.open('/home/wu/桌面/hg2.txt', 'w', encoding='utf-8')
df = pd.read_table('/home/wu/桌面/hg', header=None)

regex=r"[0-9]{1,100}$"


for i in range(len(df)):
    if i == 0 :
        a = df.ix[i, 0]
        b = df.ix[i+1, 0]
        c = re.findall(regex, b)
        d = b.replace(c[0], '')
        f.write(a + '\t' + d + '\n')
    else:
        a = df.ix[i, 0]
        b = df.ix[i+1, 0]
        c = re.findall(regex, a)
        e = re.findall(regex, b)
        d = b.replace(e[0], '')

        print(d)
        f.write(c[0] +'\t' + d + '\n')
f.close()
# print(df)
