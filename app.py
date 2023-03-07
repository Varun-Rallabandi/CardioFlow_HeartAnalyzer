# importing the packages
import streamlit as st
from PIL import Image,ImageOps
# importingthe files
import plotly.express as px
from eda import eda
from ml import ml
from eda import eda


def main():

	menu = ["Home", "Prediction Section" , "Exploratory Data Analysis Section"]

	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Home":

		st.write("<h1 style='text-align: center;'>CardioFlow - Heart Health made Easy-Peasy</h1>", unsafe_allow_html=True)
		img = Image.open("heart.jpg")
		img_resized = ImageOps.fit(img, (int(img.size[0]/2), int(img.size[1]/4)), Image.ANTIALIAS)
		with st.container():
			st.image(img_resized, use_column_width=True)
			st.write("""""")
			st.write("""""")
			st.write("""""")
		st.write("""<h5 style='text-align: center;'>
CardioFlow is an app designed to help users input heart data and detect potential heart problems early on. 
By regularly monitoring your heart data and analyzing it with CardioFlow, you can take proactive steps towards improving 
your heart health and preventing potential heart issues. Whether you're a fitness enthusiast or simply looking to improve
your heart health, CardioFlow is the perfect tool to help you achieve your goals.
		""",unsafe_allow_html=True)
		st.write("""""")
		st.write("""""")
		st.write("""""")
		st.write("""<h1 style='text-align: LEFT;'>
		Data
				""", unsafe_allow_html=True)

		st.write("""
The data we use to train our model is coming from the following link:
- https://archive.ics.uci.edu/ml/datasets/heart+disease

This dataset features data of a newly heart disease patient and a diabetic patient.The dataset includes information such as the patient's age, 
sex, chest pain type, resting blood pressure, serum cholesterol levels, fasting blood sugar levels, resting electrocardiographic results, 
maximum heart rate achieved during exercise, exercise-induced angina, ST depression induced by exercise relative to rest, 
slope of the peak exercise ST segment, number of major vessels colored by fluoroscopy, thalassemia, and the presence or 
absence of heart disease.

The dataset was originally created to help researchers develop and test machine learning algorithms that can accurately predict 
the presence or absence of heart disease based on patient data. The dataset has been widely used in academic and research 
settings to study heart disease and develop new diagnostic and treatment methods. 

	""")

		st.write("<h1 style='text-align: left;'>About this WebApp", unsafe_allow_html=True)
		st.write("<h4 style='text-align: left;'>This app is divided into 3 sections:(Use Tab on the left)", unsafe_allow_html=True)
		st.write("""
	1) **Home Page** - Provides a brief summary of the entire application, including where the data 
	for the prediction comes from. It also gives a quick overview of where to find each section of the 
	WebApp, along with a summary of what each section offers.

	2) **Heart Risk Prediction** - Users are asked to provide various medical information related to heart disease, 
	such as age, gender, blood pressure, cholesterol levels, and other relevant factors. Based on this 
	information, the WebApp will predict the user's risk of developing heart disease, categorizing it as 
	either high or low risk.

	3) **Data Analysis on Dataset** - All the data analysis and visualization parts of the WebApp. 
	This page also provides access to the dataset used in the WebApp, along with some data analytics 
	on that specific dataset. The data analytics are presented in the form of charts and graphs, which help 
	users better understand the patterns and trends in the data.
			""")

	if choice=="Exploratory Data Analysis Section":
		eda()
	if choice == "Prediction Section":
		ml()

main()
