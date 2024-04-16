import pickle
import numpy as np
import streamlit as st

loaded = pickle.load(open("/Users/shwetabalasubramoni/Downloads/trained_model.sav", "rb"))

def insurance_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded.predict(input_data_reshaped)
    return float(prediction[0])

def main():
    st.title('Health Insurance Prediction App')

    age = st.text_input('Enter your age')
    sex = st.text_input('Enter your Sex (Enter 1 for female and 0 for male)')
    bmi = st.text_input('Enter your BMI')
    children = st.text_input('Enter the number of children')
    smoker = st.text_input('Are you a smoker (Enter 1 or 0)')
    region = st.text_input('Enter your region (southwest : 1 , southeast : 2 , northeast : 3 , northwest : 4)')

    pred = ''
    if st.button('Insurance Prediction'):
        try:
            age = int(age)
            sex = int(sex)
            bmi = float(bmi)
            children = int(children)
            smoker = int(smoker)
            region = int(region)
            pred = insurance_prediction([age, sex, bmi, children, smoker, region])
        except ValueError:
            pred = 'Invalid input. Please enter numeric values.'

    st.success(f"Your prediction is {pred} dollars")

if __name__ == '__main__':
    main()
