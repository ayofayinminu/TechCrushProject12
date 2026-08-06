import streamlit as st
import pandas as pd
import joblib


# Page Settings

st.set_page_config(
    page_title="AI Delivery Failure Prediction",
    page_icon="🚚",
    layout="wide"
)


# Load Model

model = joblib.load("delivery_failure_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("🚚 AI Delivery Failure Prediction System")
st.markdown("Predict whether a delivery will fail before dispatch.")

st.divider()

# USER INPUT

col1, col2 = st.columns(2)

with col1:

    delivery_partner = st.selectbox(
        "Delivery Partner",
        ["GIG Logistics","Jumia Logistics","Kwik","DHL Nigeria","FedEx Nigeria","GUO Logistics","Kobo360"]
    )

    state = st.selectbox(
        "State",
        ["Lagos","FCT","Oyo","Ogun","Rivers","Kano","Enugu"]
    )

    city = st.text_input("City")

    package_type = st.selectbox(
        "Package Type",
        ["Electronics","Food","Documents","Fashion","Medicine","Furniture"]
    )

    vehicle_type = st.selectbox(
        "Vehicle Type",
        ["Bike","Car","Van","Truck"]
    )

    delivery_mode = st.selectbox(
        "Delivery Mode",
        ["Standard","Express","Same Day"]
    )

    weather = st.selectbox(
        "Weather",
        ["Sunny","Rainy","Heavy Rain","Harmattan"]
    )

with col2:

    traffic = st.selectbox(
        "Traffic",
        ["Low","Moderate","Heavy"]
    )

    road = st.selectbox(
        "Road Condition",
        ["Good","Fair","Bad"]
    )

    distance = st.number_input(
        "Distance (km)",
        1.0,
        1000.0,
        20.0
    )

    weight = st.number_input(
        "Package Weight (kg)",
        0.1,
        100.0,
        2.0
    )

    expected_time = st.number_input(
        "Expected Time (hours)",
        1.0,
        48.0,
        5.0
    )

    driver_exp = st.slider(
        "Driver Experience",
        0,
        20,
        5
    )

    delivery_attempts = st.slider(
        "Delivery Attempts",
        1,
        5,
        1
    )

    delivery_cost = st.number_input(
        "Delivery Cost (₦)",
        500,
        100000,
        5000
    )


# Prediction

if st.button("Predict Delivery"):

    data = pd.DataFrame(columns=model_columns)
    data.loc[0] = 0

    # Numerical Features
    if "distance_km" in data.columns:
        data.loc[0,"distance_km"] = distance

    if "package_weight_kg" in data.columns:
        data.loc[0,"package_weight_kg"] = weight

    if "expected_time_hours" in data.columns:
        data.loc[0,"expected_time_hours"] = expected_time

    if "driver_experience" in data.columns:
        data.loc[0,"driver_experience"] = driver_exp

    if "delivery_attempts" in data.columns:
        data.loc[0,"delivery_attempts"] = delivery_attempts

    if "delivery_cost_ngn" in data.columns:
        data.loc[0,"delivery_cost_ngn"] = delivery_cost

    # One-Hot Encoded Features
    one_hot_columns = [
        f"delivery_partner_{delivery_partner}",
        f"state_{state}",
        f"city_{city}",
        f"package_type_{package_type}",
        f"vehicle_type_{vehicle_type}",
        f"delivery_mode_{delivery_mode}",
        f"weather_condition_{weather}",
        f"traffic_level_{traffic}",
        f"road_condition_{road}"
    ]

    for col in one_hot_columns:
        if col in data.columns:
            data.loc[0, col] = 1

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    st.divider()

    if prediction == 1:
        st.error("⚠️ Delivery Likely to Fail")
    else:
        st.success("✅ Delivery Likely to Succeed")

    st.metric(
        "Failure Probability",
        f"{probability*100:.2f}%"
    )

    st.progress(float(probability))

    st.subheader("Recommendation")

    if probability > 0.70:
        st.warning("""
- Contact customer before dispatch.
- Verify delivery address.
- Assign an experienced driver.
- Consider an alternative route.
""")

    else:
        st.success("Proceed with delivery.")