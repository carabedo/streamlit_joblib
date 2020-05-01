import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure




st.latex('f(x) = a\sin( \omega  x)')

a = st.number_input('Insert a',1)

st.write('a = ', a)

b = st.slider('w', 0, 10, 1)

n = st.slider('n', 0, 500, 25) 
  
x=np.linspace(0,10,int(n))
y=a**2*np.tan(b*x)



p = figure(
     title='plot',
     x_axis_label='x',
     y_axis_label='y')

p.line(x, y, legend_label='sin(x)', line_width=2)
p.circle(x, y, legend_label='sin(x)', line_width=2)

st.bokeh_chart(p, use_container_width=True)

