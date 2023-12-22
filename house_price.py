# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 23:42:37 2023

@author: DELL
"""

 

import numpy as np 
import pickle
import streamlit as st

# Load the model
House_Price = pickle.load(open("C:/Users/DELL/Downloads/House_Prediction_model/House_Price1.sav", 'rb'))

# Create a function for prediction
def House_prediction(input_data):
   
    try:
        # Convert input data to numeric values
        inputs_to_numpy = np.asarray(input_data, dtype=float)
        
        # Reshape the data
        reshape_numpy_data = inputs_to_numpy.reshape(1, -1)
        
        # Make prediction
        prediction_tech = House_Price.predict(reshape_numpy_data)
        
        return prediction_tech[0]  # Return the prediction result
    
    except Exception as e:
        print(f"Error in prediction: {e}")
        return None
    
    # Custom CSS style to change input field color


def main():
    # Giving a title 
    st.title('Apartment Price ')
   
    
    
    # Getting the input data from the user
    Area = st.text_input('Size Of the Area In sqrt')
    
    furnishing_options = ['Unfurnished (2)', 'Semi-Furnished (1)', 'Furnished (0)']

    # Selectbox: Allows selecting one option from a list
    selected_furnishing = st.selectbox('Select Furnishing Option:', furnishing_options)
    st.write('You selected:', selected_furnishing)
    Furnishing = st.text_input('Furnishing')
    bhk = ['4 BHK Apartment(5)', '2 BHK Apartment (1)', '3 BHK Apartment (3)','Office Space (8)', 'Shop (9)', '3 BHK House (4)', '2 BHK Builder Floor (2)','6 BHK House (7)', '5 BHK House (6)', 'Showroom(10)', '1 BHK Apartment (0)']


    # Selectbox: Allows selecting one option from a list
    selected_bhk = st.selectbox('Select The BHK in Numerical Value :', bhk)
    st.write('You selected:', selected_bhk , 'So now Please Enter the Numirical Vlaue for prediction')
    
    
   
    BHK = st.text_input('BHK')
    
    Place = ['Sugam Morya (25)', 'Regent Park Kolkata (22)', 'Parvati Garden (20)',
       'Multicon Estelle (18)', 'Golpark Cooperative Housing Society (9)',
       'Shyam Vihar Phase 2 (24)', 'Ballygunge Kolkata (1)', 'Vip Road Kolkata (28)',
       'Urban Heights (27)', 'Thakurpukur Kolkata (26)', 'Rajarhat Kolkata (21)',
       'Batanagar Kolkata (3)', 'Buroshibtalla (6)', 'Parnasree Palli Kolkata (19)',
       'Baguiati Kolkata (0)', 'Behala Kolkata (5)', 'Behala Chowrasta Kolkata (4)',
       'Haridevpur (11)', 'Motilal Gupta Road Kolkata (16)', 'Bangur Avenue (2)',
       'Golf Towers (8)', 'Kankurgachi Kolkata (12)', 'Meena Florence (15)',
       'Greenfield City Classic Premium (10)', 'Classic Tower (7)',
       'Mukundapur Kolkata (17)', 'Koyla Vihar Vasundhara (13)',
       'Lake Town Kolkata (14)', 'Shyam Vihar (23)']


    # Selectbox: Allows selecting one option from a list
    selected_Place = st.selectbox('Select The Place in Numerical Value :', Place)
    st.write('You selected:', selected_Place , 'So now Please Enter the Numirical Vlaue for prediction')
    
    Place = st.text_input('Apartment Name')
    
    # Code for prediction
    diagnosis = ''
    
    # Create a button
    if st.button('Test-Result'):
        st.warning('Please fill in all fields before making a prediction.')
        # Prepare input data
        input_data = [Area, Furnishing, BHK, Place]
        
        # Perform prediction
        prediction_result = House_prediction(input_data)
        
        if prediction_result is not None:
            diagnosis = f"Predicted House Price: {prediction_result} in LAC"
    
    st.success(diagnosis)    

if __name__ == '__main__':
    main()
