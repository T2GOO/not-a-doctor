# **Chest X-Ray Classifier**

This project is a web-based application that uses a Convolutional Neural Network (CNN) to analyze chest X-ray images and classify them into specific lung conditions. It provides a user-friendly interface where users can upload X-ray images to receive predictions. While the tool aims to assist in decision-making, it is not a substitute for professional medical advice.

---

## **Features**

- 📷 **Upload X-ray Images**: Easily upload chest X-rays for analysis.
- 🧠 **AI-Powered Predictions**: Classifies lung conditions using a trained CNN model.
- 🎨 **Modern UI**: Intuitive and responsive design for seamless interaction.
- 🔎 **Condition Classification**: Supports classification for conditions such as:
  - COVID-19
  - Viral Pneumonia
  - Normal
- 🚀 **Real-time Results**: Displays predictions with confidence percentages and visual progress bars.

---

## **Getting Started**

### Prerequisites
Make sure you have the following installed:
- Python 3.8 or later
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chest-xray-classifier.git
   cd chest-xray-classifier
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Place your trained CNN model (`model.h5`) in the root directory.

---

## **Usage**

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Upload an X-ray image, and the tool will display predictions for the uploaded image.

---

## **Project Structure**

```plaintext
├── app.py                            # Backend application logic (Flask)
├── static/
│   ├── style.css                     # CSS for the frontend
│   ├── script.js                     # JavaScript for interactivity
├── templates/
│   ├── index.html                    # Main HTML file for the UI
├── model/
│   ├── checkpoints/
│   │   ├── cp.weights.h5             # checkpoints during model training
│   ├── main/
│   │   ├── model_VGG19_512.h5        # main model
│   ├── VGG19/                        # VGG19 fine tuned models...
│   │   ├── model_VGG19_256.h5        
│   │   ...                           
│   ├── model_VGG19.h5
│   ...
├── data/
│   ├── archive/                      # original data...
│   │   ├── test/
│   │   │   ├── Covid/
│   │   │   │   ├── image1.png
│   │   │   │   ├── image2.png
│   │   │   │   ...
│   │   │   ├── Normal/
│   │   │   │   ├── image1.png
│   │   │   │   ├── image2.png
│   │   │   │   ...
│   │   │   ├── Viral Pneumonia/
│   │   │       ├── image1.png
│   │   │       ├── image2.png
│   │   │       ...
│   │   ├── train/
│   │       ├── Covid/
│   │       │   ├── image1.png
│   │       │   ├── image2.png
│   │       │   ...
│   │       ├── Normal/
│   │       │   ├── image1.png
│   │       │   ├── image2.png
│   │       │   ...
│   │       ├── Viral Pneumonia/
│   │           ├── image1.png
│   │           ├── image2.png
│   │       ...
│   ├── current/                      # augmented data...
│       ├── test/
│       │   ├── Covid/
│       │   │   ├── image1.png
│       │   │   ├── image2.png
│       │   │   ...
│       │   ├── Normal/
│       │   │   ├── image1.png
│       │   │   ├── image2.png
│       │   │   ...
│       │   ├── Viral Pneumonia/
│       │       ├── image1.png
│       │       ├── image2.png
│       │       ...
│       ├── train/
│           ├── Covid/
│           │   ├── image1.png
│           │   ├── image2.png
│           │   ...
│           ├── Normal/
│           │   ├── image1.png
│           │   ├── image2.png
│           │   ...
│           ├── Viral Pneumonia/
│               ├── image1.png
│               ├── image2.png
│               ...
├── src/
│   ├── lab/
│       ├── build_main_modele.ipynb       # main model factory
│       ├── data_augmentation.ipynb       # Notebook to augment data
│       ├── evaluate_models.ipynb         # Model comparasion
│       ├── lab_model.ipynb               # Deep learning Research
│       ├── model_optimisation.ipynb      # Notebook to find an optimised model
├── model.h5                              # Pre-trained CNN model
├── requirements.txt                      # Python dependencies
└── README.md                             # Project documentation
```

---

## **Example**

### **Input**
An X-ray image uploaded through the interface.
You can try with an image from data/archive/test/Covid...

### **Output**
Predictions displayed with:
- Confidence scores
- Bar visualizations for each condition

---

## **Limitations**

- **Not a Medical Tool**: This application is for educational and research purposes only. It should not be used for diagnosing or treating medical conditions.
- **Model Accuracy**: Predictions depend on the quality of the training data and may vary.
- **ANI**: The only task is to predict a lung conditions. Try it on a car image, it will potentially predict a Covid...

---

## **Contributing**

Contributions are welcome! If you have suggestions or want to report a bug, feel free to open an issue or submit a pull request.

---

## **License**

This project is licensed under the [MIT License](LICENSE).

---

## **Acknowledgments**

- This project uses **Keras** and **TensorFlow** for deep learning.
- The interface is built with **Flask** and styled using custom CSS.
