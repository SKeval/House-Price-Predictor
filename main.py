import pickle 
#import streamlit as st
import pandas as pd
import numpy as np

# model = pickle.load(open('pipe.pkl','rb'))
# df = pd.read_csv("housing_price_dataset.csv")
# neighborhoods = df['Neighborhood'].unique()

# st.title('Housing Price Prediction App')
# st.markdown('This app predicts the Price of House based on its Features.')

# sqft = st.number_input('Square Foots', min_value=0, max_value=5000, value=1, step=10)
# bed = st.number_input('Number of BedRooms', min_value=1, max_value=5, value=1, step=1)
# bath = st.number_input('Number of BathRooms', min_value=1, max_value=4, value=1, step=1)

# neighbor =  st.selectbox('Where is house Located?',sorted(neighborhoods))
# year = st.number_input('In which year house is builded?', min_value=1, max_value=9999, value=1, step=10)



# if st.button('Predict Price'):
#     input = pd.DataFrame([{
#     'Neighborhood': neighbor,
#     'SquareFeet': sqft,
#     'Bedrooms': bed,
#     'Bathrooms': bath,
#     'YearBuilt': year
# }])

#     predict = model.predict(input)
#     st.success(f'The Predicted Housing Price; ${predict[0]:,.2f}')



## Flask App Routing
from flask import Flask, request, render_template,request, redirect


## Create a simple Flask App
app = Flask(__name__)
model = pickle.load(open('pipe.pkl','rb'))

@app.route("/",methods=["POST","GET"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        
        
        
        
        SquareFeet = request.form['squareFeet']
        Bedrooms = request.form['bedrooms']
        Bathrooms = request.form['bathrooms']
        YearBuilt = request.form['yearBuilt']
        Neighborhood = request.form['area']

        input_data = pd.DataFrame([{
                'SquareFeet': SquareFeet,
                'Bedrooms': Bedrooms,
                'Bathrooms': Bathrooms,
                'YearBuilt': YearBuilt,
                'Neighborhood': Neighborhood
            }])
        
        
        if not all([SquareFeet, Bedrooms, Bathrooms, YearBuilt, Neighborhood]):
            return render_template('form.html', prediction_text="Please fill in all fields.")
        try:
            input_data = pd.DataFrame([{
                'SquareFeet': int(SquareFeet),
                'Bedrooms': int(Bedrooms),
                'Bathrooms': int(Bathrooms),
                'YearBuilt': int(YearBuilt),
                'Neighborhood': Neighborhood
            }])
            prediction = model.predict(input_data)
            output = round(prediction[0], 2)
            return render_template('form.html', prediction_text="House Price should be {}$".format(output))
        
        except ValueError as ve:
            return render_template('form.html', prediction_text=f"Invalid input: {ve}")


if __name__=="__main__":
    app.run(debug=True)
    