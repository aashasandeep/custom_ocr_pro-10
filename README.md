# custom_ocr_pro-10
custom_ocr_pro-10
Custom OCR Pro-10

📌 Project Overview

Custom OCR Pro-10 is a text extraction tool that combines Tesseract OCR for preprocessing and EasyOCR for real-time text recognition using a Streamlit app. The project aims to improve OCR accuracy with preprocessing techniques and provide an interactive user experience for text extraction.

🚀 Features

Preprocessing with Pytesseract & OpenCV for better OCR accuracy.

Real-time text extraction using EasyOCR in a Streamlit web app.

Supports multiple languages for text recognition.

Image upload & real-time results for easy use.

🖼️ Preprocessing with Pytesseract & OpenCV

Before applying OCR, preprocessing is performed to improve text recognition accuracy.

🔹 Preprocessing Steps:

Convert Image to Grayscale

Apply Noise Removal (Gaussian Blur)

Thresholding (Otsu’s Binarization)

Edge Detection (Canny Algorithm)

Dilation to Improve Text Regions

📝 Preprocessing Code:



🛠️ Installation & Setup

1️⃣ Install Dependencies:-Install PyTesseract (or EasyOCR):
PyTesseract: If you're using Tesseract and Python, install PyTesseract using pip: pip install pytesseract. 
EasyOCR: If you're using EasyOCR, install it with pip: pip install easyocr. 


2️⃣ Clone the Repository


3️⃣ Run the Streamlit App:- streamlit run app.py 
http://localhost:8501/
