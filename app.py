import streamlit as st
import joblib

#load the joblib model
model_nb=joblib.load('spam-ham')

st.title('SPAM HAM CLASSIFIER')
ip=st.file_uploader("Upload an image:")
if image:
    st.image(image, caption="Uploaded image", width=300)

op=model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])

  
  
  
  
               
    
    
    
                     
