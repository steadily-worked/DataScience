1~6 -> 생략

* Fare
7 : Farecolumn에서 NaN인 것들을 추출
8 : Fare_filled라는 column을 새로 만들고 우선 Fare의 값과 같게 설정
9 : Fare의 값이 없는 것들의 Fare_filled 값을 0으로 설정

* Embarked
10, 11 : Embarked가 C, S, Q인 경우 세 가지를 각각 Embarked_C, Embarked_S, Embarked_Q로 분류

* Age
12 : 나이가 15살 미만인 것만 뽑아서 under15라는 새로운 column에 넣음

- 질문
1. FE process below is from David's nb 의 의미
2. 나이 데이터를 그대로 쓰면 예측에 문제가 생기는 이유? 소숫점 때문인가?


* Family Size
13, 14 : SibSp + Parch의 값 + 1의 값을 FamilySize라는 새로운 column에 저장
15, 16 : FamilySize가 1인 사람을 Single에, 2~4인 사람을 Average에, 5 이상인 사람을 Big에 저장

- 질문
1. 13, 14에서 두 개의 값에다가 +1을 한 이유? 본인을 포함하기 때문?

* sex
17 : Sex_encoded라는 새로운 coulmn을 만들고, 남성은 0 여성은 1의 값을 저장

* name
18 : 이부분 좀헷갈리는데 이름을 ,을 기준으로 뒤에 있는 거랑 .을 기준으로 앞에 있는 걸 return 하라는 것 같다
train["Name"].apply(get_title).unique() -> .apply를 잘 모르겠다 어쨌든 성의 종류를 .unique()로 갯수만 나타낸듯?

19 : Name column에서 Mr~Master라는 문자열(.str보고 생각 한 것 .str 처음봄)을 포함하는 경우 각각의 Title을 Mr~Master로 바꿔주기
20 : 피벗테이블화 (각 title의 생존율)
21 : Master라는 문자열을 포함한 경우 Name column을 그대로 Master라는 새 coulmn에 저장.

* Training
22 : Pclass부터 Master까지의 column을 features로 묶었음 (Survived는 제외)
23 : Survived의 column을 label로 묶음
24, 25 : features들을 표로 나타낸 것을 X_train이라는 명령어로 저장
26 : label(그러니까 생존여부)를 데이터화 한 것을 y_train이라는 명령어로 저장
27 : 모르겠다~ DecisionTreeClassifier를 처음 본다. sklearn.tree는 또 어디서 나온거고?
28번부터는 잘 모르겠음!