#Libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import load
import os


PATH = os.getcwd()
DATA_PATH = PATH + '\\Data\\'
MODELS_PATH = PATH + '\\models\\'
TOKENIZERS_PATH = PATH + '\\tokenizers\\'

stopwordsfile = open(PATH + '\\Data\\english', "r")
stopwords = stopwordsfile.read()
data = pd.read_csv(DATA_PATH + 'stress.csv')
tokenizer = load(TOKENIZERS_PATH + 'tfidf_vectorizer.joblib')
clf = load(MODELS_PATH + 'bagging_classifier.joblib')
#nn_clf = load(MODELS_PATH + 'stress.h5')


class DataEngineering:


    
    def text_filteration(text = data['text']):
        filtered_text = ''
        for char in text:
            if char not in ['/', '%', '&', '#', '@','.',',']: 
                filtered_text += char

        return filtered_text
    
    def string_processing(text):
        if text is str:
            text = DataEngineering.text_filteration(text)
            text = text.lower
        
        else:
            text = str(text)
            text = DataEngineering.text_filteration(text)
            text = text.lower        
    
        return text
    
    def feature_selection(data):
        X = data['text']
        y = data['label']
        return X,y
    
    def stopword_exclude(text, stopwords = stopwords):
        text = str(text)
        text = text.lower()
        words = text.split()  
        filtered_text = [word for word in words if word not in stopwords]
        
        return ' '.join(filtered_text) 


    def fit(data):
        temp = []
        for text in data['text']:
            temp.append(DataEngineering.process(text))
        
        data['text'] = temp
        return data

    
    def process(text):
        text = str(text)
        text = text.lower()
        text = DataEngineering.text_filteration(text)
        text = DataEngineering.stopword_exclude(text)
        text = tokenizer.transform(pd.Series(text))
        return text

    

class Model:
    
    def training(data, clf):
        X,y = DataEngineering.fit(data)
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=10)
        clf.fit(X_train,y_train)
        return clf

    def predecion(input, clf = clf):
        processed_input = DataEngineering.process(input)
        
        return clf.predict(processed_input)[0]
    
    
    

    








        

