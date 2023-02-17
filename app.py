
import numpy as np
import pickle
import pandas as pd 
import streamlit as st

from PIL import Image


pickle_in = open("demention.pkl","rb")
regressor=pickle.load(pickle_in)

def predict_house_price(Age, EDUC, eTIV	, nWBV, ASF,CDR):
       
    prediction=regressor.predict([[Age, EDUC, eTIV, nWBV, ASF,CDR]])
    print(prediction)
    return prediction

def main():
    st.title("МАШИННОЕ ОБУЧЕНИЕ ПРОГНОЗИРУЕТ БОЛЕЗНЬ АЛЬЦГЕЙМЕРА")
    html_temp = """
    <div style="background-color: tomato;padding:10px">
  <h3 style="color:white;text-align:center;">   Данная программа может помочь врачам предсказать раннюю болезнь Альцгеймера с
  использованием методов машинного обучения на основе МРТ данных </h3>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    m=st.radio("Пол человека:",
        key="M_F",
        options=["Мужчина", "Женщина"], )
    if m=="Женщина":
        M_F=0
    elif m=="Мужчина":
        M_F=1
        
    
    Age= st.text_input("Возраст в годах","")
    EDUC = st.text_input("Образование в годах","")
    eTIV= st.text_input("Расчетный общий внутричерепной объем (eTIV)","")
    nWBV= st.text_input("Нормализация всего объема мозга (nWBV) ","")
    ASF= st.text_input("Коэффициент масштабирования Атласа (ASF) ","")
    CDR= st.text_input("Клинический рейтинг деменции (CDR)","")
       
    
    result=""
    if st.button("Predict"):
        result=int(predict_house_price(Age, EDUC, eTIV, nWBV, ASF,CDR))
    
    st.success('Деменция: {}'.format(result) )
     
     

if __name__=='__main__':
    main()
