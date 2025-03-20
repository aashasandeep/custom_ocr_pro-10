# custom_ocr_pro-10
custom_ocr_pro-10![output new csv](https://github.com/user-attachments/assets/4a4f2285-55fa-45c3-ac9b-194b6ab5716e)
![output table image](https://github.com/user-attachments/assets/8850f8d1-99af-4a38-a665-e632aa9a847a)
![pic of pro-10 after selecting bounding box the extracted images](https://github.com/user-attachments/assets/4a43c19e-5f36-4928-adef-eb37a3e4b3df)
![pro-10 pic of image after processing ](https://github.com/user-attachments/assets/6cd76031-0c88-4b3d-a773-eec6ec7eaeed)
![pro-10 pic of image after bounding box](https://github.com/user-attachments/assets/87147586-4997-473e-80f0-2139ee932d2c)
![ocrpic5ppt](https://github.com/user-attachments/assets/a4fadfb5-ccad-4afa-a668-92e1275bf159)
![ocr text extraction app](https://github.com/user-attachments/assets/12c4536e-3acf-434a-861e-6dc5f32913d3)
![ocr pic4 ppt](https://github.com/user-attachments/assets/42178a69-3b22-4dfb-9bcd-01016bfe8bb2)
![ocr pic3 ppt](https://github.com/user-attachments/assets/0258a2c1-ef2e-473a-9fac-1522ba5b7cc6)
![ocr pic-2 ppt](https://github.com/user-attachments/assets/a7b8e265-c825-4183-b63e-75ee81d99ebd)
![ocr logo image](https://github.com/user-attachments/assets/a131fd0a-2f1b-4196-b2bb-992e223e6bdc)


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

🛠️ Installation & Setup

1️⃣ Install Dependencies:-Install PyTesseract (or EasyOCR):
PyTesseract: We are using Tesseract and Python, install PyTesseract using pip: pip install pytesseract. 
EasyOCR: We are using EasyOCR, install it with pip: pip install easyocr. 

3️⃣ Run the Streamlit App:- streamlit run app.py 

🛠️ Technologies Used

Python 🐍

OpenCV 📷 (Image Processing)

Pytesseract 📝 (OCR Preprocessing)

EasyOCR 🔍 (Text Extraction)

Streamlit 🌐 (Web App Interface)
📢 Future Enhancements

✅ Support for more languages in OCR.

✅ Integration with YOLOv3 for text detection before OCR.

✅ Deploy the Streamlit app on Google Cloud / Heroku

Asha Sandeep Kashyap
Regards and Thanks to Shweta mam and Twinkle baid mam for supporting our all projects. 
