import pandas as pd

df1 = pd.read_csv('Veri_Seti/alev-coskun.csv', encoding='iso-8859-9')
df1['Yazar'] = 'Alev Coskun'

df2 = pd.read_csv('Veri_Seti/altan-oymen.csv', encoding='iso-8859-9')
df2['Yazar'] = 'Altan Oymen'

df3 = pd.read_csv('Veri_Seti/mujdat-gezen.csv', encoding='iso-8859-9')
df3['Yazar'] = 'Mujdat Gezen'

df4 = pd.read_csv('Veri_Seti/ataol-behramoglu.csv', encoding='iso-8859-9')
df4['Yazar'] = 'Ataol Behramoglu'

df5 = pd.read_csv('Veri_Seti/ozdemir-ince.csv', encoding='iso-8859-9')
df5['Yazar'] = 'Ozdemir ince'


concateddf = pd.concat([df1, df2, df3, df4, df5], ignore_index= True)
concateddf.to_csv('Yazarlar.csv', sep=',', index=False, encoding='utf-8')

print(concateddf)