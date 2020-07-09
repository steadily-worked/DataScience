#7/9 멋쟁이사자처럼 데이터사이언스 스터디 기록

import pandas as pd

df = pd.read_csv('Downloads/titanic.csv') #타이타닉 데이터셋을 이용한 데이터 분석

df['Total'] = df.loc[:, 'SibSp':'Parch'].sum(axis='columns') #Total(SibSp + Parch) column 추가
df[df['Total'] == 0] #(합이 0인 row 찾기)
boolean1 = (df['Total'] == 0) & (df['Survived'] == 1) #동반자가 없는 사람 중 생존자
boolean2 = (df['Total'] != 0) & (df['Survived'] == 1) #동반자가 최소 한 명 이상 있는 사람 중 생존자
# boolean1과 2를 통해 동반자의 여부가 생존에 영향이 있었는지를 분석했음.
# 각 boolean의 값을, Survived와 무관한 양으로만 뽑은 값으로 나눠서 비율로 비교함.
# 결과적으로 동반자가 있는 쪽의 생존율이 20% 이상 높았음. (163 / 537 vs 179 / 354)

boolean3 = (df['SibSp'] != 0) & (df['Survived'] == 1 & (df['Parch'] == 0)) #아내, 자식만 데려온 사람들 중 생존자
boolean4 = (df['Parch']== 0) & (df['Survived'] == 1) & (df['SibSp'] != 0) #직계,친척만 데려온 사람들 중 생존자
# boolean3과 4를 통해 친척을 데려온 사람과 본인의 가족을 데려온 사람의 생존율을 비교했음.
# boolean3과 4의 값을, Survived와 무관한 양으로만 뽑은 값으로 나눠서 비율로 비교함.
# 결과적으로 아내, 자식을 데려온 사람의 생존율이 더 높았으나 .. 유의미한 결과라고 보긴 어렵다.

df.loc[df['Pclass'] == 1, 'Wealth'] = 'Rich'
df.loc[df['Pclass'] == 2, 'Wealth'] = 'Normal'
df.loc[df['Pclass'] == 3, 'Wealth'] = 'Poor'
# Wealth라는 새로운 column을 만들고, Pclass의 수준에 따라 Rich에서 Poor까지 분류했음.
boolean5 = df[(df['Wealth'] == 'Poor') & df['Fare'] != 0]
boolean5.loc[:, 'Fare'].sum() / len(boolean5) #Poor에 해당하는 자들의 평균 지불 금액
boolean6 = df[(df['Wealth'] == 'Normal') & df['Fare'] != 0]
boolean6.loc[:, 'Fare'].sum() / len(boolean6) #Normal에 해당하는 자들의 평균 지불 금액
boolean7 = df[(df['Wealth'] == 'Rich') & df['Fare'] != 0]
boolean7.loc[:, 'Fare'].sum() / len(boolean7) #Rich에 해당하는 자들의 평균 지불 금액
# boolean 5,6,7을 통해 1,2,3등석에 해당하는 사람들이 평균적으로 지불한 가격을 분석했음.
# 결과적으로 Poor -> 13.78, Normal = 21.35, Rich = 86.14만큼 지불. 2등석과 1등석의 가격 차이가 매우 큼.

df[(df['Embarked'] == 'S') & (df['Pclass'] == 1)]
df[(df['Embarked'] == 'C') & (df['Pclass'] == 1)]
df[(df['Embarked'] == 'Q') & (df['Pclass'] == 1)]
# 세 코드로, S와 C, Q 각 지역에서의 1등석의 비율을 측정했음.
boolean8 = df[(df['Embarked'] == 'Q') & (df['Age'] > 0)]
boolean8['Age'].sum() / len(boolean8['Age'])
boolean9 = df[(df['Embarked'] == 'C') & (df['Age'] > 0)]
boolean9['Age'].sum() / len(boolean9['Age'])
boolean10 = df[(df['Embarked'] == 'S') & (df['Age']  > 0)]
boolean10['Age'].sum() / len(boolean10['Age'])
# boolean 8,9,10을 통해 S와 C, Q 각 지역 사람들의 평균 나이를 계산했음.