import pickle
from pathlib import Path

import pandas as pd
import streamlit as st


# Paths

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "best_rf_model.pkl"
ENCODER_PATH = BASE_DIR / "models" / "encoders.pkl"
TRAIN_PATH = BASE_DIR / "Dataset" / "train.csv"
FEATURES_PATH = BASE_DIR / "models" / "feature_columns.pkl"
# Page config
st.set_page_config(page_title="House Rent Prediction", page_icon="🏠", layout="centered")
st.title("🏠 House Rent Prediction Dashboard")
st.write("Enter the property details below to predict monthly rent.")


# Load saved artifacts
@st.cache_resource
def load_artifacts():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(ENCODER_PATH, "rb") as f:
        encoders = pickle.load(f)

    with open(FEATURES_PATH, "rb") as f:
        feature_columns = pickle.load(f)

    return model, encoders, feature_columns


@st.cache_data
def load_reference_data():
    return pd.read_csv(TRAIN_PATH)


try:
    model, encoders, feature_columns = load_artifacts()
    train_df = load_reference_data()
except FileNotFoundError as e:
    st.error(f"Required file not found: {e}")
    st.stop()
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()


# Identify feature columns
if "price" not in train_df.columns:
    st.error("The training dataset must contain a 'price' column.")
    st.stop()



categorical_cols = [col for col in feature_columns if col in encoders]
numeric_cols = [col for col in feature_columns if col not in encoders]


# Build input form
st.subheader("Enter Property Details")

user_inputs = {}

with st.form("prediction_form"):
    for col in feature_columns:
        label = col.replace("_", " ").title()

        if col in categorical_cols:
            # LabelEncoder stores original categories in .classes_
            options = list(encoders[col].classes_)
            user_inputs[col] = st.selectbox(label, options=options)

        else:
            # Decide int/float input from train data
            col_series = train_df[col].dropna()

            if col_series.empty:
                # Safe fallback
                user_inputs[col] = st.number_input(label, value=0.0)
            elif pd.api.types.is_integer_dtype(col_series):
                min_val = int(col_series.min())
                max_val = int(col_series.max())
                default_val = int(col_series.median())

                user_inputs[col] = st.number_input(
                    label,
                    min_value=min_val,
                    max_value=max_val,
                    value=default_val,
                    step=1,
                )
            else:
                min_val = float(col_series.min())
                max_val = float(col_series.max())
                default_val = float(col_series.median())

                user_inputs[col] = st.number_input(
                    label,
                    min_value=min_val,
                    max_value=max_val,
                    value=default_val,
                    step=1.0,
                )

    predict_clicked = st.form_submit_button("Predict")


# Prediction
if predict_clicked:
    try:
        processed_input = {}

        for col in feature_columns:
            value = user_inputs[col]

            if col in categorical_cols:
                processed_input[col] = encoders[col].transform([value])[0]
            else:
                processed_input[col] = value

        input_df = pd.DataFrame([processed_input], columns=feature_columns)

        prediction = model.predict(input_df)[0]

        st.success(f"Predicted Rent: ₹ {prediction:,.2f}")

    except Exception as e:
        st.error(f"Prediction failed: {e}")