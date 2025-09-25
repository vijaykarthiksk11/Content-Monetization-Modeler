import streamlit as st
import pandas as pd
import joblib

# -------------------------
# Config
# -------------------------
st.set_page_config(page_title="YouTube Ad Revenue Predictor", layout="centered")

# Gradient background + custom card CSS
st.markdown("""
<style>
/* Style Streamlit buttons */
div.stButton > button:first-child {
    background-color: #ff0000;   /* YouTube red */
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
    transition: 0.3s;
}

/* Hover effect */
div.stButton > button:first-child:hover {
    background-color: #cc0000;   /* darker red */
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Load model
# -------------------------
MODEL_PATH = r"C:\Users\11vij\OneDrive\Desktop\Youtube_project\Linear Regression.pkl"
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# -------------------------
# Header
# -------------------------
st.markdown("<h1 style='text-align:center'> YouTube Ad Revenue Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:rgba(255,255,255,0.8)'>Predict your estimated ad revenue based on video performance.</p>", unsafe_allow_html=True)
st.write("---")

# -------------------------
# Sidebar for inputs
# -------------------------
st.sidebar.header("📥 Enter Inputs")

views = st.sidebar.number_input("Views", min_value=0, step=1000, value=10000)
likes = st.sidebar.number_input("Likes", min_value=0, step=100, value=500)
comments = st.sidebar.number_input("Comments", min_value=0, step=10, value=50)
watch_time = st.sidebar.number_input("Watch Time (minutes)", min_value=0, step=1, value=500)
video_length = st.sidebar.number_input("Video Length (minutes)", min_value=0, step=1, value=10)
subscribers = st.sidebar.number_input("Subscribers", min_value=0, step=100, value=10000)

category = st.sidebar.selectbox("Category", ["Entertainment", "Education", "Gaming", "Music", "Technology"])
device = st.sidebar.selectbox("Device", ["Mobile", "Desktop", "Tablet"])
country = st.sidebar.selectbox("Country", ["US", "India", "UK", "Canada", "Other"])

# -------------------------
# Prediction section
# -------------------------
if st.button("🔮 Predict Revenue"):
    # Prepare input
    input_dict = {
        "views": views,
        "likes": likes,
        "comments": comments,
        "watch_time_minutes": watch_time,
        "video_length_minutes": video_length,
        "subscribers": subscribers,
        "category": category,
        "device": device,
        "country": country
    }
    input_df = pd.DataFrame([input_dict])

    # Encoding align
    input_encoded = pd.get_dummies(input_df)
    try:
        model_features = model.feature_names_in_
    except Exception:
        st.error("The model does not have `feature_names_in_`. Retrain with sklearn for compatibility.")
        st.stop()

    input_encoded = input_encoded.reindex(columns=model_features, fill_value=0)

    try:
        prediction = model.predict(input_encoded)[0]
        st.markdown(
            f"""
            <div style="background:linear-gradient(90deg, #ff0000, #ffffff); 
                        padding:20px; border-radius:15px; text-align:center; 
                        color:white; font-size:20px; font-weight:bold; margin-top:20px;">
                💰 Estimated Ad Revenue: ${prediction:.2f} USD
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Prediction error: {e}")

else:
    st.info("Enter inputs in the sidebar and click **Predict Revenue** to see the result.")

# -------------------------
# Tips
# -------------------------
st.markdown("""
<div class='card' style='margin-top:20px'>
<h3>💡 Tips to Improve Revenue</h3>
<ul>
<li>Increase average watch time & engagement.</li>
<li>Target high CPM regions (e.g., US, UK).</li>
<li>Encourage likes & comments for algorithm boost.</li>
</ul>
</div>
""", unsafe_allow_html=True)
