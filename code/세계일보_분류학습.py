import pandas as pd
import numpy as np
from konlpy.tag import *
twitter = Twitter()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#파일 불러오기
article = pd.read_csv('segye_news.csv', encoding = 'CP949')

#morphs
article["morphs"] = 0
for i in range(article["article"].count()):
    article["morphs"][i] = twitter.morphs(article["article"][i])

#파일 출력
article.to_csv("segye_news.csv")

#파일 다시 불러오기
article = pd.read_csv('segye_news.csv', encoding = 'CP949')
type(article["article"][0])
morphs = []
for i in range(article["morphs"].count()):
    morphs.append(article["morphs"][i])
    
#tf-idf
article_tfidf = TfidfVectorizer().fit(morphs)
morphs_matrix = article_tfidf.transform(morphs).toarray()


#normalizer
normalizer = Normalizer()
norm_morphs = normalizer.fit_transform(morphs_matrix)

#svm or naive bayes

#결과값 array 형태로 만들기
field = np.zeros((article["field"].count(), 1))
for i in range(article["field"].count()):
    if (article["field"][i] == "정치"):
        field[i] = 0 #발라드 가변수
    elif (article["field"][i] == "경제"):
        field[i] = 1 #댄스 가변수
    elif (article["field"][i] == "연예"):
        field[i] = 2 #랩/힙합 가변수
    elif (article["field"][i] == "스포츠"):
        field[i] = 3 #알앤비/어반 가변수
    else:
        pass
    
X_train, X_test, Y_train, Y_test = train_test_split(
        norm_morphs, field, random_state=42)

logreg = LogisticRegression().fit(X_train, Y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg.score(X_train, Y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg.score(X_test, Y_test)))

logreg100 = LogisticRegression(C=100).fit(X_train, Y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg100.score(X_train, Y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg100.score(X_test, Y_test)))

logreg001 = LogisticRegression(C=0.01).fit(X_train, Y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg001.score(X_train, Y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg001.score(X_test, Y_test)))