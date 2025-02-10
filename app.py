import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# Set parameters
IMG_SIZE = (150, 150)

# Load the model
MODEL_PATH = "best_wheat_classification_model.h5"
model = load_model(MODEL_PATH)

# Define class labels
CLASS_LABELS = ['Healthy', 'Unhealthy', 'Unknown']

# Function to preprocess an image
def preprocess_image(image):
    image = img_to_array(image)
    image = cv2.resize(image, IMG_SIZE)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Function to make predictions
def predict_image(image_path):
    image = load_img(image_path, target_size=IMG_SIZE)
    preprocessed_image = preprocess_image(image)
    prediction = model.predict(preprocessed_image)
    predicted_class = CLASS_LABELS[np.argmax(prediction)]
    confidence = np.max(prediction)
    return predicted_class, confidence

# Function to process video
def predict_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    predictions = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if frame_count % 30 == 0:  # Analyze every 30th frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, IMG_SIZE)
            frame = np.expand_dims(frame / 255.0, axis=0)
            prediction = model.predict(frame)
            predicted_class = CLASS_LABELS[np.argmax(prediction)]
            predictions.append(predicted_class)

    cap.release()
    return predictions

# Streamlit app UI
st.title("Wheat Classification App")
st.write("This application predicts whether wheat is **Healthy**, **Unhealthy**, or **Unknown**.")

# Upload image or video
upload_option = st.selectbox("Choose an option to upload:", ["Image", "Video"])

if upload_option == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        with st.spinner("Processing Image..."):
            # Save and predict
            image_path = f"temp_{uploaded_file.name}"
            with open(image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            predicted_class, confidence = predict_image(image_path)
            st.image(image_path, caption="Uploaded Image", use_column_width=True)
            st.success(f"Prediction: {predicted_class}")
            st.info(f"Confidence: {confidence:.2f}")
            os.remove(image_path)

elif upload_option == "Video":
    uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
    if uploaded_file:
        with st.spinner("Processing Video..."):
            # Save and predict
            video_path = f"temp_{uploaded_file.name}"
            with open(video_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            predictions = predict_video(video_path)
            st.video(video_path)
            st.success("Predictions on Frames:")
            st.write(predictions)
            os.remove(video_path)

# Confusion Matrix and Classification Report Option
if st.button("Show Evaluation Metrics"):
    st.info("This feature requires validation dataset and predictions.")
    st.warning("Add validation data and labels to show metrics.")

st.write("App created by your ML assistant.")
