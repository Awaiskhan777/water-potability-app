import streamlit as st
import numpy as np
import pickle
import joblib
import os

st.set_page_config(page_title="Water Potability App", layout="wide")

# Path Setup
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "svm_model.pkl")
scaler_path = os.path.join(current_dir, "scaler.pkl")

@st.cache_resource
def load_assets():
    assets = {}
    paths = {'model': model_path, 'scaler': scaler_path}
    
    for name, path in paths.items():
        if not os.path.exists(path):
            st.error(f"❌ {name} file missing at {path}")
            return None, None
        
        # Try loading with joblib first (more robust), then pickle
        try:
            assets[name] = joblib.load(path)
        except:
            try:
                with open(path, "rb") as f:
                    assets[name] = pickle.load(f)
            except Exception as e:
                st.error(f"❌ Error loading {name}: {e}")
                st.warning("The file might be corrupted or saved in an incompatible Python version.")
                return None, None
                
    return assets.get('model'), assets.get('scaler')

model, scaler = load_assets()

# --- UI LOGIC ---
st.title("💧 Water Potability App")

if model and scaler:
    st.success("✅ System Ready")
    
    # Inputs
    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    hardness = st.number_input("Hardness", 0.0, 500.0, 150.0)
    solids = st.number_input("Solids", 0.0, 50000.0, 10000.0)
    chloramines = st.number_input("Chloramines", 0.0, 15.0, 7.0)
    sulfate = st.number_input("Sulfate", 0.0, 500.0, 250.0)
    conductivity = st.number_input("Conductivity", 0.0, 1000.0, 400.0)
    organic_carbon = st.number_input("Organic Carbon", 0.0, 30.0, 10.0)
    trihalomethanes = st.number_input("Trihalomethanes", 0.0, 150.0, 80.0)
    turbidity = st.number_input("Turbidity", 0.0, 10.0, 4.0)

    if st.button("Predict"):
        data = np.array([[ph, hardness, solids, chloramines, sulfate, 
                          conductivity, organic_carbon, trihalomethanes, turbidity]])
        try:
            scaled_data = scaler.transform(data)
            prediction = model.predict(scaled_data)
            if prediction[0] == 1:
                st.success("Safe to drink!")
            else:
                st.error("Not safe to drink!")
        except Exception as e:
            st.error(f"Prediction Error: {e}")
else:
    st.info("Please fix the file errors above to continue.")