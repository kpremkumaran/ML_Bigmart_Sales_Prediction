import streamlit as st  # framework building interactive web application directly from python without an UI
import pandas as pd
import joblib

model = joblib.load("Model/bigmart_model.pkl")

st.set_page_config(page_title="BigMart Sales Prediction", page_icon="🛒", layout='centered')

st.title("🛒 Bigmart Sales Prediction APP")
st.markdown("""This app is going to predict ***Item Outlet Sales*** based on the 
input values I provide, Once done click ***Predict Sales*** button""")

with st.form("input_form"):
    st.header("Enter Product & Outlet Details")
    col1, col2 = st.columns(2)
    with col1:
        item_weight = st.number_input("Item Weight", min_value=0.0, step=0.1)
        item_visibility = st.number_input("Item Visibility", min_value=0.0, step=0.001)
        item_mrp = st.number_input("Item MRP", min_value=0.0, step=0.5)
        outlet_age = st.number_input("Outlet Age", min_value=0, step=1)
        outlet_location_score = st.selectbox("Outlet Location Score", [1, 2, 3])

    with col2:
        item_type = st.text_input("Item Type (e.g 'Dairy', 'Meat')")
        item_category = st.selectbox("Item Category", ["FD", "DR", "NC"])
        outlet_size = st.selectbox("Outlet Size", ['Small', "Medium", "High"])
        outlet_location_type = st.selectbox("Outlet Location Type", ['Tier 1', 'Tier 2', 'Tier 3'])
        outlet_type = st.selectbox("Outlet Type",
                                   ['Supermarket Type1', 'Grocery Store', 'Supermarket Type2', "Supermarket Type3	"])
        Outlet_Identifier = st.selectbox("Outlet Identifier", ['OUT027',
                                                               'OUT013',
                                                               'OUT035',
                                                               'OUT049',
                                                               'OUT046',
                                                               'OUT045',
                                                               'OUT018',
                                                               'OUT017',
                                                               'OUT010',
                                                               'OUT019'])

    # values = st.text_input("Enter multiple MPRs")
    # m_values = [float(v) for v in values.split(',')]
    # st.write("MRPs entered:",m_values)
    # uploaded = st.file_uploder("Enter your CSV",type = ['csv','xlsx'])
    # data = pd.read_csv(uploaded)
    submitted = st.form_submit_button("Predict Sales")

if submitted:
    input_df = pd.DataFrame({
        "Item_Weight": [item_weight],
        "Item_Visibility": [item_visibility],
        "Item_MRP": [item_mrp],
        "Outlet_age": [outlet_age],
        'Outlet_Location_Score': [outlet_location_score],
        'Item_Type': [item_type],
        'Item_Category': [item_category],
        'Outlet_Size': [outlet_size],
        'Outlet_Location_Type': [outlet_location_type],
        'Outlet_Type': [outlet_type],
        'Outlet_Identifier': [Outlet_Identifier]})

    pred = model.predict(input_df)[0]
    st.success(f" Predicted Sales: Rs. {pred:.2f}")
    st.balloons()