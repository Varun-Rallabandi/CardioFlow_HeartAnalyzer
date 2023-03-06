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
		st.write("""

The data that we use in this particular app contain the features of a newly heart disease patient 
or a diabetic patient.
		""")

		st.write("""
- https://archive.ics.uci.edu/ml/datasets/heart+disease
	""")

		st.write("# App Content")
		st.write("""
	- This app has four sections
	1) Home Page - The page you are currently in

	2) Prediction- The page in which you will be asked to give the information on all the medical aspects
		and we will predict the desired the output  

	3) Exploratory Data Analysis - The page in which you will find all the Data Analysis and Visualization Parts

			""")

	if choice=="Exploratory Data Analysis Section":
		eda()
	if choice == "Prediction Section":
		ml()

main()
