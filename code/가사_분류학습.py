import pandas as pd
import numpy as np
from konlpy.tag import *
twitter = Twitter()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#파일 불러오기
music = pd.read_csv('music.csv', encoding = 'CP949')

#morphs
music["morphs"] = 0
for i in range(music["morphs"].count()):
    music["morphs"][i] = twitter.morphs(music["lyrics"][i])

#파일 출력
music.to_csv("music.csv")

#파일 다시 불러오기
music = pd.read_csv('music.csv', encoding = 'CP949')

morphs = []
for i in range(music["morphs"].count()):
    morphs.append(music["morphs"][i])
    
#tf-idf
music_tfidf = TfidfVectorizer().fit(morphs)
morphs_matrix = music_tfidf.transform(morphs).toarray()


#normalizer
normalizer = Normalizer()
norm_morphs = normalizer.fit_transform(morphs_matrix)

#svm or naive bayes

#결과값 array 형태로 만들기
genre = np.zeros((music["genre"].count(), 1))
for i in range(music["lyrics"].count()):
    if (music["genre"][i] == "가요 > 발라드"):
        genre[i] = 0 #발라드 가변수
    elif (music["genre"][i] == "가요 > 댄스"):
        genre[i] = 1 #댄스 가변수
    elif (music["genre"][i] == "가요 > 랩/힙합"):
        genre[i] = 2 #랩/힙합 가변수
    elif (music["genre"][i] == "가요 > 알앤비/어반"):
        genre[i] = 3 #알앤비/어반 가변수
    else:
        pass
    
X_train, X_test, Y_train, Y_test = train_test_split(
        norm_morphs, genre, random_state=42)

logreg = LogisticRegression().fit(X_train, Y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg.score(X_train, Y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg.score(X_test, Y_test)))

logreg100 = LogisticRegression(C=100).fit(X_train, Y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg100.score(X_train, Y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg100.score(X_test, Y_test)))

logreg001 = LogisticRegression(C=0.01).fit(X_train, Y_train)
print("훈련 세트 점수 : {:.3f}".format(logreg001.score(X_train, Y_train)))
print("테스트 세트 점수 : {:.3f}".format(logreg001.score(X_test, Y_test)))
