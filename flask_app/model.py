import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#데이터 로드, 전처리
df1 = pd.read_csv('modelData.csv')

colList = list(df1.columns)
colList.remove('id')
colList.remove('expectedmoney')
colList.remove('Unnamed: 0')

#print(colList)
#학습데이터와 테스트데이터 분할
x_data=df1.loc[:, colList]
y_data=df1.loc[:, 'expectedmoney']
x_train, x_test, y_train, y_test=train_test_split(x_data,
                                                  y_data,
                                                  test_size=0.2,
                                                  shuffle=True,
                                                  random_state=12)

#선형 회귀 모형
lr=LinearRegression()
lr.fit(x_train, y_train)
y_test_pred=lr.predict(x_test)

# 입력예시
# x_input = pd.DataFrame({'capital':20000	,'foodtype_고기':1,'foodtype_디저트':0	,'foodtype_베이커리': 0,'foodtype_분식':0 ,	'foodtype_일식': 0,	'foodtype_중식': 0,	'foodtype_치킨':0, 'foodtype_커피':0,	'foodtype_패스트푸드': 0,	'foodtype_퓨전음식': 0,	'foodtype_한식':0,	'locate_경기':0,	'locate_서울':1,	'locate_인천': 0},index = [0])
# #print(x_input)
# income = lr.predict(x_input)
# print(income)

def income_predict(capital = 0, meat= 0,dessert = 0	,bakery= 0,bunsic = 0 ,	jp= 0,	ch= 0,	chicken = 0, coffe = 0,	fast= 0,	fusion= 0,	korea = 0,	gyeonggi = 0,	seoul = 0,	incheon= 0):
    x_input = pd.DataFrame({'capital':capital	,'foodtype_고기':meat,'foodtype_디저트':dessert	,'foodtype_베이커리': bakery,'foodtype_분식':bunsic,	'foodtype_일식': jp,	'foodtype_중식': ch,	'foodtype_치킨':chicken, 'foodtype_커피':coffe,	'foodtype_패스트푸드': fast,	'foodtype_퓨전음식': fusion,	'foodtype_한식':korea,	'locate_경기':gyeonggi,	'locate_서울':seoul,	'locate_인천': incheon},index = [0])
    income = lr.predict(x_input)
    income = int(income)
    return income
    
#income_predict(capital = 20000, meat=1,seoul=1)
