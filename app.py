#streamlit UI

#import necessary libraries
import pickle
import streamlit as st
import pandas as pd

#Model De-serialization (loading the model)
with open("Linear_model.pkl","rb") as file:
    model=pickle.load(file)

#Encoder De-serialization (loading the model)
with open("label_encoder.pkl","rb") as file1:
    encoder=pickle.load(file1)


# model.predict(data)

#using joblib De-serialization
# import joblib
# file="model.pkl"
# model=joblib.load(file)
#model.predict(data)

#load cleaned dataset
df=pd.read_csv("cleaned_data.csv")

st.set_page_config(page_title="House Price Prediction of Bangalore",page_icon="download.jpg")

with st.sidebar:
    st.title("Bangalore House Price Prediction")
    st.image("download.jpg")

#input fields
#Trained column sequence:	bhk	total_sqft	bath	encoded_loc
location=st.selectbox("Location: ",options=df["location"].unique())
bhk=st.selectbox("BHK: ",options=sorted(df["bhk"].unique()))
sqft=st.number_input("Total Sqft: ",min_value=300)
bath=st.selectbox("No. of restrooms: ",options=sorted(df["bath"].unique()))

#encode the new location
encoded_loc=encoder.transform([location])

#new data preparation
new_data=[[bhk,sqft,bath,encoded_loc[0]]]

#prediction
col1,col2=st.columns([1,2])
if col2.button("Predict House Price"):
    pred=model.predict(new_data)[0]
    pred=round(pred*100000)
    st.subheader(f"Predicted Price: र. {pred}")
    