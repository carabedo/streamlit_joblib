import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import streamlit as st
from sklearn.linear_model import ElasticNetCV as eNetCv
from bokeh.plotting import figure
import seaborn as sns

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())


df = pd.read_csv('StudentsPerformance.csv')
df.columns = [x.replace(' ', '_') for x in df.columns]
columnas_categoricas = ['gender', 'race/ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
columnas_respuestas  = ['math_score', 'reading_score', 'writing_score']
df_dummies = pd.get_dummies(df, columns = columnas_categoricas)
X = df_dummies.drop(labels = columnas_respuestas, axis=1)
y = df_dummies[[x for x in df_dummies.columns if x in columnas_respuestas]]





def predict(mod,x_pred):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    
    def math(X_train, y_train,X_pred,X_test):      
        
        model_math = eNetCv(alphas=np.linspace(0.001, 10, 100), cv = 3)
        model_math.fit(X_train, y_train['math_score'])
        y_pred=model_math.predict(X_test)
        output = model_math.predict(X_pred)
        p = figure()
        p.line(y_test['math_score'], y_test['math_score'],  line_width=2)
        p.circle(y_pred, y_test['math_score'], line_width=2)
        return output[0],p

    def read(X_train, y_train,X_pred,X_test):
        model_read = eNetCv(alphas=np.linspace(0.001, 10, 100), cv = 3)
        model_read.fit(X_train, y_train['reading_score'])
        output = model_read.predict(X_pred)
        y_pred=model_read.predict(X_test)
        p = figure()
        p.line(y_test['reading_score'], y_test['reading_score'],  line_width=2)
        p.circle(y_test['reading_score'],y_pred , line_width=2)
        
        return output[0],p

    def write(X_train, y_train,X_pred,X_test):
        
        model_write = eNetCv(alphas=np.linspace(0.001, 10, 100), cv = 3)
        model_write.fit(X_train, y_train['writing_score'])
        y_pred=model_write.predict(X_test)
        output = model_write.predict(X_test)
        p = figure()
        p.line(y_test['writing_score'], y_test['writing_score'],  line_width=2)
        p.circle( y_test['writing_score'],y_pred, line_width=2)
        return output[0],p
    
    mtype = {'math' : math, 'read' : read , 'write' : write }     
    model=mtype[mod]
    pred,p=model(X_train, y_train,x_pred,X_test)
    return pred,p



optl=['math', 'read', 'write']
option =  st.sidebar.selectbox('Que parametro quiere predecir?', optl)

gender =  st.selectbox('gender',('female','male'))
gl=['female','male']

race =  st.selectbox('race',('a','b','c','d','e'))
rl=['a','b','c','d','e']

ed =  st.selectbox('parental_level_of_education',('associate','bachelor','high school','master','college','some high school'))
el=['associate','bachelor','high school','master','college','some high school']

lun =  st.selectbox('lunch',('free','standard'))
ll=['free','standard']

tp =  st.selectbox('test_preparation_course',('complete','none'))
tl=['complete','none']


dm=gl+rl+el+ll+tl
x_pred=np.zeros(len(dm))
x_pred[dm.index(gender)]=1
x_pred[dm.index(race)]=1
x_pred[dm.index(ed)]=1
x_pred[dm.index(lun)]=1
x_pred[dm.index(tp)]=1
x_pred=x_pred.reshape(1, -1)
 
    
if  st.sidebar.checkbox("Heatmap correlacion"):
    xc=X.copy()
    n=optl.index(option)
    xc[option]=y.iloc[:,n].values
    st.write(sns.heatmap(xc.corr()))
    # Use Matplotlib to render seaborn
    st.pyplot()

if st.button('predecir'):
    pred=predict(option,x_pred)
    st.write(pred[0])    
    st.bokeh_chart(pred[1], use_container_width=True)
