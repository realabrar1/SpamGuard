import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# nltk.download('punkt')
# nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
        
    return " ".join(y)   

tfidf =pickle.load(open('vectorizer.pkl' , 'rb'))
model = pickle.load(open('model.pkl' , 'rb'))

st.title("E-mail / SMS classifier")

input_sms = st.text_input("Enter the text message")
if st.button('predict'):
      # step 1 : preprocess
      transform_sms = transform_text(input_sms)
      # step 2 : vectorize
      vector_input = tfidf.transform([transform_sms])
      # step 3 : predict
      result = model.predict(vector_input[0])
      # step 4 : display
      if result == 1:
            st.header("It is a spam message")
      else:
            st.header("It is not a spam message")
