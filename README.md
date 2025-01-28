# Wheat Classifier 🌾 - CNN-based Classification with Streamlit Web Interface

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?logo=docker&logoColor=white)](https://www.docker.com/)

A deep learning project for wheat classification using Convolutional Neural Networks (CNN), capable of predicting whether the wheat is **normal**, affected by **Fusarium**, or has an **unknown disease**. The project includes a modern web interface powered by Streamlit for real-time predictions.

![App Screenshot](./assets/app_screenshot.png) <!-- Add actual screenshot path -->

## Features ✨

- **CNN-powered Classification**: A robust model trained for wheat disease detection.
- **Streamlit Web Interface**: Easy-to-use interface for uploading and classifying images.
- **Docker Support**: Containerized for effortless deployment across platforms.
- **Cross-Platform**: Compatible with Windows, Linux, and macOS.

## Installation 🛠️

### Prerequisites
- Python 3.10
- Docker (optional)

### Local Setup
```bash
# Clone repository
git clone https://github.com/M-Tayyab06/Wheat_classifier.git
cd Wheat_classifier

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Docker Setup
```bash
# Build Docker image
docker build -t wheat-classifier .

# Run container
docker run -p 8501:8501 wheat-classifier
```

## Usage 🚀

### Running the Application
```bash
# Local run
streamlit run owl.py

# Docker run
docker run -p 8501:8501 wheat-classifier
```

Access the web interface at [http://localhost:8501](http://localhost:8501).

### Making Predictions
1. Upload a wheat sample image through the web interface.
2. View real-time classification results indicating whether the wheat is **normal**, affected by **Fusarium**, or has an **unknown disease**.
3. Explore model confidence scores and visualizations.

## Project Structure 🗂
```plaintext
├── Dockerfile                        # Docker configuration
├── owl.py                            # Streamlit web application
├── best_wheat_classification_model.h5  # Trained model weights (HDF5 format)
├── best_wheat_classification_model.keras # Trained model weights (Keras format)
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

## Contributing 🤝

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments 🎓

- Built with [Streamlit](https://streamlit.io/) for web interface
- Powered by [Keras](https://keras.io/) and [TensorFlow](https://www.tensorflow.org/) for deep learning
- Containerization made possible by [Docker](https://www.docker.com/)

---

**Happy Classifying!** 🚀🌾  
Maintained by [M. Tayyab](https://github.com/M-Tayyab06)
