import streamlit as st
from joblib import load
import shap
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class TypeSelector(BaseEstimator, TransformerMixin):
    def __init__(self, dtype):
        self.dtype = dtype
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        assert isinstance(X, pd.DataFrame)
        return X.select_dtypes(include=[self.dtype])
    


def load_model():
    model, transformer, explainer = load('app.joblib') 
    return model,transformer, explainer



# funcion que me permite integrar un grafico de shap con streamlit
def st_shap(plot, height=None):
    js=shap.getjs()
    shap_html = f"<head>{js}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height)
    
    
    
# aca empieza la 'pagina'
st.title("Tasador de propiedades")


# entreno el modelo
model,transformer=load_model()


st.header('Elija las variables de la propiedad que quiere predecir:')

tipo = st.selectbox(
     'Tipo de inmueble?',['PH', 'apartment', 'house', 'store'])

lista_barrios=['Mataderos', 'Belgrano', 'Palermo', 'Flores', 'Boedo',
       'Las Cañitas', 'Balvanera', 'Caballito', 'Nuñez', 'Almagro',
       'Colegiales', 'Floresta', 'Barrio Norte', 'Barracas', 'Recoleta',
       'Villa Crespo', 'Puerto Madero', 'Constitución', 'Villa Urquiza',
       'Saavedra', 'Parque Chas', 'Paternal', 'Agronomía',
       'Villa Pueyrredón', 'Coghlan', 'Parque Centenario', 'San Telmo',
       'Monserrat', 'Villa Devoto', 'Boca', 'Parque Avellaneda',
       'San Cristobal', 'Abasto', 'Versalles', 'Villa del Parque',
       'Monte Castro', 'Retiro', 'Parque Patricios', 'San Nicolás',
       'Chacarita', 'Congreso', 'Liniers', 'Centro / Microcentro',
       'Tribunales', 'Once', 'Parque Chacabuco', 'Velez Sarsfield',
       'Catalinas', 'Pompeya', 'Villa Lugano', 'Villa Luro',
       'Villa General Mitre', 'Villa Ortuzar', 'Villa Santa Rita',
       'Villa Soldati', 'Villa Real', 'Villa Riachuelo']

barrio= st.selectbox(
     'Barrio del inmueble?',lista_barrios)

sup = st.slider('Superficie del inmueble?', 5, 100, 2)


habs= st.slider('Cantidad de habitaciones?', 1, 10, 1)



pred=[tipo,barrio,sup,habs]

df_pred=pd.DataFrame([pred], columns=['tipo','barrio','sup','habs'])
X_pred=transformer.transform(df_pred)
lista_features=['sup', 'habs', 'tipo_apartment', 'tipo_house', 'tipo_store',
       'barrio_Agronomía', 'barrio_Almagro', 'barrio_Balvanera',
       'barrio_Barracas', 'barrio_Barrio Norte', 'barrio_Belgrano',
       'barrio_Boca', 'barrio_Boedo', 'barrio_Caballito', 'barrio_Catalinas',
       'barrio_Centro / Microcentro', 'barrio_Chacarita', 'barrio_Coghlan',
       'barrio_Colegiales', 'barrio_Congreso', 'barrio_Constitución',
       'barrio_Flores', 'barrio_Floresta', 'barrio_Las Cañitas',
       'barrio_Liniers', 'barrio_Mataderos', 'barrio_Monserrat',
       'barrio_Monte Castro', 'barrio_Nuñez', 'barrio_Once', 'barrio_Palermo',
       'barrio_Parque Avellaneda', 'barrio_Parque Centenario',
       'barrio_Parque Chacabuco', 'barrio_Parque Chas',
       'barrio_Parque Patricios', 'barrio_Paternal', 'barrio_Pompeya',
       'barrio_Puerto Madero', 'barrio_Recoleta', 'barrio_Retiro',
       'barrio_Saavedra', 'barrio_San Cristobal', 'barrio_San Nicolás',
       'barrio_San Telmo', 'barrio_Tribunales', 'barrio_Velez Sarsfield',
       'barrio_Versalles', 'barrio_Villa Crespo', 'barrio_Villa Devoto',
       'barrio_Villa General Mitre', 'barrio_Villa Lugano',
       'barrio_Villa Luro', 'barrio_Villa Ortuzar', 'barrio_Villa Pueyrredón',
       'barrio_Villa Real', 'barrio_Villa Riachuelo',
       'barrio_Villa Santa Rita', 'barrio_Villa Soldati',
       'barrio_Villa Urquiza', 'barrio_Villa del Parque']
# printeamos el grafico
st.subheader('Analizando la prediccion:')


explainer = shap.TreeExplainer(model)
# genero la expliacion para los datos del test

shap_value = explainer.shap_values(X_pred)
st_shap(shap.force_plot(explainer.expected_value, shap_value, X_pred,feature_names=lista_features))


